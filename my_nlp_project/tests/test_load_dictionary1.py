import pytest
import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import sys.my_library.load_dictionary1 as load_dictionary1
d1 = load_dictionary1.load("../src/my_library/load_dictionary1.py")
expected_output = 0
assert d2["２，３日"] == expected_output
