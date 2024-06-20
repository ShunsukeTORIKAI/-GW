def output(rawdata_arrays, result):    #rawdata_arraysはdata.txtの文字列を要素に持つリスト
    for i in range(len(rawdata_arrays)):
        sentence_str = rawdata_arrays[i]
        sentence_str += "\t" + str(result[i]) + "\n"
        with open("../logs/log.txt", "a") as f:
            f.write(sentence_str)
