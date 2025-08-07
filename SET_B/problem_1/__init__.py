import sys
import os
import io
import json

# sys.path.insert(0, os.path.abspath(".."))
from problem_1.candidate_code import print_number_pattern

def run():
    with open("testcases.json") as f:
        cases = json.load(f)["problem_1"]
    c=0
    for i, case in enumerate(cases):
        expected = case["output"]
        n = case["input"]

        buffer = io.StringIO()
        sys.stdout = buffer
        print_number_pattern(n)
        sys.stdout = sys.__stdout__
        output = buffer.getvalue().strip()
        if output!=expected:
            break
        else:
            c+=1
        # assert output == expected, f"❌ Problem 1, Test case {i+1} failed.\nExpected:\n{expected}\nGot:\n{output}"
    print(f"✅ Problem 1 passed {c} / 10 test cases.")


run()
