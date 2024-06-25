import os
import sys
print(os.path.dirname(os.path.dirname( os.path.abspath(__file__) )) )
project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(project_root_path)

file1_array = []
file2_array = []
output_array = []
with open("../logs/log_v7.txt") as f1: #logファイルその1
    for line1 in f1:
        line1 = line1.strip("\n")
        array1 = line1.split("\t")
        file1_array.append(array1)
with open("../logs/log_v8.txt") as f2: #logファイルその2
    for line2 in f2:
        line2 = line2.strip("\n")
        array2 = line2.split("\t")
        file2_array.append(array2)
print(len(file1_array) == len(file2_array)) #２つのlogファイルの行数が等しいか？
with open("../logs/log_v7_v8_diffs.txt","a") as f: #出力ファイル
    for i in range(len(file1_array)):
        if file1_array[i] != file2_array[i]:
            string = str(i) + " " + str(file1_array[i][0]) + "\t" + str(file1_array[i][1]) + " " + str(file2_array[i][1]) +"\n"
            f.write(string)