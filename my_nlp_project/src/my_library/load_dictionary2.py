def load(input_path):

    dictionary = {}
    with open(input_path) as f:
        for line in f:
            if line != "":
                array = line.split("\t") #arrayは左から評価基準・P/Nを持つリスト
                if array[0] == "ネガ（経験）" or array[0] == "ネガ（評価）":
                    array[0] = -1
                elif array[0] == "ポジ（経験）" or array[0] == "ポジ（評価）":
                    array[0] = 1
                dictionary[array[1].rstrip('\n')] = array[0]
            else:
                pass
    return dictionary