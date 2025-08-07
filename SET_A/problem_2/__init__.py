import sys
import os
import json

# sys.path.insert(0, os.path.abspath(".."))
from problem_2.candidate_code import missing_number

def run():
    with open('/home/eren/selection/round-2/Programming_Round/SET_A/hidden/testcases.json') as f:
        cases = json.load(f)["problem_2"]
    c=0
    for i, case in enumerate(cases):
        result = missing_number(case["input"])
        expected = case["output"]

        if result!=expected:
            break
        else:
            c+=1
        # assert result == expected, f"❌ Problem 2, Test case {i+1} failed.\nExpected: {expected}\nGot: {result}"
    print(f"✅ Problem 2 passed {c} / 10 test cases.")


if missing_number is not None:
  run()