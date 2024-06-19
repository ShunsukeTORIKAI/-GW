import os
import sys
print(os.path.dirname(os.path.dirname( os.path.abspath(__file__) )) )
project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(project_root_path)

from janome.tokenizer import Tokenizer
t = Tokenizer()
with open("../data/data.txt") as f:
    for line in f:
        if line != "":
            sentence_token_list = list(t.tokenize(line, wakati = True))
            sentence_token_list = [x for x in sentence_token_list if x != "。" and x != "、"]    #"。"と"、"は極性評価に関係ないので削除
            sentence_token_string = ",".join(sentence_token_list)
            sentence_token_string += "\n"
            with open("../data/processed_data.txt", "a") as f1:
                f1.write(sentence_token_string)
        else:
            pass