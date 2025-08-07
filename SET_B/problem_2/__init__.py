import json
import sys
import os

# sys.path.insert(0, os.path.abspath(".."))
from problem_2.candidate_code import single_number

def run():
    with open("testcases.json") as f:
        cases = json.load(f)["problem_2"]
    c=0
    for i, case in enumerate(cases):
        nums = case["input"]
        expected = case["output"]
        output = single_number(nums)
        if output!=expected:
            break
        else:
            c+=1
        # assert output == expected, f"❌ Problem 2, Test case {i+1} failed.\nExpected: {expected}\nGot: {output}"
    print(f"✅ Problem 2 passed {c} / 10 test cases.")



run()
