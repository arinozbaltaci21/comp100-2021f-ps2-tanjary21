question = "Name something a baby does that would be unacceptable in a roommate."
possible_answers = [("CRY/AT 3 A.M.", 39), ("POO/WET SELF", 28), ("PUKE/ON ME", 9), ("BURP", 8), ("MAKE MESS/TOSS FOOD", 5), ("FART", 4), ("PEE IN MY FACE", 3), ("NURSE/ON MY NIPS", 2)]

player_strikes_left = 3
player_score = 0
###################################
####### Start of your code ########
###################################
def is_match(player_answer, possible_answer):
  possible_answer = possible_answer.lower().replace("'s","").replace("/"," ").replace(".","")
  player_answer = player_answer.lower().replace("'s","").replace("/"," ").replace(".","")
  #print(player_answer, possible_answer)
  return player_answer in possible_answer

def is_right(player_answer, possible_answers):
  for i,(possible_answer, points) in enumerate(possible_answers):
    if is_match(player_answer, possible_answer):
      possible_answers.pop(i)
      return points
  
  return 0

while player_strikes_left != 0 and len(possible_answers) != 0:
  #player_answer = input("player answer: ")
  player_answer = input().strip()
  points = is_right(player_answer,possible_answers)
  if points == 0:
    player_strikes_left -= 1
  else:
    player_score += points
  
###################################
######## End of your code #########
###################################
print(f'player score: {player_score}, player strikes left: {player_strikes_left}')
