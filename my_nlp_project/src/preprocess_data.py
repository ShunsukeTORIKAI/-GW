import os
import sys
print(os.path.dirname(os.path.dirname( os.path.abspath(__file__) )) )
project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(project_root_path)

from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
t = Tokenizer()
token_filters = [CompoundNounFilter(), POSStopFilter(['記号','助詞']), LowerCaseFilter()]
a = Analyzer(tokenizer=t, token_filters=token_filters)
with open("../data/data.txt") as f:
    for line in f:
        if line != "":
            sentence_token_list = []
            for token in a.analyze(line):
                token_list = str(token).split()
                token_list[1] = token_list[1].rstrip("'").split(",")
                if token_list[1][0] == "動詞":
                    token_list[0] = token_list[1][6]
                else:
                    pass
                sentence_token_list.append(token_list[0])
            sentence_token_string = ",".join(sentence_token_list)
            sentence_token_string += "\n"
            with open("../data/processed_data.txt", "a") as f1:
                f1.write(sentence_token_string)
        else:
            pass