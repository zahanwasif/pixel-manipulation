import os
mylist = []


file = input("Enter name of image file:")
next_file = input("Enter name of output file:")
myfile = open(file, "r")
data = myfile.readline()
data2 = myfile.readline().split()
data3 = myfile.readline()
data4 = myfile.read().split()
col = data2[0]
row = data2[1]
x = 0
for i in range(int(data2[0])):
    mylist.append([])
    for j in range(int(data2[1])):
        mylist[i].append([])
        for k in range(3):
            mylist[i][j].append(data4[x])
            x+=1  




def extreme_contrast():
    for i in range(int(row)):
        for j in range(int(col)):
            if int(mylist[i][j][0]) >= 127:
                mylist[i][j][k] = 255
            elif int(mylist[i][j][0]) <= 127:
                mylist[i][j][k] = 0
    print(mylist)
extreme_contrast()