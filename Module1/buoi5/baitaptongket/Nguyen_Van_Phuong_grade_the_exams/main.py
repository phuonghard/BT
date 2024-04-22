# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
  # Press Ctrl+F8 to toggle the breakpoint.
def write_class(NC):
    #direction

    DNC = r"C:\Users\phuon\Downloads\AIO-WARNUP\A\BT\Module1\buoi5\baitaptongket\data-files\Data Files"
    with open(DNC + "\\" + NC, "r+") as NC:
        NC.read()
        print("ngon")
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
                write_class(FNCT)
        else:
            write_class(FNC)
    except:
        print("bạn nhập sai lớp")
# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
