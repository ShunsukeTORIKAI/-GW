import pytest
import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import sys.my_library.load_input_data as load_input_data
sentence_arrays = load_input_data.load("../src/my_library/load_input_data.py")
expected_output = 
assert  == expected_output
