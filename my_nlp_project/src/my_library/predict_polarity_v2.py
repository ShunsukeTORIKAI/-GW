def predict(PN_table):
    sum_of_classified_word = PN_table[0] + PN_table[2]    #正、負の極性を持つ語数
    sum_of_polarity = PN_table[2] - PN_table[0] #極性の和
    if sum_of_classified_word != 0:
        return sum_of_polarity / sum_of_classified_word
    else:
        return 0