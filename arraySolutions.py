import array

mainArray = []

secondArray = []

number = int(input("Please Enter a Number "))

for i in range(number):

    name = input("Enter a Name ")
    marks = float(input("Enter a Marks "))
    data = [name, marks]
    mainArray.append(data)


for name in range(len(mainArray)):
    for name2 in range(len(mainArray):)
