import sys

meny = '''
[1] Show movie database
[2] Add movie to database
[3] Remove movie from database
[4] View movie information
[5] Exit
'''

class addMovie:
    def __init__(self):
        print("Choose a genre:")
        print("1. horror")
        print("2. drama")
        print("3. other")

        choice = input("Enter 1, 2, or 3: ").strip()
        genres = {"1": "horror", "2": "drama", "3": "other"}
        self.genre = genres.get(choice, "unknown")

        self.title = input("Title: ").strip()
        self.release_year = input("Release year: ").strip()

    def to_dict(self):
        return {"release year": self.release_year}

    def __repr__(self):
        return f"{self.title} ({self.release_year}) [{self.genre}]"   


movieDB = {
        "horror": { 
            "the wailing": {"release year": "2018"},
            "the thing": {"release year": "1982"}
                   },
        "drama": {
            "parasite": {"release year": "2018"}
            },
        "other": {
            "spiderman": {"release year": "2005"}
            }
        }


def printDatabase():
    for genre, movies in movieDB.items():
        print(genre)
        for title in movies:
            print(f"  {title}")
    pass

def addToDatabase():
    m = addMovie()
    
    movieDB.setdefault(m.genre, {})[m.title] = m.to_dict()   

    pass

def removeFromDatabase():
    printDatabase()
    db = movieDB

    genre = input("input the genre of the movie to remove:  ").strip()
    title = input("input the title to remove:  ").strip()

    if genre in db and title in db[genre]:
        del db[genre][title]
        print(f"Removed {title}")
    else:
        print(f"Either the genre or the title or both was not found")

    pass

def showMovieInfo():
    printDatabase()
    db = movieDB
    genre = input("input the genre of the movie:  ").strip()
    title = input("input the title to show more:  ").strip()
    
    if genre in db and title in db[genre]:
        for k, v in db[genre][title].items():
            print(f"  {k}: {v}")

    else:
        print("Not found")

    pass

if __name__=='__main__':
    while True:
        choise = input(meny)

        options = {
                '1': printDatabase,
                '2': addToDatabase,
                '3': removeFromDatabase,
                '4': showMovieInfo,
                '5': sys.exit
                }.get(choise, lambda: print("No option was selecte, to select an option type its-\n" 
                "respecitve number and press Enter"))

        options()

