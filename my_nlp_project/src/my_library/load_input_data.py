def load(input_path):
    sentence_arrays = []
    with open(input_path) as f:
        for line in f:
            if line != "":
                sentence_arrays.append(line.rstrip("\n").split(","))
                sentence_arrays
            else:
                pass
    return sentence_arrays