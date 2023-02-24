# This is a sample Python script.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputFilePath = "D:/Projects/FabdbToCardmarket/test.txt"  # sys.argv[0]
    outputFilePath = "D:/Projects/FabdbToCardmarket/result.txt"  # sys.argv[1]
    tmp = []
    with open(inputFilePath, "r+") as temp_f:
        dataFile = temp_f.readlines()
    for line in dataFile:
        tmp+=line.replace("[2]", "2x").replace("[1]", "1x").replace("(Red)", "[Red]").replace("(Blue)", "[Blue]").replace(
            "(Yellow)", "[Yellow]")
    outputFile = open(outputFilePath, "w")
    outputFile.writelines(tmp)
    outputFile.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
