def output(sentence_arrays, result):
    for i in range(len(sentence_arrays)):
        sentence_str = str()
        for word in sentence_arrays[i]:
            sentence_str += word
        sentence_str += "\t" + str(result[i]) + "\n"
        with open("../logs/log.txt", "a") as f:
            f.write(sentence_str)
