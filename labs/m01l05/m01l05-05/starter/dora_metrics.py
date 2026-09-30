"""Compute DORA's five software delivery metrics from a real git history.

Usage: python3 dora_metrics.py <repository>

The repository is read, never written. A deployment is an annotated tag named
deploy-NNNN. A change is a commit. A deployment is judged failed when a later
commit carries the trailer Remediates: <that tag>, which is also what makes
the deployment carrying that commit unplanned, and therefore rework.
"""
