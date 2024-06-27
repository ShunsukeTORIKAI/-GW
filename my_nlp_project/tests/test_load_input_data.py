import pytest
import os
import sys
print(os.path.dirname(os.path.dirname( os.path.abspath(__file__) )) )
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import src.my_library.load_input_data as load_input_data
sentence_arrays = load_input_data.load("../data/processed_data.txt")
expected_output = ['雨', '降る', 'てる', 'から', '気分', '落ち込む', '早い', '晴れる', 'て', 'ほしい']
assert sentence_arrays[0] == expected_output
