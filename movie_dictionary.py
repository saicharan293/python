movies={
    'Harry Potter':'1pm',
    'Resident Evil':'2pm',
    'Game of Thrones':'2:20pm',
    'Max Steel':'4pm'
}

print("We're showing following movies: ")

for movie in movies:
    print(movie)
movie_name=input("Which movie do you like to watch? ").title()
#title() : turns the first letter of every word present
# in the string as capital
show_time=movies.get(movie_name)
if show_time==None:
    print("Not available")
else:
    print(movie,'is playing at',show_time)