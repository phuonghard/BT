# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
  # Press Ctrl+F8 to toggle the breakpoint.
import re
import numpy

'''
this is the function call class to process'''
def write_class(NC):
    #direction
    #DNC = directionary of file
    DNC = r"C:\Users\phuon\Downloads\AIO-WARNUP\A\BT\Module1\buoi5\baitaptongket\data-files\Data Files"
    #this is 
    with open(DNC + "\\" + NC, "r+") as NCT:
        NCT1=NCT.read().split("\n")
        NCT.read()
        print("Read file:",FN)

        total_line = 0
        total_fail_line = 0
        good_line = 0
        print("---Analyze---")

        for line in NCT1:


            PC = line.split(",")
            PC[-1] = PC[-1].replace("\n", "")
            # print(re.findall(r"\AN\d{8}", PC[0]), line)

            if re.findall(r"\AN\d{8}$", PC[0]) and len(PC) == 26:
                good_line += 1
            elif re.findall(r"\AN\d{8}$", PC[0]) and len(PC) != 26:
                total_fail_line += 1
                print("Invalid line of data: the length is invalid\n", PC)
            elif re.findall(r"\AN\d{8}$", PC[0]) == [] and len(PC) == 26:
                total_fail_line += 1
                print("Invalid line of data: the N# is invalid\n", PC)
            else:
                total_fail_line += 1
                print("Invalid line of data: the N# + the length is invalid\n", PC)

            # print(NCT1.readline().split(",")[0])
            total_line += 1

        if total_fail_line == 0:
            print("No error found")
        print("---Report---")
        print("Total valid line of data:", total_line)
        print("Total fail line of data:", total_fail_line, "\n")

    #print(NC)
    return NC
FNC = 0
while(FNC!="end"):
    FNC = input("Your class is:")

    try:
        if FNC == "allclass":

            i = 0
            for i in range(1, 9):
                FNCT = "class" + str(i) + ".txt"
                FN = FNCT
                write_class(FNCT)

        else:
            FN = FNC
            write_class(FNC+".txt")
    except:
        if FNC == "end":
            print("")
        else:
            print("Bạn nhập sai lớp, vui lòng nhập lại tên lớp")

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
