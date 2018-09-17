def finddigits(inputarray):
    for element in inputarray:
        counter = 0
        orig = element
        while int(element):
            digit = int(element) % 10
            if (int(digit) != 0.0 and (orig % digit == 0.0)):
                counter = counter + 1
            element = int(element)/10
        print (counter)

testcase = int(input())
inputarray = []
for x in range(0, testcase):
    inputele = int(input())
    inputarray.append(inputele)
finddigits(inputarray)
