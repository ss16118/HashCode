def makeslide(data):
    out = []
    for i in range(len(data)):
        if data[i][0][0] == "H":
            out.append(([data[i][0][1]], set(data[i][1])))
            data[i] = ((-1, -1), {})
    for j in range(len(data)):
        min1 = 99999
        other = -1
        if data[j] != ((-1, -1), {}):
            for k in range(j + 1, len(data)):
                if data[k] != ((-1, -1), {}) and len(set(data[j][1]).intersection(set(data[k][1]))) < min1:
                    min1 = len(set(data[j][1]).intersection(set(data[k][1])))
                    other = k
                if min1 == 0:
                    break

        if other != -1:
            out.append(((list(set([data[j][0][1], data[other][0][1]]))), (set(data[j][1] + data[other][1]))))
            data[k] = ((-1, -1), {})
            data[j] = ((-1, -1), {})
    return out