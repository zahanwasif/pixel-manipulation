mylist = []

myfile = open("practice.ppm", "r")
first_line = myfile.readline()
second_line = myfile.readline().split()
col = second_line[0]
row = second_line[1]
third_line = myfile.readline()
pixel_values = myfile.read().split()
x = 0
for i in range(int(second_line[1])):
    mylist.append([])
    for j in range(int(second_line[0])):
        mylist[i].append([])
        for k in range(3):
            mylist[i][j].append(pixel_values[x])
            x+=1 






nextfile = open("lol.ppm", "w")
print(first_line, file=nextfile)
print(row, col, file=nextfile)
print(third_line, file=nextfile)
for i in range(int(row)):
    for j in range(int(col)):
        for k in range(3):
            print(mylist[i][j][k], end=" ", file=nextfile)



