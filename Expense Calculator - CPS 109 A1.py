# -*- coding: utf-8 -*-
""" 
    ~~ Assignment 1 ~~
    
    Name: Patricia Delos Santos
"""

"""
-- Program Description / Problem: --
    
Since I've started my first year this year, I've realized that there are 
many costs associated with being a university student - from food and school 
supplies to tuition. Obviously, there are many more expenses as compared 
to when I was in highschool.

So, for this assignment, I want to create a program that can help with 
tracking expenses.

I want to make a program that can:
    1. Track expenses - You can add expenses and track them
    2. Calculate total expenses - Add together all expenses
    3. Display a summary of expenses - Display a list of all expenses in a way
    that is easy to see and understand. (Extra) make it possible to sort the list
    4. Pay off expense feature (extra) - "pay off" an expense and remove it from
    the list / stop tracking it.
"""


def addexpense(mlist):   
    """
    Adds an expense to the expense masterlist.
    
    User Input
    ----------
    Expense name and expense amount
    
    Parameters
    ----------
    mlist : list
        list containing all the expenses

    Returns
    -------
    None
    """
    exp = []        #List to append to master list
    amnt = ''       #For user input
    numofdec = 0    #Counts number of decimals in user input
    valid = False   #Boolean value - if valid answer or not
    
    #Takes the name of the expense and adds it to the list exp
    exp.append(str(input("\nPlease enter the name of the expense. Enter 'CANCEL' to cancel: ")))
    exp[0] = exp[0].casefold()
    
    #checks if the name is CANCEL which is a command. 
    #If cancel, does not continue to add item. If not, asks for the amount of the exp
    if exp[0] != 'cancel':
        #Error catching, to prevent program from crashing if user input was not a number
        while(valid == False):
            numofdec = 0
            valid = True    #Sets valid to True
            
            amnt = str(input("Please enter the amount of the expense: "))
            
            #Iterates through the user input (amnt)
            for i in amnt:
                #If a '.' then add one to numofdec. Only want 1 decimal
                if i == '.':
                    numofdec += 1
                #If there are more than one '.' in the input or not a number (not including '.')
                if (numofdec > 1) or (i.isnumeric() == False and i != '.'):
                    print("\n(!) Sorry, that is not a valid expense amount. Please try again. (!)")
                    valid = False
                    break   #no need to continue iteration, invalid input
            
            #If valid input (numbers and only one '.')
            if valid == True:
                #Append float of amnt into append
                exp.append(float(amnt))
        
        #Appends the list exp containing the name and the amount of a single expense into the masterlist
        #Can edit lists within functions in python, no need to return
        mlist.append(exp)
        
        #Let user know that it has been added
        print("\n(*) Expense successfully added! (*)\n")
        
    
    
def calcexpense(mlist):
    """
    Adds all the values within the masterlist and prints the total amount of expenses

    Parameters
    ----------
    mlist : list 
        masterlist that contains the names and amounts of the expenses
        

    Returns
    -------
    None
    """
    
    #Takes the size of the list
    count = len(mlist)
    
    #If the list is not empty, continue with the calculation
    if count > 0:
        total = 0
        
        #Iterates through the mlist parameter (masterlist) and adds together
        #the second element (index=1) of each nested list (amount of expense)
        for i in mlist:
            total += i[1]
        
        print("\nNumber of different purchase(s)/expense(s): ", count)
        print("Total expenses: $", round(total, 2))
        
    #Else, the list is empty and let the user know
    else:
        print("\n(!) You do not yet have any logged expenses! (!)")
        
        


