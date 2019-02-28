class fileHandler:
    def read(self, fileDir):
        file = open(fileDir, 'r')
        data = [item.replace("\n", "").split(" ") for item in file.readlines()];
        del data[0]
        output = []
        i = 0
        for item in data:
            output += ((item[0], i), item[2:])
            i += 1;
        print(output)

    def write(self,listElems):
        file = open("output.txt", 'w')
        file.write(str(len(listElems)) + "\n")
        for item in listElems:
            file.write(" ".join(item) + "\n")