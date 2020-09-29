letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters,points)}

letter_to_points[""] = 0


#print(letter_to_points)

# This function displays points for given word

def score_word(word):
  word = word.upper()
  point_total = 0
  for i in word:
    point_total += letter_to_points.get(i, 0)
  return point_total

print(score_word('BROWNIE'))

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}



# This function takes in a player and a word, and add that word to the list of words they’ve played

def play_word(player, word):
  word = word.upper()
  for i in player_to_words.keys():
    if i == player:
      player_to_words[i].append(word)
    else:
      print("Player doesn't exist")
      break
    return player_to_words
    
print(play_word("player1", "Bulldog"))

# This function displays how many points each player score 

def update_point_totals(player_to_words):
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_words[player] = player_points
  return player_to_words

print(update_point_totals(player_to_words))




