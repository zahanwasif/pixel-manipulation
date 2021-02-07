#Subhan Wasif
#241575583

import os

# "negate_red" is a function which subtracts red color value with  highest number of pixel
def negate_red():
    for i in range(int(row)):
        for j in range(int(col)):
            for k in range(3):
                mylist[i][j][0] = 255 - int(mylist[i][j][0])
    return mylist
    #"return" returns mylist, and mylist can also be used outside the function using return
# function "neagte_green" subtrcts green color with highest number which is 255, 
def negate_green():
    for i in range(int(row)):
        for j in range(int(col)):
            for k in range(3):
                mylist[i][j][1] = 255 - int(mylist[i][j][1])
    return mylist
# "negate_blue" works as negate_green and negate_red but the blue value, in mylist 
def negate_blue():
    for i in range(int(row)):
        for j in range(int(col)):
            for k in range(3):
                mylist[i][j][2] = 255 - int(mylist[i][j][2])
    return mylist
# "flatten_red" is a function which sets ever red value to 0 in list, if user wants to put all the red
#  to 0, he would select "just the reds" in options 
def flatten_red():
    for i in range(int(row)):
        for j in range(int(col)):
            mylist[i][j][0] = 0
    return mylist
#"flatten_green" put all the green values to 0 in 3d list
def flatten_green():
    for i in range(int(row)):
        for j in range(int(col)):
            mylist[i][j][1] = 0
    return mylist
# "flatten_blue" does the same work as "flatten_green" and "flatten_red" with with blue values 
def flatten_blue():
    for i in range(int(row)):
        for j in range(int(col)):
            mylist[i][j][2] = 0
    return mylist
#"grey_scale"  sets each pixel value to the average of the three
def grey_scale():
    for i in range(int(row)):
        for j in range(int(col)):
            #"total" is a variable used to store the added value of pixels
            total = 0
            total += int(mylist[i][j][0])
            total += int(mylist[i][j][1])
            total += int(mylist[i][j][2]) 
            total = total/3 
            for k in range(3):
                mylist[i][j][k] = int(total)
    return mylist
# "flip_horizontal"  that flips each row horizontally
def flip_horizontal():
    for i in range(int(row)):
        mylist[i].reverse()
    return mylist


def extreme_contrast():
    for i in range(row):
        for j in range(col):
            for k in range(3):
                if mylist[i][j][k] >= 127:
                    mylist[i][j][k] = 255
                elif mylist[i][j][k] <= 127:
                    mylist[i][j][k] = 0








            
#mylist is 3d array we use to store pixel values
mylist = []
file = input("Enter name of image file:")
next_file = input("Enter name of output file:")
# file and next_file are the input and output files respectivily. User enters these files to store pixel values to
# to specific files
myfile = open(file, "r")
# myfile is a varibale er used to open the given file
first_line = myfile.readline()
# variable "first_line" is used to read and store the first line of given file
second_line = myfile.readline().split()
# "second_line" is col-row line. first number is  colmun and second number is row 
col = second_line[0]
row = second_line[1]
third_line = myfile.readline()
#thirt line of a ppm is always the maximum number of pixel value
pixel_values = myfile.read().split()
#"pixel_values" is a list we made for pixel values 
x = 0
#to make a 3d list and to store the pixel values in it, we make a loop for number of rows and inside that list
#we make number of colmuns which makes it 2d list. and then we make a list in every list of colmun of every
#and store RGB values in it and its called a 3d list 
for i in range(int(row)):
    mylist.append([])
    for j in range(int(col)):
        mylist[i].append([])
        for k in range(3):
            mylist[i][j].append(pixel_values[x])
            x+=1




while True:

    #these are 8 options given to user to do different things 
    print("Here are your choices:")
    print("[0] exit")
    print("[1] convert to greyscale")
    print("[2] flip horizontally")
    print("[3] negative of red")
    print("[4] negative of green")
    print("[5] negative of blue")
    print("[6] just the reds")
    print("[7] just the greens")
    print("[8] just the blues")
    choice = int(input("Enter choice:"))
    # "choice", variable for the input to user to do function above
    if choice == 0:
        print("Bye Bye")
        break
        # "exit" ends the program
    elif choice == 1:
        grey_scale()
    elif choice == 2:
        flip_horizontal()
    elif choice == 3:
        negate_red()
    elif choice == 4:
        negate_green()
    elif choice == 5:
        negate_blue()
    elif choice == 6:
        flatten_red()
    elif choice == 7:
        flatten_green()
    elif choice == 8:
        flatten_blue()
    # these options just call the functions user wants to do

    
    nextfile = open(next_file, "w")
    #"nextfile" opens the file on which we write pixel values
    #"next_file" is a input that will store give file name 
    print(first_line, file=nextfile)
    print(col, row,file=nextfile)
    print(third_line, file=nextfile)
    # for loop writes every single in given file
    for i in range(int(row)):
        for j in range(int(col)):
            print(mylist[i][j][0],mylist[i][j][1],mylist[i][j][2], file= nextfile)
            
        
    

    #"option" input which asks user if wants to do more operations
    option = input("Do you want to do more operations (y or n):")
    if option == "n":
        # "n" means no and this will take program to end
        print("Bye Bye")
        break
    elif option == "y":
        input_file = input("Do you want to change input file (y or n):")
        output_file = input("Do you want to change output file (y or n):")
        # here user also can change input file or outfile 
        if input_file == "y":
            #if user changes the file, this code will again read it and make it a list
            file = input("Enter name of input file:")
            myfile = open(file, "r")
            first_line = myfile.readline()
            second_line = myfile.readline().split()
            col = second_line[0]
            row = second_line[1]
            third_line = myfile.readline()
            pixel_values = myfile.read().split()
            x = 0
            # this makes a 3d aray of pixels values
            for i in range(int(row)):
                mylist.append([])
                for j in range(int(col)):
                    mylist[i].append([])
                    for k in range(3):
                        mylist[i][j].append(pixel_values[x])
                        x+=1

        if output_file == "y":
            next_file = input("Enter name of output file:")




# to close the opened file, close function is used
# this will close the both files given by user
myfile.close()
nextfile.close()
os.system("pause");