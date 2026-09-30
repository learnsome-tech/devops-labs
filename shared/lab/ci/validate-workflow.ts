// Validates a GitHub Actions workflow file without GitHub.
//
// A workflow is the one artifact in this course that a learner will copy
// straight into a repository, so a listing that is subtly wrong is worse than
// no listing at all. This parses the YAML and checks the structure the Actions
// runner requires, plus the two hygiene rules the course teaches: pin the
// action to a version, and declare the permissions the token needs.
//
// Run: bun run scripts/validate-workflow.ts <file> [more files]

import { readFileSync } from "node:fs";
import { basename } from "node:path";

interface Step { uses?: string; run?: string; name?: string; with?: unknown }
interface Job { "runs-on"?: string; steps?: Step[]; needs?: string | string[]; uses?: string; environment?: unknown }
interface Workflow { name?: string; on?: unknown; true?: unknown; jobs?: Record<string, Job> }

export function validate(file: string, text: string): { errors: string[]; warnings: string[]; jobs: string[]; steps: number } {
  const errors: string[] = [];
  const warnings: string[] = [];
  let doc: Workflow;
  try {
    doc = Bun.YAML.parse(text) as Workflow;
  } catch (err) {
    return { errors: [`not valid YAML: ${(err as Error).message}`], warnings, jobs: [], steps: 0 };
  }
  if (!doc || typeof doc !== "object") return { errors: ["workflow is not a mapping"], warnings, jobs: [], steps: 0 };

  // `on:` is the one key YAML 1.1 turns into the boolean true, so accept both.
  if ((doc.on ?? (doc as Record<string, unknown>)["true"]) === undefined) {
    errors.push("no on: trigger, so the workflow can never start");
  }
  const jobs = doc.jobs ?? {};
  const names = Object.keys(jobs);
  if (names.length === 0) errors.push("no jobs");
  if (!("permissions" in (doc as Record<string, unknown>))) {
    warnings.push("no permissions block, so the token keeps the repository default");
  }

  let steps = 0;
  for (const [name, job] of Object.entries(jobs)) {
    const reusable = typeof job.uses === "string";
    if (!reusable && !job["runs-on"]) errors.push(`job ${name} has no runs-on, so no runner can claim it`);
    if (typeof job["runs-on"] === "string" && job["runs-on"].endsWith("-latest")) {
      warnings.push(`job ${name} runs on ${job["runs-on"]}, which changes under you`);
    }
    for (const need of typeof job.needs === "string" ? [job.needs] : job.needs ?? []) {
      if (!names.includes(need)) errors.push(`job ${name} needs ${need}, which is not a job in this file`);
    }
    if (reusable) continue;
    const list = job.steps ?? [];
    if (list.length === 0) { errors.push(`job ${name} has no steps`); continue; }
    list.forEach((step, i) => {
      steps += 1;
      const where = `job ${name} step ${i + 1}`;
      if (!step.uses && !step.run) errors.push(`${where} neither runs a command nor uses an action`);
      if (step.uses && step.run) errors.push(`${where} has both uses and run`);
      if (step.uses && !step.uses.includes("@")) errors.push(`${where} uses ${step.uses} with no version, so it floats`);
    });
  }
  return { errors, warnings, jobs: names, steps };
}

if (import.meta.main) {
  const files = process.argv.slice(2);
  let bad = 0;
  for (const file of files) {
    const result = validate(file, readFileSync(file, "utf8"));
    console.log(`workflow  ${basename(file)}`);
    console.log(`jobs      ${result.jobs.length}${result.jobs.length ? ` (${result.jobs.join(", ")})` : ""}`);
    console.log(`steps     ${result.steps}`);
    for (const warning of result.warnings) console.log(`warning   ${warning}`);
    for (const error of result.errors) console.log(`error     ${error}`);
    console.log(result.errors.length === 0 ? "verdict   valid" : `verdict   invalid, ${result.errors.length} errors`);
    if (result.errors.length) bad += 1;
  }
  process.exit(bad > 0 ? 1 : 0);
}
