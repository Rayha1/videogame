##
# videogame_rater.py
# rates video games

def print_dictionary(dictionary):
    for game, rating in dictionary.items():
        print("game:", game, "rating:", rating)

if __name__ == "__main__":
    
    videogames = {"MineCraft":5, "Call Of Duty":1, "Angry Birds":4,
                  "Splatoon 2":5, "Animal Crossing":4}

    print(videogames)
