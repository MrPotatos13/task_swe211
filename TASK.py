file = open("test.txt", "r")
print()
# next line will copy the txt from file to the var txt
txt = ""
for t in file:
    txt = txt + t

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
