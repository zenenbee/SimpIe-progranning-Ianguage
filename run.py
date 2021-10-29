import sys
"""Pain Programming Language"""

input = str(sys.argv[1])

try :
    with open(input,'r') as f:
        COD = f.readlines()
except :
    print("No such file or directory " + input)
    exit()

COD = ''.join(COD)
COD = COD.replace('\n','')
COD = COD.replace(' ','')
PART = 0

clen = len(COD)

hexstack = []

inputt = ""
inputpart = -1

def use(part):
    """Main function"""
    global COD
    global hexstack
    global dummystack
    global clen
    global inputt
    global inputpart

    code = COD[part] + COD[part+1] #if you get a error here, its usually due to f0
    value = COD[part+2] + COD[part+3]

    if code == "00":
        hexstack += [chr(int(value, 16))]
    if code == "01":
        print(''.join(hexstack))
    if code == "02":
        hexstack = ""
    if code == "03":

        if int(value, 16) > len(hexstack)-1:
            hexstack.insert(0, hexstack.pop(len(hexstack)-1))
        else:
            hexstack.insert(len(hexstack)-int(value, 16)-1, hexstack.pop(len(hexstack)-1))

    if code == "04":
        hexstack.pop(len(hexstack)-1)

    if code == "05":
        value = str(input(""))
        hexstack += value

    if code == "06":
        temp = hexstack[len(hexstack)-2]
        hexstack[len(hexstack)-2] = hexstack[len(hexstack)-1]
        hexstack[len(hexstack)-1] = temp

    if code == "07":
        temp = chr(ord(hexstack[len(hexstack)-1]) + ord(hexstack[len(hexstack)-2]))
        hexstack.pop(len(hexstack)-1)
        hexstack.pop(len(hexstack)-1)
        hexstack += temp

    if code == "08":
        temp = chr(ord(hexstack[len(hexstack)-2]) - ord(hexstack[len(hexstack)-1]))
        hexstack.pop(len(hexstack)-1)
        hexstack.pop(len(hexstack)-1)
        hexstack += temp

    if code == "09":

        hexstack += hexstack[len(hexstack)-1]


    if code == "10":
        if ord(hexstack[len(hexstack)-1]) != 0:
            part -= int(value, 16) * 4


    if code == "f0":
        COD = ""

    if code == "f1":
        pass

    return part


while PART < clen:
    PART = use(PART)
    PART += 4