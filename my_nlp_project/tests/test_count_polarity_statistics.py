import os,sys

print(os.path.dirname(os.path.dirname( os.path.abspath(__file__) )) )
project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(project_root_path)

import src.my_library.count_polarity_statistics as count_polarity_statistics

def test_count_polarity():
    dictionary1={"友達":1,"喧嘩":-1}
    dictionary2={"大好きな":1}
    input_sentence=["大好きな","友達","と","喧嘩","した"]
    expected_output=[1,0,2]
    assert count_polarity_statistics.count(dictionary1,dictionary2,input_sentence) == expected_output

def test_count_polarity_contradictory_conjunction():
    dictionary1={"ピーマン":0,"苦味":-1}
    dictionary2={"嫌いだ":-1,"良い":1}
    input_sentence=["ピーマン","は","苦味","が","強く","て","嫌いだ","けど","体に","良い"]
    expected_output=[0.2,0.1,1]
    assert count_polarity_statistics.count(dictionary1,dictionary2,input_sentence) == expected_output


def test_count_polarity_negation():
    dictionary1={"虫":0}
    dictionary2={"可愛く":1,"嫌いだ":-1}
    input_sentence=["虫","は","可愛く","ない","から","嫌いだ"]
    expected_output=[2,1,0]
    assert count_polarity_statistics.count(dictionary1,dictionary2,input_sentence) == expected_output
