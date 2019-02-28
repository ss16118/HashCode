import evaluator

# input [([Index], {Atts})]
# output [[Index]]

def makeSlideShow(listSlides):
    listSlides.sort(key=lambda x : len(x[1]))

    totalScore = 0
    finalSlides = []

    for i in range(len(listSlides) - 1):
        totalScore += evaluator.getScore(set(listSlides[i][1]), set(listSlides[i + 1][1]))
        finalSlides.append(listSlides[i][0])

    finalSlides.append(listSlides[-1][0])

    print(totalScore)

    return finalSlides