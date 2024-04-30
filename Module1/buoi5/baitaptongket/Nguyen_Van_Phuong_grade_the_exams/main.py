# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
  # Press Ctrl+F8 to toggle the breakpoint.
import re
import numpy
import math
from collections import Counter


'''
this is the function call class to process'''
def write_class(NC):
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key = list(answer_key.split(","))

    #direction
    #DNC = directionary of file
    DNC = r"C:\Users\phuon\Downloads\AIO-WARNUP\A\BT\Module1\buoi5\baitaptongket\data-files\Data Files"
    #this is
    with open(DNC + "\\" + NC, "r+") as NCT:
        #split data of the file to the list by \n
        NCT = NCT.read().split("\n")
        #FN = file name
        print("Read file:", FN)
        total_line = 0
        total_fail_line = 0
        good_line = 0
        print("---Analyze---")
        high_points = 0
        median_point = 0
        list_points = []
        list_empty_answers = []
        list_wrong_answers= []
        #task2
        for line in NCT:
            PC = line.split(",")
            PC[-1] = PC[-1].replace("\n", "")
            #good case
            if re.findall(r"\AN\d{8}$", PC[0]) and len(PC) == 26:
                good_line += 1
                value = 1
                point = 0
                while value <= len(PC)-1:
                    if PC[value] == answer_key[value-1]:
                        point +=4
                    elif PC[value] == "":
                        point +=0
                        list_empty_answers.append(value)


                    else:
                        point -=1
                        list_wrong_answers.append(value)


                    value +=1
                list_points.append(point)
                if point>80:
                    high_points +=1
            elif re.findall(r"\AN\d{8}$", PC[0]) and len(PC) != 26:
                total_fail_line += 1
                list_points.append(0)
                print("Invalid line of data: the length is invalid\n", PC)
            elif re.findall(r"\AN\d{8}$", PC[0]) == [] and len(PC) == 26:
                total_fail_line += 1
                list_points.append(0)
                print("Invalid line of data: the N# is invalid\n", PC)
            else:
                total_fail_line += 1
                list_points.append(0)
                print("Invalid line of data: the N# + the length is invalid\n", PC)
            total_line += 1
        count_empty = 0
        dic_empty = {}
        dic_wrong = {}
        list_empty_answers = Counter(list_empty_answers)
        list_wrong_answers = Counter(list_wrong_answers)
        # for empty answers
        for element, count in list_empty_answers.items():
            dic_empty[element] = count

        dic_empty = sorted(dic_empty.items(), key=lambda x: x[1], reverse=True)
        list_empty_answers = list(list_empty_answers.items())
        list_empty_answers = []

        for element, count in dic_empty:
            #print(element, count)
            if count >= dic_empty[0][1]:

                list_empty_answers.append(element)
                list_empty_answers.append(count)
                list_empty_answers.append(count/total_line)

        #for wrong answers
        for element, count in list_wrong_answers.items():
            dic_wrong[element] = count
        dic_wrong = sorted(dic_wrong.items(), key=lambda x: x[1], reverse=True)
        list_wrong_answers = list(list_wrong_answers.items())
        list_wrong_answers = []

        for element, count in dic_wrong:
            if count >= dic_wrong[0][1]:
                list_wrong_answers.append(element)
                list_wrong_answers.append(count)
                list_wrong_answers.append(count/total_line)
        #notice no error found
        if total_fail_line == 0:
            print("No error found")
        #Median
        if len(list_points)%2 == 0:
            list_points.sort()
            median_point = int(
                (list_points[(len(list_points) / 2).__ceil__()] + list_points[(len(list_points) / 2).__floor__()]) / 2)
        else:
            list_points.sort()
            median_point = list_points[len(list_points) // 2]
        print("---Report---")
        print("Total valid line of data:", total_line)
        print("Total fail line of data:", total_fail_line, "\n")
        ''' Evaluate '''
        print("Number of high points:", high_points)
        print("Mean point:", sum(list_points)/len(list_points))
        print("Highest point is:", max(list_points))
        print("Lowest point is:", min(list_points))
        print("Value range of points:", max(list_points) - min(list_points))
        print("Median of points:", median_point)
        print("Empty answers:", list_empty_answers)
        print("Wrong answers:", list_wrong_answers)
        # print("Empty answers:", str(list_empty_answers).replace("[","").replace("]","").replace(",",""))
        # print("Wrong answers:", str(list_wrong_answers).replace("[","").replace("]","").replace(",",""))

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
