import pytest
import os
import sys
print(os.path.dirname(os.path.dirname( os.path.abspath(__file__) )) )
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import src.my_library.load_dictionary1 as dictionary_loader1
d1 = dictionary_loader1.load(project_root_path + "/data/dictionary1.txt")
expected_output = 0
assert d1["２，３日"] == expected_output