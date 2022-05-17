# open a file: filevar = open("<filename>, '<mode>') mode = r w a
# open a fo;e om a path: file

# write a string to a file: <filevar>.write(<var> + "/n"


def while_loop_read():
    infile = open('names.txt')
    name = infile.readline()
    while name != '':
        print(name)
        name = infile.readline()

    infile.close()


while_loop_read()


def write_new_file():
    outFile = open('test.txt', 'w')
    for n in range(0, 100, 10):
        outFile.write(format(n, '3d') + '\n')
        print(outFile)

    outFile.close()


write_new_file()
