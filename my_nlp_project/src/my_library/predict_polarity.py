def predict(PN_table):
    sum_of_classified_word = PN_table[0] + PN_table[2]    #正、負の極性を持つ語数
    sum_of_polarity = PN_table[2] - PN_table[0] #極性の和
    if sum_of_classified_word != 0:
        score_of_polarity = sum_of_polarity / sum_of_classified_word
        if 0.2 < score_of_polarity <= 1.0:
            return f"Positive({score_of_polarity})"
        elif -1.0 <= score_of_polarity < -0.2:
            return f"Negative({score_of_polarity})"
        else:
            return f"Neutral({score_of_polarity})"
    else:
        return "Not found"