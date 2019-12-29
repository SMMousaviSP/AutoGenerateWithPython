HELVETICA_MEDIUM = '\\helveticaMedium'
HELVETICA_LIGHT = '\\helveticaLight'

def create_latex(sourceAddress, outputAddress):
    try:
        sourceFile = open(sourceAddress, 'r')
    except IOError:
        print("Can't open source file")
        return
    try:
        outputFile = open(outputAddress, 'a')
    except IOError:
        print("Can't open output file")
        return

    sourceContent = [x.strip() for x in sourceFile.read().split('\n')]
    if sourceContent[-1] == '':
        sourceContent.pop()

    flag = True
    for s in sourceContent:
        if s == '' or s == '\n':
            continue
        if s[-1] == ':':
            if s[-2] == ':':
                outputFile.write("%%%%%%%%%%%%%%%%%%%%%%%% {} %%%%%%%%%%%%%%%%%%%%%%%%\n".format(s[:-1]))
                outputFile.write("\\newline\n")
                outputFile.write("\\colorbox{black}{\\textcolor{white}{" + "\\helveticaMedium {}".format(s[:-1]) + "}}\n")
            else:
                flag = False
                outputFile.write("\\newline\n")
                outputFile.write("{" + "\\helveticaMedium {}".format(s) + "}\n")
        else:
            if flag: outputFile.write("\\linebreak\n")
            else: flag = True
            outputFile.write("{" + "\\helveticaLight {}".format(s) + "}\n")

    outputFile.close()
    sourceFile.close()


create_latex("readTest.txt", "writeTest.txt")
