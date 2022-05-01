def string_check(choice, options):

    for var_list in options:

        # if the snack is in one of the lists, return
        if choice in var_list:

            # get full name of snack and put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to not valid
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

# valid snacks holds list of all snacks
# Each item in valid snacks is a list with
# valid options for each snack <full name, letter code (a - e)
# . and possible abbriviations etc>
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]


# yes / no checker
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# holds snack order for a single user
snack_order = []

check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

# If they say yes, ask what snacks they want (and add to our snack order)
if check_snack == "yes":

    desired_snack = ""
    while desired_snack != "xxx":
        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

    # check if the snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack choice: ", snack_choice)

    # Add to snack list

    # check that snack is not the exit code before adding
    if snack_choice != "xxx" and snack_choice != "invalid choice":
        snack_order.append(snack_choice)

# show snack orders
print()
if len(snack_order) == 0:
    print("Snacks ordered: None")

else:
    print("Snacks ordered: ")

    for item in snack_order:
        print(item)

