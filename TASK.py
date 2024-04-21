import os
print()
x=input("Please enter the file name or path\n")
if ( os.path.isfile(x)):

    file = open(x, "r")
    # next line will copy the txt from file to the var txt
    txt = file.read()

    print("The file content before sorting:")
    print(txt)
    print()

    list = []
    list = txt.split(" ")
    # it will sepreate each word
    number = []
    word = []
    # check if the word is number or alphabit
    for x in list:
        if x.isdigit():
         number.append(x)
        elif x.isalpha():
         word.append(x)
    print("After sorting:")
    print()
    print("Number list: "+str(number))
    print()
    print("Word list: "+str(word))
else:
    print("\033[91m{}\033[00m".format("There is no file or path exists has name "+x))
