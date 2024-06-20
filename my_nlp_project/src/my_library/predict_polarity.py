"""極性が中性の語はsum_of_classified_wordに含まなくて良いのではという、木下さんの意見を反映してみました"""
def predict(PN_table):
    sum_of_classified_word = PN_table[0] """+ PN_table[1]""" + PN_table[2]    #極性を持つ語数
    sum_of_polarity = PN_table[2] - PN_table[0] #極性の和
    if sum_of_classified_word != 0:
        return sum_of_polarity / sum_of_classified_word
    else:
        return 0
