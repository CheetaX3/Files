import random
import cities_functions as cf

CITIES_FILEPATH = 'c:/Users/User/Desktop/Technium/Files/Cities/cities.txt'
ANSWERS_FILEPATH ='c:/Users/User/Desktop/Technium/Files/Cities/answers.txt'
MAX_ERRORS = 5

cf.game(CITIES_FILEPATH, ANSWERS_FILEPATH, MAX_ERRORS)