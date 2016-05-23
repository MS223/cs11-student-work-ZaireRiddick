# I am stuck on the add code
action = raw_input("What would you like to do?")
day = raw_input("What day would you like to do it?").capitalize()
Days = {
    "Monday":[],
    "Tuesday":[],
    "Wednesday":[],
    "Thursday":[],
    "Friday":[],

}

def add(action, day):
    for add in action:
        x = day
    Days[day] = action

    print Days
    #I am trying to add so the user can add the day and what they want to do.

some_dictionary[day].append(action)
    #until you...
    # I need an option to call choice()

def get(day):
    print some_dictionary[day]
    # I need an option to call choice()

def choice():
    user_choice = raw_input("How can I help you?")
    # if they choose 'add' call add()
    # if they choose 'get' call get()
add("something", "monday")

get("monday")
