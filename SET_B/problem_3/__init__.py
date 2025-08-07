import json
import sys
import os

# sys.path.insert(0, os.path.abspath(".."))
from problem_3.candidate_code import length_of_longest_substring

def run():
    with open("testcases.json") as f:
        cases = json.load(f)["problem_3"]
    c=0
    for i, case in enumerate(cases):
        s = case["input"]
        expected = case["output"]
        output = length_of_longest_substring(s)

        if output!=expected:
            break
        else:
            c+=1
        # assert output == expected, f"❌ Problem 3, Test case {i+1} failed.\nExpected: {expected}\nGot: {output}"
    print("✅ Problem 3 passed all test cases.")
    


run()
