#file = open("tasks.txt","r")
#tasks = file.read().split("\n")
#for task in tasks:
#    print(f"{tasks.index(task)}. {task}")


# Use loops to calculate the sum of the numbers below
#numbers = [10, 5, 20, 8, 15]
#total = 0

#for number in numbers:
#    total = total + number
#print("The sum is", total)

# Open the file emails.txt in READ mode
#file = open("emails.txt","r")
# Read and split the data using \n to get a list
#emails = file.read().split("\n")
# Loop over the list of emails and print a generated username for each of them i.e username is all characters before the @
#for email in emails:
#    user_name = email.split("@")[0]
#    print(user_name)


# Define a register user function
# def register_user(name, email, password):
    # Check if user does not already exist
    # Hash user password
    # Validate inputs
    # Check if user is not a robot
    # Return response 
#    return "User registered successfully!"


import add
import show
import update
import delete

add_task_response = add.add_task("Sleep")
print(add_task_response)

show_tasks_response = show.show_tasks()
print(show_tasks_response)

update_task_response = update.update_task("Sleep", "Wake Up")
print(update_task_response)

delete_task_response = delete.delete_task("Wake Up")
print(delete_task_response)


























































































































