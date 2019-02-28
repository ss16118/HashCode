def getScore(set_first, set_second):
    union_score = len(set_first.intersection(set_second))
    difference_score_first = len(set_first - set_second)
    difference_score_second = len(set_second - set_first)
    return min(union_score, difference_score_first, difference_score_second)