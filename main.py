# import statements

# functions go here

# ➤ checks that the ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry - this can't be blank")

# checks for an integer between two values
def int_check(question, low_num, high_num):

    error = "Please enter an integer between {} " \
            "and {}".format(low_num, high_num)


    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if  low_num <= response <= high_num:
                return response
            else:
                print(error)

        # if an integer is not entered, display an error
        except ValueError:
            print(error)

# ★☆★☆★☆★☆★☆★ Main Routine ★☆★☆★☆★☆★☆★

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details

# start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tells user how many seats are left
    if count < 4:
        print("You have {} seats "
           "left".format(MAX_TICKETS - count))

    # Warns user that only one seat is left
    else:
        print("☆☆☆ There is ONE seat left! ☆☆☆")

    # Get name (can't be blank)
    name = not_blank("Name: ")
    count += 1

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # get age (between 12 and 130)
    age = int_check("Age: ", 12, 130)

# End of tickets loop

# Calculate profit etc...
if count == MAX_TICKETS:
    print ("You have sold all the available tickets!")
else:
    print("you have sold {} tickets.   \n"
          "There are {} places still available"
          .format(count, MAX_TICKETS - count))

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary

# Calculate Total sales and profit

# Output data to text file
