##
# videogame_rater.py
# rates video games

def print_dictionary(dictionary):
    for id, game in dictionary.items():
        for k, v in game.items():
            print("ID: {} game: {}\trating: {}".format(id, game["name"], game["Rating"]))

if __name__ == "__main__":
    
    videogames = {1:{"name":"MineCraft", "Rating":5,},
                  2:{"name":"Call Of Duty", "Rating":1},
                  3:{"name":"Angry Birds", "Rating":4},
                  4:{"name":"Splatoon 2", "Rating":5},
                  5:{"name":"Animal Crossing", "Rating":4}}

    print_dictionary(videogames)
