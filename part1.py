question = "Name something you have to squeeze really hard before anything comes out."
possible_answers = [("LEMON/CITRUS", 25), ("KETCHUP/MUSTARD", 25), ("TOOTHPASTE", 19), ("ZIT/BLACKHEAD", 14), ("GLUE", 6), ("MY POOPER", 3), ("LOTION BOTTLE", 2), ("LIQUID SOAP/SHAMPOO", 2)]

#player_answer = "mustard"
#player_answer = input("player answer: ")
player_answer = input()
player_score = 0
###################################
####### Start of your code ########
###################################
def is_match(player_answer, possible_answer):
  possible_answer = possible_answer.lower().replace("'s","").replace("/"," ").replace(".","")
  player_answer = player_answer.lower().replace("'s","").replace("/"," ").replace(".","")

  return player_answer in possible_answer

def is_right(player_answer, possible_answers):
  for i,(possible_answer, points) in enumerate(possible_answers):
    if is_match(player_answer, possible_answer):
      #possible_answers.pop(i)
      return points
  
  return 0

player_score = is_right(player_answer, possible_answers)
###################################
######## End of your code #########
###################################
print(player_score)