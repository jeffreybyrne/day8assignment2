#Exercise 0
#Lists of my favourite colours, age of me and my siblings, five coin flips, and three artists
fav_colours = ['red','blue','green']
ages = [33,30,32,29]
coins = [True,False,False,True,True]
fav_artists = ['The Offspring','Great Big Sea','Barenaked Ladies']
#Dicts of three words & definitions, favourite movie names and their years, three cities and their pops, names of my siblings and their ages
words = {'croze': 'groove in the staves of a cask', 'soliloquent': 'speaking in soliloquies; prone to giving soliloquies', 'recte': 'correctly; which should be'}
fav_movies = {'BASEketball': 1998, 'Blade Runner 2049': 2017, 'Back to the Future': 1985}
cities = {'Chicago': 2695598, 'Halifax': 403131, "St. John's": 108860}
my_siblings = {'John': 33, 'Darrell': 32, 'Jeff': 30, 'Kim': 29}


#Exercise 1
# Print out the list of coin flips.
print(coins)
# Print out the first element of the list of your favourite colours.
print(fav_colours[0])
# Output the sorted version of the list of your friends and family members' ages.
print(sorted(ages))
# Add a new baby (0 years old) to the list of your family's ages.
ages.append(0)
print(ages)
# Using the dictionary of movie information, access and print the year of one of the movies.
print(fav_movies['BASEketball'])

#Exercise 2
# Print out the last element of the list of your favourite colours.
# Note: do this in a way that would still work for a list of any size!
print(fav_colours[-1])
# Add a new city to the dictionary of cities and population.
cities["Georgetown"] = 42123
# Reverse the list of coin flips and save it.
coins.reverse()
# Print out the population of one of the cities.
print(cities['Halifax'])
# Print out a sentence about each item in the list of performing artists.
for artist in fav_artists:
    print("I think {} is pretty neat".format(artist))

#Exercise 3
# Print out the first two performing artists in that list.
print(fav_artists[0])
print(fav_artists[1])
# For each of your favourite movies, print out a sentence about when the movie was released.
for movie, value in fav_movies.items():
    print("{} came out in {}".format(movie,value))
# Sort and reverse the list of ages of your family. Save it and print it to the screen.
# See if you can sort and reverse the list on one line!
ages.reverse()
print(ages)
# Add "Beauty and the Beast" movie to your dictionary of movies information, but with a twist: the movie was released both in 1991 and in 2017. Print it out.
fav_movies["Beauty and the Beast"] = '1991,2017'
print(fav_movies)

#Exercise 4
# Print out all of the ages of your friends/family that are less than 30 (or any number where some ages will not be printed!).
for age in ages:
    if age < 30:
        print(age)
# Find and output the age of the oldest person in your friends/family list.
print(max(ages))
# Count how many times you flipped 'heads' using the coin flips list.
print(coins.count(True))
# You realize one of the performing artists in your list is no longer a favourite. Remove one of them from the list.
fav_artists.pop()
# Pick a city in your city population dictionary and change its population.
cities['Chicago'] = 2023407

#Exercise 5
# Find the sum total of the population in the dictionary of cities.
total_pop = 0
for city, value in cities.items():
    total_pop += value
# Using your dictionary containing the names of your family and friends with their ages, print out one of two messages for each depending on their age.
for sibling, age in my_siblings.items():
    if age > 30:
        print('Dang, {} is old!'.format(sibling))
    else:
        print("Good, {} isn't old yet".format(sibling))
# Print out the last two colours in your list of favourite colours.
print(fav_colours[-2:])
# Increase by 1 the age of everyone in your list of ages. Print it out.
for sibling, age in my_siblings.items():
    my_siblings[sibling] = age + 1
# Add two new colours to your list of favourite colours.
fav_colours.append('fuschia')
fav_colours.append('cerulean')

#Exercise 6
# Make a new dictionary that contains a list of movies for each year. Each list of movies should be a list. Below is some data you can use.
#
# 1999: The Matrix, Star Wars: Episode 1, The Mummy
# 2009: Avatar, Star Trek, District 9
# 2019: How to Train Your Dragon 3, Toy Story 4, Star Wars: Episode 9
movies_by_year = {
    1999: ['The Matrix', 'Star Wars: Episode 1', 'The Mummy'],
    2009: ['Avatar', 'Star Trek', 'District 9'],
    2019: ['How to Train Your Dragon 3', 'Toy Story 4', 'Star Wars: Episode 9']
}
# Make a new list that contains each row of the buttons on a phone. Each row should be a list.
# The rows on a phone are: 1 2 3, 4 5 6, 7 8 9, * 0 #
phone_nums = [[1,2,3],[4,5,6],['*',0,'#']]
# Make a new list that contains information about three countries. Each country should be a dictionary that has a name, a continent, and whether or not it is an island.
countries = [
    {'name': 'Ireland',
    'continent': 'Europe',
    'island': True},
    {'name': 'Canada',
    'continent': 'North America',
    'island': False},
    {'name': 'Guyana',
    'continent': 'South America',
    'island': False}
]

#Exercise 7
# Output the message "I will not skateboard in the halls" 20 times.
for number in range(0,20):
    print('I will not skateboard in the halls')
# Create a list consisting of the above message. It should appear in the list 20 times.
message_list = []
for number in range(0,20):
    message_list.append('I will not skateboard in the halls')

# Create a list consisting of the numbers between 1 and 50.
one_to_fifty = list(range(1,51))

# Use a for loop to find the sum of the numbers in the above list.
list_sum = 0
for number in one_to_fifty:
    list_sum += one_to_fifty[number-1]
# Create a new list which has three of each number up to 50.
# Ie. [1, 1, 1, 2, 2, 2, 3, 3, 3, ... , 50, 50, 50] and so on, up to 50.
new_list = []
for number in range(1,51):
    new_list.append(number)
    new_list.append(number)
    new_list.append(number)

# Make a new list out all of the countries from the dictionary in Exercise 6 that are not islands. Print out both lists.
non_islands = []
islands = []
for each_country in countries:
    if each_country['island']:
        islands.append(each_country['name'])
    elif not each_country['island']:
        non_islands.append(each_country['name'])

print('The list of non-islands is {}'.format(non_islands))
print('The list of islands is {}'.format(islands))
