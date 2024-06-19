def _analyse(value, table):
    if value == -1:
        table[0] += 1
    elif value == 0:
        table[1] += 1
    elif value == 1:
        table[2] += 1
    return table 

def count(d1, d2, sentence):
    PN_table = [0, 0, 0]
    for word in sentence:
        if word in d1:
            PN_table = _analyse(d1[word], PN_table)
        elif word in d2:
            PN_table = _analyse(d2[word], PN_table)
        else:
            pass
    return PN_table