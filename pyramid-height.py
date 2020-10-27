blocks = int(input("Enter the number of blocks: "))
used = 0
for i in range(1,blocks):
    height = i
    used = used + i
    i = i+1
    if (blocks - used < i):
        break

print("The height of the pyramid:", height)