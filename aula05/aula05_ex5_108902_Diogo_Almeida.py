def telToName(tel, telList, nameList):
    count = 0
    for i in telList:
        if i == tel:
            return nameList[count]
        else:
            count+=1
    return tel

def nameToTels(partName, telList, nameList):
    count = 0
    tels=[]
    for i in nameList:
        if partName in i:
            tels.append(telList[count])
            count +=1
        else:
            count +=1
    return tels


def main():

    telList = ['975318642', '234000111', '777888333', '911911911']
    nameList = ['Angelina', 'Brad',      'Claudia',   'Bruna']


    tel = input("Tel number? ")
    print( telToName(tel, telList, nameList) )
    print( telToName('234000111', telList, nameList) == "Brad" )
    print( telToName('222333444', telList, nameList) == "222333444" )


    name = input("Name? ")
    print( nameToTels(name, telList, nameList) )
    print( nameToTels('Clau', telList, nameList) == ['777888333'] )
    print( nameToTels('Br', telList, nameList) == ['234000111', '911911911'] )

if __name__ == "__main__":
    main()
