s = input("Caracter e numero:")
s.lower()
m= []
while True:
    for i in s:
        m.append(i)
    break

if "1" in m or "9" in m:
    if "a" in m or "h" in m:
        print("Corner")
    else:
        print("Border")
elif "a" in m or "h" in m:
    print("Border")
else:
    print("Inside")