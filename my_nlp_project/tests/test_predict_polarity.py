import os,sys

print(os.path.dirname(os.path.dirname( os.path.abspath(__file__) )) )
project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(project_root_path)

import src.my_library.predict_polarity as predict_polarity

def test_positive_predict():
    test_table=[1,0,2]
    expected_output=f"Positive({1/3})"
    assert predict_polarity.predict(test_table) == expected_output

def test_negative_predict():
    test_table=[5,0,2]
    expected_output=f"Negative({-3/7})"
    assert predict_polarity.predict(test_table) == expected_output

def test_neutral_predict():
    test_table=[10,10,11]
    expected_output=f"Neutral({1/21})"
    assert predict_polarity.predict(test_table) == expected_output

def test_empty_predict():
    test_table=[0,3,0]
    expected_output="Not found"
    assert predict_polarity.predict(test_table) == expected_output
