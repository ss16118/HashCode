def read(fileDir):
    file = open(fileDir, 'r')
    data = [item.replace("\n", "").split(" ") for item in file.readlines()];
    del data[0]
    output = []
    i = 0
    for item in data:
        output.append([(item[0], i), item[2:]])
        i += 1;
    return output

def write(listElems, name):
    file = open(name, 'w')
    file.write(str(len(listElems)) + "\n")
    for item in listElems:
        file.write(" ".join(list(map(str, item))) + "\n")
