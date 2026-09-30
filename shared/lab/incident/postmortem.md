# Credential rotation outage postmortem (incident 2026-014)

**Date:** 2026-02-10

**Authors:** engineer, oncall, reviewer

**Status:** Complete, action items in progress

**Summary:** Quote search returned errors for 80 minutes after deployment
deploy-0007 rotated the database credential without rotating the copy held by
the read replica pool.

**Impact:** An estimated 214,000 search requests failed. No data was lost. The
error budget for the quarter is 71 percent spent.

## Root Causes

The deployment changed one of two copies of the database credential. The
replica pool reads its credential from a second secret that no automation
updates, so every replica connection was rejected once the old credential was
revoked. A missing integration test meant no pipeline stage exercised a
replica connection with a rotated credential.

## Trigger

Deployment deploy-0007 at 16:00 UTC, which revoked the previous credential.

## Detection

The availability alert fired on the ratio of failed search requests at 16:04.

## Resolution

The previous credential was restored, which recovered the replica pool. The
rotation was replayed at 09:20 the next morning with both secrets updated in
one change, which is deployment deploy-0008.

## Action Items

| Action item | Type | Owner | Bug |
| --- | --- | --- | --- |
| Rotate both copies in one automated change | prevent | engineer | 812 DONE |
| Test a rotated credential against a replica | prevent | oncall | 813 TODO |
| Alert when the two credential copies differ | detect | oncall | 814 TODO |
| Add the replica pool to the smoke test | mitigate | reviewer | 815 TODO |

## Lessons Learned

### What went well

The alert fired on a user visible symptom, not on a machine metric.
The rollback was one command and took four minutes.

### What went wrong

The credential existed in two places and only one was automated.
No test covered a rotated credential against a replica.

### Where we got lucky

The rotation ran during the quietest hour of the day.
The previous credential had not yet been deleted, so rollback was possible.

## Timeline

2026-02-10, all times UTC.

- 16:00 deploy-0007 reaches production and revokes the old credential
- 16:04 availability alert pages the on-call engineer
- 16:09 incident declared, on-call engineer takes incident command
- 16:31 replica connection errors identified in the logs
- 17:20 previous credential restored, errors stop
- 17:24 OUTAGE ENDS

## Supporting information

Dashboard, alert history and the chat transcript are linked in the ticket.
