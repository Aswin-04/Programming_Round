import sys
import os
import io
import json
import subprocess
import os
# sys.path.insert(0, os.path.abspath(".."))
from problem_1.candidate_code import print_pattern



def run():
    with open("/home/eren/selection/round-2/Programming_Round/SET_A/hidden/testcases.json") as f:
        cases = json.load(f)["problem_1"]
    c=0
    for i, case in enumerate(cases):
        expected = case["output"]
        n = case["input"]

        buffer = io.StringIO()
        sys.stdout = buffer
        print_pattern(n)
        sys.stdout = sys.__stdout__
        output = buffer.getvalue().strip()

        if output!=expected:
            break
        else:
            c+=1
        # assert output == expected, f"❌ Problem 1, Test case {i+1} failed.\nExpected:\n{expected}\nGot:\n{output}"
    print(f"✅ Problem 1 passed {c} / 10 test cases.")

if print_pattern is not None:
  run()
