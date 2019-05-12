# ************************************
# Title: Interactive To Do List
# Dev: CWright
# Desc:
# Date: May 11, 2019
# Changelog: (who, what, when)
# CWright, 4/26/2019, created script
# ************************************

# Step 0 - Create a text file and write data to it
txtFile = open("ToDo.txt", "w")

line1 = "Clean House,low" + "\n"
line2 = "Pay Bills,high"

txtFile.write(line1)
txtFile.write(line2)
txtFile.close()

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"

objFile = open("ToDo.txt", "r")
strData = objFile.read()
lstTable = []
for line in strData.splitlines():
    stringValues = line.split(",")
    dicRow = {"Task":stringValues[0], "Priority":stringValues[1]}
    lstTable.append(dicRow)
objFile.close()
for dicRow in lstTable:
    print("Task:", dicRow["Task"] + ",","Priority:", dicRow["Priority"])


# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print("\n----- The current items in the To Do list are: ------")
        for dicRow in lstTable:
            print("Task:", dicRow["Task"] + ",", "Priority:", dicRow["Priority"])
        print("---------------------------------------------------")

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newTask = input("Please enter a task: ")
        newPriority = input("Please enter the task's priority? (low, medium, or high): ")
        dicRowNew = {"Task": newTask, "Priority": newPriority}
        lstTable.append(dicRowNew)
        print("\n-----",newTask, "added to table. -----")

        print("\n----- The current items in the To Do list are: ------")
        for dicRow in lstTable:
            print("Task:", dicRow["Task"] + ",", "Priority:", dicRow["Priority"])
        print("---------------------------------------------------")
        continue

    # Step 5 - Remove an existing item from the list/Table
    elif (strChoice == '3'):
        task = input("Which task would you like to remove? (Case Sensitive): ")
        for dicRow in lstTable:
            if task == dicRow["Task"]:
                lstTable.remove(dicRow)
                print("\n----- Okay, I deleted", task, "-----")
            else:
                print("\n----- Task does not exist in table. Please try again. -----")
            break
        print("\n----- The current items in the To Do list are: ------")
        for dicRow in lstTable:
            print("Task:", dicRow["Task"] + ",", "Priority:", dicRow["Priority"])
        print("---------------------------------------------------")
        continue

    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        objFile = open('ToDo.txt', 'w')
        for dicRow in lstTable:
            #objFile.write(dicRow["Task"], dicRow["Priority"])
            #"Task:", dicRow["Task"] + ",", "Priority:", dicRow["Priority"])
            objFile.write("Task: " + dicRow["Task"] + ", " + "Priority: " + dicRow["Priority"] + "\n")
            #objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        print("\n----- Data Saved to File. Have a Great Day! -----")
        print("---------------------------------------------------")
        continue

    # Step 7 - Exit program
    elif (strChoice == '5'):
        print("\n----- Goodbye. Have a Great Day! -----")
        break  # and Exit the program
