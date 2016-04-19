#a = [1, 2, 4]
#b = a

# input: a list of ints
# output: an int
def update_list(a_list):
    a_list[3] = "yo"
    b = a_list[4]
    b = 100
my_list = [1, 2, 3, 4, 5]
update_list(my_list)
print my_list
# This will print out yo with one of the numbers in the list

var_1 = "kittens" # local
var_2 = "cookies" # local
# input: a string
# output: a string
def my_function(my_favorite_things): # global
    song_lyrics = "rain drops on roses," # local
    combined_song = song_lyrics + my_favorite_things # local
    return combined_song
# input: a string
# output: a string
def my_function_2(item, item2): # global
    full_lyrics = item + "on " + item2 #local
    full_song = my_function(full_lyrics)
    return full_song
my_song = my_function_2(var_1, var_2)

var_1 = 'cat' # local
var_2 = 'dog' # local

def print_out_my_favorite(favorite_pet): # global
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    if favorite_pet == var_2:
        print("My favorite pet is the dog.")
    

print_out_my_favorite(var_1)
print(var_2)

def my_num 

