import sys
import os
import json

# sys.path.insert(0, os.path.abspath(".."))
from problem_3.candidate_code import min_operations_to_equal_strings

def run():
    with open('/home/eren/selection/round-2/Programming_Round/SET_A/hidden/testcases.json') as f:
        cases = json.load(f)["problem_3"]
    c=0
    for i, case in enumerate(cases):
        result = min_operations_to_equal_strings(*case["input"])
        expected = case["output"]
        if result!=expected:
            break
        else:
            c+=1
        # assert result == expected, f"❌ Problem 3, Test case {i+1} failed.\nExpected: {expected}\nGot: {result}"
    print(f"✅ Problem 3 passed {c} / 10 test cases.")

if min_operations_to_equal_strings is not None:
  run()
