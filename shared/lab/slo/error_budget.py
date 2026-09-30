"""Turn a service level objective into an error budget, and burn it.

Usage: python3 error_budget.py
No arguments: the numbers below are the worked example the lesson shows.
"""
TARGET = 0.999          # the objective: 99.9 percent of requests succeed
WINDOW_DAYS = 30        # the window the objective is measured over
REQUESTS = 2_000_000    # requests expected in the whole window
FAILED = 1_430          # failed requests so far
ELAPSED_DAYS = 10       # how far into the window we are

budget = REQUESTS * (1 - TARGET)
spent = FAILED / budget
elapsed = ELAPSED_DAYS / WINDOW_DAYS
burn = spent / elapsed
per_day = FAILED / ELAPSED_DAYS
remaining = (budget - FAILED) / per_day

print(f"objective                 {TARGET * 100:.1f} percent"
      f" over {WINDOW_DAYS} days")
print(f"error budget              {budget:,.0f} failed requests")
print(f"budget spent              {FAILED:,} requests,"
      f" {spent * 100:.1f} percent")
print(f"window elapsed            {elapsed * 100:.1f} percent")
print(f"burn rate                 {burn:.2f} times the sustainable rate")
print(f"budget exhausted in       {remaining:.1f} days")
verdict = "freeze and fix" if burn > 1 else "keep shipping"
print(f"verdict                   {verdict}")
