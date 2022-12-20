"""Restaurant rating lister."""


# Pseudo:
#inputs: ratings from the given file
#outputs: a printed statement giving the aphabetical ordered ratings of the restaurants 

# Your job is to write a program named ratings.py that:
# Reads the ratings in from the file
# Stores them in a dictionary
# And finally, spits out the ratings in alphabetical order by restaurant
# 

#open the file - store the file in the variable name data
def restaurant_ratings(filename):
    data = open(filename)
    #create an empty dictionary to store the data from the file - call it alphabetized_restaurant_ratings 
    alphabetized_restaurant_ratings = {}

    restaurant_name = " " #key
    restaurant_rating = 0 #value - might need to change?  

    for line in data:
        #restaurant_rating = everything after the :
        #restaurant_name = everything before the :
        restaurant_info = line.rstrip()
        #need to rename variable below
        restaurant_info = restaurant_info.split(":")
        #if restaurant name is not in dictionary as a key then add restaurant name with rating as the value
        
        #create a tuple to store the restaurant names and the ratings as a key/value pair 
        alphabetized_restaurant_ratings.items()
print(restaurant_ratings("scores.txt"))
    # To append an element to an existing dictionary, 
        #you have to use the dictionary name followed by square brackets with the key name and assign a value to it.

    #put the name of the restaurant into the dictionary as the key, then put the corresponding number as the value
        #restaurant name = key
        #restaurant rating = value
    #to add a value syntax:
        
    

    


#sort the dictionary using sorted() method 
    #Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.
    #Hint 2: Refer to the Python docs on the sorted() function if you need a reminder of how to sort.

#for animal, number in sorted(animal.items()):
#print(f"{animal}: {number})