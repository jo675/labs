f = open("input", "r")

l = [int(x.strip()) for x in f]

count = 0
for i in range(len(l)-1):
    if l[i+1] > l[i]:
        count+=1

print(count)
#count=1681


