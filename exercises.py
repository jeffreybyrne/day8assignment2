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
