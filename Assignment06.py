# ************************************
# Title: ToDo list with Functions
# Dev: CWright
# Desc: create a new script that manages a "ToDo list." This project is like to the last one,
# but different enough to be a challenge. this time you will place the code you created
# for working with your ToDo.txt file into Functions and a Class.
# Date: May 25, 2019
# Changelog: (who, what, when)
# CWright, 5/25/2019, completed script
# ************************************

#-- Data --#
objFileName = "ToDo.txt"
lstTable = []
strData = ""
dicRow = {}

#-- Input/Output --#
class IO:
    @staticmethod
    def InputMenuOptions():
        ''' Input - asks which menu option user wants to choose '''
        strChoice = input("Which option would you like to perform? [1 to 4] - ")
        #print()  # adding a new line
        return strChoice

    @staticmethod
    def InputAddNewTask():
        ''' Input - asks user what new item to add to the list/table '''
        newTask = input("Please enter a task: ")
        newPriority = input("Please enter the task's priority? (low, medium, or high): ")
        #dicRowNew = {"Task": newTask, "Priority": newPriority}
        #lstTable.append(dicRowNew)
        return newTask, newPriority

    @staticmethod
    def InputDelExistingTask():
        ''' Input - asks user which existing list/table item to delete '''
        taskToRemove = input("Which task would you like to remove? (Case Sensitive): ")
        return taskToRemove

    @staticmethod
    def OutputMenuOptions():
        ''' Output - displays a menu of choices to the user '''
        print("---------------------------------------------------")
        print("""
        ** Menu of Options **
        1) Show current data
        2) Add a new item
        3) Remove an existing item
        4) Save Data to File
        5) Exit Program
        """)
        print("---------------------------------------------------")

    @staticmethod
    def OutputDisplayCurrentTasks(lstTable):
        ''' Output - shows the current items in the list/table '''
        print("\n----- The current items in the To Do list are: ------")
        for dicRow in lstTable:
            print("Task:", dicRow["Task"] + ",", "Priority:", dicRow["Priority"])
        print("---------------------------------------------------")

    @staticmethod
    def OutputAddNewTask(newTask):
        ''' Output - displays a message to the user that item was added to table/list'''
        print("\n*****", newTask, "added to table. *****")

    @staticmethod
    def OutputDelExistingTask(blnItemRemoved):
        ''' Output - displays a message to the user that item was deleted from table/list '''
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        print("---------------------------------------------------")

    @staticmethod
    def OutputSaveData():
        ''' Output - displays a message to the user that the data has been saved '''
        print("\n***** Data Saved to File. Have a Great Day! *****")
        print("---------------------------------------------------")

    @staticmethod
    def OutputExitProgram():
        ''' Output - displays a goodbye message to the user '''
        print("\n***** Goodbye. Have a Great Day! *****")
        print("---------------------------------------------------")

#-- Processing --#
class ProcessData:
    @staticmethod
    def LoadFileData (objFileName, lstTable):
        '''loads existing data from a ToDo.txt text file into a Python dictionary'''
        objFile = open(objFileName, "r")
        strData = objFile.read()
        for line in strData.splitlines():
            stringValues = line.split(",")
            #dicRow = {"Task": stringValues[0].strip(), "Priority": stringValues[1].strip()}
            dicRow = {"Task": stringValues[0], "Priority": stringValues[1]}
            lstTable.append(dicRow)
        objFile.close()
        print("\n***** The current items in the To Do list are: *****")
        for dicRow in lstTable:
            print("Task:", dicRow["Task"] + ",", "Priority:", dicRow["Priority"])
        return lstTable

    @staticmethod
    def AddTask (newTask, newPriority, lstTable):
        ''' adds task to the list/table'''
        dicRow = {"Task": newTask, "Priority": newPriority}
        lstTable.append(dicRow)

    @staticmethod
    def DelTask (taskToRemove, lstTable):
        ''' deletes task from the list/table'''
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        while (intRowNumber < len(lstTable)):
            if (taskToRemove == str(list(dict(lstTable[intRowNumber]).values())[0])):  # the values function creates a list!
                del lstTable[intRowNumber]  # Add Error handling!
                blnItemRemoved = True
            # end if
            intRowNumber += 1
        # end for loop
        return blnItemRemoved

    @staticmethod
    def WriteData(objectFileName, lstTable):
        ''' writes the existing data to ToDo.txt '''
        objFile = open(objectFileName, "r")
        objFile = open('ToDo.txt', 'w')
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + ", " + dicRow["Priority"] + "\n")
        objFile.close()


# End class

#-- Main --#
# Step 1 - Load data from a file
# When the program starts, load each "row" of data
# in "ToDo.txt" into a python Dictionary.
# Add the each dictionary "row" to a python list "table"

ProcessData.LoadFileData(objFileName, lstTable)

while(True):
# Step 2 - Display a menu of choices to the user
    IO.OutputMenuOptions()
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))

# Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        IO.OutputDisplayCurrentTasks(lstTable)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newTask, newPriority = IO.InputAddNewTask()
        ProcessData.AddTask(newTask, newPriority, lstTable)
        IO.OutputAddNewTask(newTask)
        continue

    # Step 5 - Remove an existing item from the list/Table
    elif (strChoice == '3'):
        taskToRemove = IO.InputDelExistingTask()
        blnItemRemoved = ProcessData.DelTask(taskToRemove, lstTable)
        IO.OutputDelExistingTask(blnItemRemoved)
        continue

    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        ProcessData.WriteData(objFileName,lstTable)
        IO.OutputSaveData()
        continue

    # Step 7 - Exit program
    elif (strChoice == '5'):
        IO.OutputExitProgram()
        break # exit the program without writing to ToDo list





