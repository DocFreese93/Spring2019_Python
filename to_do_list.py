# -*- coding: utf-8 -*-
"""
- Function: Option Selection
    - Prompt user to enter a number to select an option
        - Validate user input (input must be numeric values between 1 and 5)
        - Display Error message if input is invalid and prompt user until valid input is provided
            - Option 1: view current to do list items
            - Option 2: view finished items
            - Option 3: add item to to do list
            - Option 4: Move item to completed list
            - Option 5: Exit application

"""

# Declare variables
to_do_list = []
completed_list = []

import sys

def main():
    
    # Call method to display options
    option_selection()

def option_selection():
    
    # Display choices for user to select from
    print('1) View current items on To Do List')
    print('2) View completed items from To Do List')
    print('3) Add item(s) to To Do List')
    print('4) Mark item from To Do List as accomplished')
    print('5) End Appliction (List will not be saved upon exit)')
    print('\nSelect one of the above options: ')
    
    # Declare variable and assign the value of the user's selection
    option = int(input())
    
    # Validate input
    while option < 1 or option > 5:
        
        # Display error message and prompt user to enter valid input
        # withi numerical boundaries
        print('\nInvalid input. Enter a number between 1 and 5: ')
        option = int(input())
        print()
    
    # Determine option the user has selected and direct user to 
    # desired selection
    if option == 1:
        view_todo_list(to_do_list)
    elif option == 2:
        view_completed_list(completed_list)
    elif option == 3:
        add_todo_list(to_do_list)
    elif option == 4:
        complete_item(to_do_list, completed_list)
    elif option == 5:
        end_program()
        
# This function displays the items within the To Do List
# Argument(s): to do list
def view_todo_list(todo_list):
    
    # Initialize task number
    task_count = 1
    
    # Determine if no values exist within To Do List
    if len(todo_list) == 0:
        
        # Display message
        print('\nThere is nothing to display')
      
    print()
    
    # Display the tasks within the list
    for item in todo_list:
        
        print(task_count, ': ', item, sep='')
        
        # Increment task number
        task_count += 1
    
    print()
    
    # Return to main function
    main()

# This function displays the items within the Completed 
# Argument(s): completed_list
def view_completed_list(finished_list):
    
    # Initialize task number
    task_count = 1
    
    print()
    
    # Determine if no values exist within To Do List
    if len(finished_list) == 0:
        
        # Display message
        print('\nThere is nothing to display')
    
    # Display the tasks within the list
    for item in finished_list:
        
        print(task_count, ': ', item, sep='')
        
        # Increment the task number
        task_count += 1
        
    print()
    
    # Return to main function
    main()

# This function adds a task to the To Do List and asks the user if the 
# task should be prioritized
def add_todo_list(todo_list):
    
    # Prompt user to enter a new task
    new_task = input('Enter a task to be added to the To Do List: ')
    
    # Add task to To Do List
    todo_list.append(new_task)
    print()
    
    # Prompt user to prioritize the new task
    print('Do you want to priortize the task: Enter [y] if yes |',
          'Enter any other character to skip priority: ')
    is_priority = input()
    print()
    
    # Determine if user has opted to prioritize the task
    if 'y' in is_priority or 'Y' in is_priority:
        
        # Prompt user and obtain input
        priority = int(input('Enter priority of task: 1, 2, 3, etc: '))
        print()
        
        # Validate that user input is within numerical boundaries
        while priority < 0 or priority > len(todo_list) + 1:
            
            # Display error message
            print('Invalid input. Input must be greater than 1 and',
                  'cannot exceed number of items within list')
            
            # Repeat prompt for user input
            priority = int(input('Enter priority of task - 1, 2, 3, etc: '))
            print()
            
        # Remove task from list
        todo_list.remove(new_task)
        
        # Re-enter task into last at prioritized position
        todo_list.insert(priority - 1, new_task)
        
    # Ask the user if another task is desired to be added to the list
    print('Add another task?')
    again = int(input('[1] = yes | [0] = no: '))
    print()
    
    while again < 0 or again > 1:
        again = int(input('Invalid input. Enter [1] to add another task', 
              'or [0] to return to the main menu: '))
    
    # Determine user decision
    if again == 1:
        
        # allow user to add another task
        add_todo_list(todo_list)
        
    elif again == 0:
        
        # redirect back to main
        main()

    # Return to main function
    main()
    
# This function removes a 
# arguments: to_do_list and completed_list
def complete_item(todo_list, finished_list):
    
    # Display the To Do list
    print()
    print('Current To Do List')
    print('------------------')

    # Initialize task number
    task_count = 1
    
    # Display the tasks within the list
    for item in todo_list:
        print(task_count, ': ', item, sep='')
        
        # Increment task number
        task_count += 1
        
    print()
    
    # prompt user to enter the completed task
    finished_task = input('Enter the the task you have completed: ')
    print()
    
    # Determine if the input is within to do list
    if finished_task in to_do_list:
        
        # remove the task from the to do list
        to_do_list.remove(finished_task)
        
        # add the task to the completed list
        completed_list.append(finished_task)
        
    else:
        # Display error message and prompt user to enter a valid task
        print('The task you have entered is not within the To Do List.',
              'Try Again.')
        print()
        
        # Return user to enter a valid task
        complete_item(todo_list, finished_task)
        
    # Return to main function    
    main()

# This function ends the application
def end_program():
    
    print()
    print('Are you sure? All data will be lost upon exit.')
    exit_program = int(input('[1] = yes | [0] = no: '))
    print()
    
    # Validate user input
    while exit_program < 0 or exit_program > 1:
        
        # Display error message and prompt user to enter valid input
        print('Invalid input. Enter [1] to exit', 
              'the program or [0] to continue to stay in the program: ')
        exit_program = int(input())
    
    # Determine course of action for user input
    if exit_program == 1:
        
        # Exit program
        sys.exit(0)
        
    elif exit_program == 0:
        
        print()
        
        # Return to main function
        main()
        
# Run Program
if __name__ == "__main__":
    main()
