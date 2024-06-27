import pytest
import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import sys.my_library.load_dictionary2 as load_dictionary2
d2 = load_dictionary2.load("../src/my_library/load_dictionary2.py")
expected_output = 1
assert d2["あがく"] == expected_output
