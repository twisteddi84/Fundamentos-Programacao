
# This program generates 20 terms of a sequence by a recurrence relation.
Un = 100                    # Un = each term of the sequence. Initially = U0
n=0
count=0
while Un>0:
    n += 1
    count += 1
    count = str(count)
    print("{} : {}.".format("Un"+count, Un))
    Un = 1.01*Un - 1.01
    count = int(count)
print("Número total de termos: {}.".format(n))