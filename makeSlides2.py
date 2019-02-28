def makeSlide(listElem):

    listVertical = []
    listSlides = []
    for item in listElem:
        if item[0][0] == "H":
            listSlides.append(([item[0][1]], item[1]))
        elif item[0][0] == "V":
            listVertical.append((item[0][1], item[1]))

    while len(listVertical) > 1:
        start = listVertical[0]
        end = listVertical[-1]

        del listVertical[0]
        del listVertical[-1]

        listSlides.append(([start[0], end[0]], set(start[1] + end[1])))

    return listSlides