def paidexpense(mlist):
    """
    Removes a specific expense from the masterlist

    Parameters
    ----------
    masterlist : list 
        contains the names and amounts of the expenses
        

    Returns
    -------
    none
    """
    
    matches = []        #List that keeps track of matching expenses.
    temp = []           #Temporary list 
    valid_ans = []      #Keep track of valid user inputs for error catching
    
    #If the masterlist is empty, let the user know
    if len(mlist) == 0:
        print("\n(!) You do not yet have any logged expenses! (!)")
    
    #Else, continue with operation
    else:
        while(True):
            
            #Asks user to enter the name of the expense to be deleted (paid)
            name = str(input("\nPlease enter the name of the expense. Enter 'CANCEL' to cancel: "))
            
            #Casefolds (turns to lower case) the user input so that
            #it's not case sensitive
            name = name.casefold()
            
            #sets index counter to 0
            index = 0
            
            #Goes through the master list to look for matching expense names
            for i in mlist:
                
                #Sets expname to the first element in the nested list
                expname = i[0]
                
                #compares name to a casefolded expname (not case sensitive)
                #If name == expname then...
                if name == expname.casefold():
                    #Set temporary list to i (the nested list)
                    temp = i[:]
                    #Appends an index to keep track of its index in the master list
                    temp.append(index)
                    #Appends temporary list to list matches
                    matches.append(temp)
                
                #increase index counter by one
                index += 1
                
                #So each list in matches will have the format: [name, amount, index in masterlist]
            
            #If CANCEL command was entered or matching expenses were found, break
            if name == "cancel" or len(matches) != 0:
                break
            #If no expenses were found, let user know
            else:
                print("(!) Could not find expenses with the given name! (!)")
    
        #If not CANCEL (user wants to go through with action) then...
        if name != "cancel":
            
            #While true for error catching
            while(True):
                
                #Set counter to 1 (for user input and display)
                countmatch = 1
                
                #Print out the found matching statements
                print("\nThe following expenses were found with the same given name:")
                print("----------------------------------------")
                print("\n#:    Expense:                   Amount:")
                
                #Iterates through the list containing all the expenses with matching names
                for k in matches:
                    letterlen = len(k[0])
                    
                    #Simply to make it so that they line up
                    #Counts number of characters then subtracts it from a certain amount of characters
                    #To determine number of spaces to print out after name/number
                    #If number is negative (a really long name for example), python counts it as *0
                    print(countmatch," "*(4 - len(str(countmatch))), k[0]," "*(25 - letterlen), round(k[1], 2))
                    
                    #Appends the counter to valid_ans to keep track of valid user inputs
                    valid_ans.append(str(countmatch))
                    #Increases counter by 1
                    countmatch += 1
                print("----------------------------------------")
                
                #Add 'cancel' as a valid user input
                valid_ans.append("cancel")
                
                print("\nTo select an expense to remove, enter the expense number. \nEnter 'CANCEL' to cancel")
                ans = str(input("\nEnter a number or 'CANCEL': "))
                #casefold so accepts both upper and lower case
                ans = ans.casefold() 
                
                #If user input is not in list valid_ans, then invalid user input. Let user know
                if ans not in valid_ans:
                    print("\n"*5)
                    print("\n(!) Sorry, that is not a valid input, please try again... (!)")
                else:
                    break
            
            #If user did not input CANCEL and chose to go ahead with the operation
            if ans != "cancel":
                #Sets variable item to the chosen element in matches
                item = matches[int(ans)-1]
                #Sets the index to the third element (index in master list) of list item 
                index = item[2]
                #Deletes the item from the master list
                del mlist[index]
                #Let user know that item was removed
                print("\n(*) Item successfully removed (*)")
                
                
                

def summary(mlist):
    """
    Generates a more detailed expense summary

    Parameters
    ----------
    mlist : list 
        contains the names and amounts of the expenses
        

    Returns
    -------
    none
    """
    
    #Checks if master list is empty. If so, let user know, else, continue with function
    if len(mlist) == 0:
        print("\n(!) You do not yet have any logged expenses! (!)")
    else:
        print("\n"*5)
        print("----------------------------------------")
        print("     --- Your Expenses Summary ---")
        print("\nExpense:                   Amount:")
        
        letterlen = 0
        total = 0
        
        #Iterates through masterlist
        for i in mlist:
            letterlen = len(i[0])
            
            #Counts letters and subtracts it from given character amount to determine
            #number of spaces to be printed (also explained in paidexpense function)
            print(i[0]," "*(25 - letterlen), roundaddzero(i[1]))
            
            #Adds the second element of i (expense amount) to the total
            total += i[1]
        
        #print total, uses roundaddzero function
        print("\nTotal:                    ", roundaddzero(total))
        print("\n\nEnd of Summary")
        print("----------------------------------------")
        
        
        
