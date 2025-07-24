# 1
my_dict = {'name': 'Alexander', 'age': 40, 'favour_color': 'black'}
print(my_dict)
print(type(my_dict))

# 2
my_dict = {
    'Titanic': ['Leonardo DiCaprio', 'Kate Winslet', 'Billy Zane'],
    'Fight Club': ['Brad Pitt', 'Edward Norton', 'Helena Bonham Carter'],
    'The Green Mile': ['Tom Hanks', 'David Morse', 'Michael Clarke Duncan'],
    'Taxi Driver': ['Robert De Niro', 'Robert De Niro', 'Cybill Shepherd']
}
movie_info = input('enter the name of the movie to know its actors')
print(my_dict.get(movie_info, 'the movie is not in the list yet'))

# 3
country = 'Russia'
capital = 'Moscow'
pop_size = 140
my_dict = {'Country': country, 'Capital': capital, 'Population size': pop_size}
print(my_dict)

# 4
my_dict = {'Eugene Onegin': ['novel', 1833], 'War and peace': ['novel', 1867], 'Macbeth': ['play', 1623]}
print(my_dict)

# 5
my_dict = {'Russia': 'Moscow', 'USA': 'Washington DC', 'Ukraine': 'Kiev'}
print(my_dict)

# 6
my_dict = {'orange': 80, 'banana': 170, 'kiwi': 100, 'tangerine': 170, 'grape': 180, 'apple': 75}
fruit_name = input('enter the name of the fruit').lower()
fruit_weight = float(input('enter the weight of the fruit in kilograms'))
print(my_dict[fruit_name]*fruit_weight)
