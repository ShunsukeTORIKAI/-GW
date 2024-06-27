import pytest
import os
import sys
print(os.path.dirname(os.path.dirname( os.path.abspath(__file__) )) )
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import src.my_library.load_dictionary2 as dictionary_loader2
d2 = dictionary_loader2.load(project_root_path + "/data/dictionary2.txt")
expected_output = -1
assert d2["あがく"] == expected_output