def choices(option):
    """
    Function to help with inputs, choices and error catching

    Parameters
    ----------
    option : int
        Determines which options to give user (Depending on function)
        

    Returns
    -------
    a : str
        An answer to be returned to main
    """
    
    #If the option parameter is 1 (if the user is adding expenses)
    if option == 1:
        while(True):
            #print user options
            print("\n--------------------------")
            print("Here is what you can do : ")
            print("(1) Enter another expense")
            print("(0) Do something else (Return to main screen)")
            print("--------------------------")
            
            a = str(input("What would you like to do? (Enter a number): "))
            
            #error catching
            if a != '0' and a != '1':
                print("(!) Sorry, that is not a valid input, please try again... (!)")
            #If valid input then break out of loop and return a
            else:
                break
        
        return a
    
    #If the option parameter is 3 (if the user is removing expenses)        
    elif option == 3:
        while(True):
            print("\n--------------------------")
            print("Here is what you can do : ")
            print("(1) Remove another expense")
            print("(0) Do something else (Return to main screen)")
            print("--------------------------")
        
            a = str(input("What would you like to do? (Enter a number): "))
            
            #error catching
            if a != '0' and a != '1':
                print("(!) Sorry, that is not a valid input, please try again... (!)")
            #If valid input then break out of loop and return a
            else:
                break
        
        return a
    
    #If the option parameter is 4 (if the user is viewing the general summary)
    elif option == 4:
        print("Enter \'A\' to sort alphabetically.")
        print("Enter \'R\' to sort reverse alphabetically.")
        print("Enter \'D\' to sort numerically, from lowest to highest amount.")
        print("Enter \'U\' to sort numerically, from highest to lowest amount.")
        print("Enter anything else to return to the main screen.")
        a = str(input("\n\nWhat would you like to do?: "))
        
        #casefold so it doesn't matter whether input is caps or not
        a = a.casefold()
        
        #return an answer depending on user input
        if a == 'a':    #Return 1 if ans is a (alphabetic sort)
            return '1'
        elif a == 'r':  #Return 2 if ans is r (reverse alpha sort)
            return '2'
        elif a == 'd':  #Return 3 if ans is d (lowest to highest expense amount)
            return '3'
        elif a == 'u':  #Return 4 if ans is u (highest to lowest expense amount)
            return '4'
        else:
            return '0'  #Return 0 if anything else is entered (return to main)
        
        
        
        
        

#Used as key for sorting using built-in sort / sorted
def second(item):
    """
    Returns the second element of the list (used for sort)
    
    Parameters
    ----------
    item : list
        List from which to take second element
        

    Returns
    -------
    item[1] : int
        returns the second element of the list (expense amount)
    """
    #Returns second element of a given list
    return item[1]




def exitsequence():
    """
    Function that handles the exit sequence when the user inputs 'EXIT'
    
    Parameters
    ----------
    None
        

    Returns
    -------
    None
    """
    
    valid_ans = ['Y', 'y', 'N', 'n']    #List of valid user inputs (Y/N)
    valid = False   #Boolean - if valid user input or not
    
    while(valid == False):
        ans = str(input("\nWould you like to exit the program? (Y/N): "))
        
        #If user wished to exit the session (input == Y)
        if ans == ('Y') or ans == ('y'):
            valid == True
            print("\nYou have chosen to end the session.")
            print("Thank you for using the calculator. Have a nice day!")
            return 1    #returns True (1)
        
        #If user did not want to quit session (input == N)
        elif ans in valid_ans:
            print("You have chosen not to end the session.")
            print("Returning you to your current session...")
            return 0    #returns False (0)
        
        #Else not in valid_ans, so not valid input
        else:
            print("That is not a valid input, please try again...")
            
            
            
    
def roundaddzero(number):
    """
    Function rounds a float to 2 decimal places and adds 0 padding if needed.
    
    Parameters
    ----------
    number : float
        number to be rounded / added zeroes
        

    Returns
    -------
    stringnum : str
        rounded and zero padded number
    
    Example
    -------
    7.2 --> 7.20,
    12.783 --> 12.78
    """
    
    #List of decimal place values that need 0 padding
    endswith = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]  
    
    #Rounds float number to 2 places
    number = round(number, 2)
    
    #Mod 1 just takes the decimal place
    a = number%1
    
    #convert number to str and assign to stringnum
    stringnum = str(number)
    
    #Zero padding (7.1 --> 7.10):
    #a contains the decimal places (mod). 
    #Multiply by 100 to take first 2 decimals 
    #int to get rid of any other decimals (because 10.1 != 10)
    #Check if in endswith (endings that need padding)
    if int(a*100) in endswith:
        #concatenate 0 to the end of stringnum
        stringnum += '0'
    
    #return stringnum
    return stringnum
    


print("\n--- Welcome to the Expense Calculator ---")

masterlist = []     #Masterlist - contains all names and amounts of expenses
valid_ans = ['1', '2', '3', '4', 'exit']    #Contains all valid user inputs
end = False    #Boolean Variable - if the user decided to end the program or not

    
ans = ''   #Answer - Variable to contain user inputs

