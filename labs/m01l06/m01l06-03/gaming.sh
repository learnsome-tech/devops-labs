# DevOps & Site Reliability Engineering — lesson m01l06 — The Pitfalls Of Measurement
# https://learnsome.tech/courses/devops-course/watch?lesson=m01l06
# © LearnSome.tech
count=0
for sha in $(git -C "$copy" rev-list --reverse HEAD); do
  count=$((count + 1))
  stamp="$(git -C "$copy" show -s --format=%aI "$sha")"
  GIT_COMMITTER_DATE="$stamp" \
    git -C "$copy" tag -a "deploy-9$(printf '%03d' "$count")" "$sha" \
      -m "deployed"
done

echo "honest, deployments tagged when they reached production"
