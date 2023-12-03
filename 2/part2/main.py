
red_amount = 12
green_amount = 13
blue_amount = 14

colors = ["blue", "red", "green"]

data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"""
data = data.replace(",", '')

current_game_dict = {}
all_dicts = []
all_games = []
flagga = False
current_game = -1
rows = data.split("\n")
sentence = ""
for outer_index, row in enumerate(rows):
    sentence = list(row.split(" "))
    for index, word in enumerate(sentence):
        if word == "Game" and flagga:
            all_games.append(all_dicts)
            all_dicts = []
            current_game_dict = {}
        if ';' in word:
            word = word.replace(";", '')
            current_game_dict[word] = sentence[index -1] 
            all_dicts.append(current_game_dict)
            current_game_dict = {}
            continue
        if word in colors:
            current_game_dict[word] = sentence[index -1]
        flagga = True
        if index == len(sentence) -1:
            all_dicts.append(current_game_dict)

    if outer_index == len(rows) -1:
        #all_dicts.append(current_game_dict)
        all_games.append(all_dicts)
        print("dick", )


for elem in all_games:
    print(elem)
