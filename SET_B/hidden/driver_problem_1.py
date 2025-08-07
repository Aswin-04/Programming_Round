import sys
import os
import io
import json

sys.path.insert(0, os.path.abspath(".."))
from problem_1.candidate_code import print_number_pattern

def run():
    with open("testcases.json") as f:
        cases = json.load(f)["problem_1"]

    for i, case in enumerate(cases):
        expected = case["output"]
        n = case["input"]

        buffer = io.StringIO()
        sys.stdout = buffer
        print_number_pattern(n)
        sys.stdout = sys.__stdout__
        output = buffer.getvalue().strip()

        assert output == expected, f"❌ Problem 1, Test case {i+1} failed.\nExpected:\n{expected}\nGot:\n{output}"
    print("✅ Problem 1 passed all test cases.")

if __name__ == "__main__":
    run()
