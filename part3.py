question = "Name something a baby does that would be unacceptable in a roommate."
possible_answers = [("CRY/AT 3 A.M.", 39), ("POO/WET SELF", 28), ("PUKE/ON ME", 9), ("BURP", 8), ("MAKE MESS/TOSS FOOD", 5), ("FART", 4), ("PEE IN MY FACE", 3), ("NURSE/ON MY NIPS", 2)]

player_1_strikes_left = 3
player_2_strikes_left = 3
player_1_score = 0
player_2_score = 0
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
      possible_answers.pop(i)
      return points
  
  return 0


round_points = 0

player_1_answer = input().strip()
round_points += is_right(player_1_answer,possible_answers)
if round_points != 0:
  
  while player_1_strikes_left != 0 and len(possible_answers) != 0:
    
    player_1_answer = input().strip()
    points = is_right(player_1_answer,possible_answers)
    if points == 0:
      player_1_strikes_left -= 1
      
    else:
      round_points += points

  if len(possible_answers) == 0:
    player_1_score += round_points
  else:
    
    player_2_answer = input().strip()
    points = is_right(player_2_answer, possible_answers)
    if points != 0:
      player_2_score += round_points
    else:
      player_1_score += round_points
else:
 
  while player_2_strikes_left != 0 and len(possible_answers) != 0:
    
    player_2_answer = input().strip()
    points = is_right(player_2_answer,possible_answers)
    if points == 0:
      player_2_strikes_left -= 1
     
    else:
      round_points += points

  if len(possible_answers) == 0:
    player_2_score += round_points
  else:
   
    player_1_answer = input().strip()
    points = is_right(player_1_answer, possible_answers)
    if points != 0:
      player_1_score += round_points
    else:
      player_2_score += round_points


###################################
######## End of your code #########
###################################
print(f'player 1 score: {player_1_score}, player 1 strikes left: {player_1_strikes_left},   player 2 score: {player_2_score}, player 2 strikes left: {player_2_strikes_left}')
