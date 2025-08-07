import sys
import os
import json

sys.path.insert(0, os.path.abspath(".."))
from problem_3.candidate_code import min_operations_to_equal_strings

def run():
    with open('testcases.json') as f:
        cases = json.load(f)["problem_3"]

    for i, case in enumerate(cases):
        result = min_operations_to_equal_strings(*case["input"])
        expected = case["output"]

        assert result == expected, f"❌ Problem 3, Test case {i+1} failed.\nExpected: {expected}\nGot: {result}"
    print("✅ Problem 3 passed all test cases.")

if __name__ == "__main__":
    run()