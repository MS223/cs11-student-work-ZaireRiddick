action = raw_input("What would you like to do?")
day = raw_input("What day would you like to do it?").capitalize()
Days = {
    "Monday":[],
    "Tuesday":[],
    "Wednesday":[],
    "Thursday":[],
    "Friday":[],

}

def add():
    Days[day] = action
    print Days
    #I am trying to add so the user can add the day and what they want to do.