#While end is false, run program
while(end == False):
    
    #error catching
    while(True):
        ans = ''
        
        #Let user know what their options are
        print("\n--------------------------")
        print("Here is what you can do : ")
        print("(1) Enter an expense")
        print("(2) Calculate total expenses")
        print("(3) Remove a specific paid expense")
        print("(4) Generate an expense summary")
        print("(EXIT) Exit the program")
        print("--------------------------")
        
        ans = str(input("\nWhat would you like to do? (Enter a number or \'EXIT\'): "))
        ans = ans.casefold()
        
        #Checks valid_ans list if user input is in it. If not then not valid input. Let user know.
        if ans not in valid_ans:
            print("(!) Sorry, that is not a valid input, please try again... (!)")
        #Else, valid answer, continue with program
        else:
            break
    
    #While end is false (continue running program)
    while(end == False):
        
        #if input was 'exit'
        if ans == "exit":
            #call exit sequence function. Assign end the returned value
            end = exitsequence()
            break   #Break out of while loop and return to "main screen"
        
        
        #If input was 1 (add expense)
        elif ans == valid_ans[0]:
            #Allow user to continue putting inputs unless ans is 0
            while (ans != '0'):
                #call addexpense function
                addexpense(masterlist)
                #call choices function for option 1 (add expense)
                ans = choices(1)
            break   #Break out of while loop and return to "main screen"
            
        #If input was 2 (calculate expense)
        elif ans == valid_ans[1]:
            #call calcexpense function
            calcexpense(masterlist)
            #"Pause" program until user inputs something to allow user 
            #to look at the calculated expenses without returning to main right away
            ans = str(input("\nEnter anything to return to main screen: "))
            break   #Break out of while loop and return to "main screen"
        
        
        #If input was 3 (remove / pay expense)
        elif ans == valid_ans[2]:
            #Allow user to continue removing inputs unless ans is 0
            while (ans != '0'):
                #call paidexpense function
                paidexpense(masterlist)
                #if list is empty, no choices given (nothing to be removed)
                if len(masterlist) == 0:
                    temp = str(input("\nEnter anything to return to main screen: "))
                    #Set ans to 0 to break out of while loop
                    ans = '0'
                #Else, list has content, call choices function option 3
                else:
                    ans = choices(3)
            break   #Break out of while loop and return to "main screen"
        
        #If input was 4 (generate general summary)
        elif ans == valid_ans[3]:
            #set mastercopy = to masterlist (not a copy, just for variable consistency)
            mastercopy = masterlist
            while(ans != '0'):
                #call summary function with mastercopy list
                summary(mastercopy)
                
                #Checks if list is empty, if so, don't give sort options (nothing to sort!)
                if len(masterlist) == 0:
                    temp = str(input("\nEnter anything to return to main screen: "))
                    ans = '0'
                #If list has content, give sort options
                else:
                    #call choices function, option 4, and assign returned value to ans
                    ans = choices(4)
                    
                    #sorted(item, key, reverse (default = False)) 
                    #(sorted = same as sort, but does not alter original list (returns list))
                    #Using sorted so order of user input in masterlist is not affected
                    
                    #if ans is 1, then sort alphabetically
                    if ans == '1':
                        mastercopy = sorted(masterlist)
                    
                    #if ans is 2, then sort reverse alpha. Make reverse true
                    elif ans == '2':
                        mastercopy = sorted(masterlist, reverse=True)
                        
                    #if ans is 3, then sort numerically from lowest to highest
                    #In simple terms, key tells sort() what to sort in given list.
                    #Default is first item if nested list
                    #key = function, in this case, "second". Second returns the second element in a given item
                    #This allows for sorted() to sort the second item in the nested list rather than the first
                    #Needed since the amount of expense is second elem (index = 1) in each nested list
                    #Learned about keys from + referenced this source:
                    #https://www.programiz.com/python-programming/methods/list/sort
                    elif ans == '3':
                        mastercopy = sorted(masterlist, key=second)
                    
                    #if ans is 3, then sort numerically from lowest to highest
                    #key=second (explained above) and reverse is True
                    elif ans == '4':
                        mastercopy = sorted(masterlist, key=second, reverse=True) 
            
            break   #Break out of while loop and return to "main screen"
        
    #Prints a bunch of newlines to "separate" this section from the "main screen"
    print("\n"*10)