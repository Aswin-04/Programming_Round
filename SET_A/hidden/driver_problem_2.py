import sys
import os
import json

sys.path.insert(0, os.path.abspath(".."))
from problem_2.candidate_code import missing_number

def run():
    with open('testcases.json') as f:
        cases = json.load(f)["problem_2"]

    for i, case in enumerate(cases):
        result = missing_number(case["input"])
        expected = case["output"]

        assert result == expected, f"❌ Problem 2, Test case {i+1} failed.\nExpected: {expected}\nGot: {result}"
    print("✅ Problem 2 passed all test cases.")


if __name__ == "__main__":
    run()