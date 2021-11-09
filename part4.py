questions_4x = ["Name something a baby does that would be unacceptable in a roommate.", 
                "Name something you have to squeeze really hard before anything comes out.",
                "We asked 100 women... If a man is ugly, he'd better have a beautiful what?",
                "Name something a bald guy might rub on his head."]
possible_answers_4x = [
                      [("CRY/AT 3 A.M.", 39), ("POO/WET SELF", 28), ("PUKE/ON ME", 9), ("BURP", 8), ("MAKE MESS/TOSS FOOD", 5), ("FART", 4), ("PEE IN MY FACE", 3), ("NURSE/ON MY NIPS", 2)],
                      [("LEMON/CITRUS", 25), ("KETCHUP/MUSTARD", 25), ("TOOTHPASTE", 19), ("ZIT/BLACKHEAD", 14), ("GLUE", 6), ("MY POOPER", 3), ("LOTION BOTTLE", 2), ("LIQUID SOAP/SHAMPOO", 2)],
                      [("PERSONALITY",31),("SMILE/MOUTH",17),("HEART/SOUL",17),("BANK ACCOUNT/JOB",14),("CAR/ROLLS-ROYCE",9),("HOUSE",4),("WIFE/CHICK",4),("BODY/MAN-CAN",3)],
                      [("LOTION/SUNSCREEN",51),("OIL/BABY OIL",18),("WAX/POLISH",6),("ROGAINE/HAIR MED",5),("HIS HAND",5),("PET. JELLY/OINTMENT",5),("SHAMPOO/SOAP",3),("CHICK'S BOOBS",2)]]

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

for r in range(4):
  player_1_strikes_left = 3
  player_2_strikes_left = 3
  multiplier = r if r > 1 else 1
  question = questions_4x[r]
  possible_answers = possible_answers_4x[r]
  #print(f'question: {question}')
  #print(f'possible_answers: {possible_answers}')
  round_points = 0
  #player_1_answer = input("player 1 answer: ")
  player_1_answer = input()
  round_points += multiplier*is_right(player_1_answer,possible_answers)
  if round_points != 0:
    #print("\nplayer 1 controls\n")
    while player_1_strikes_left != 0 and len(possible_answers) != 0:
      #player_1_answer = input("player 1 answer: ")
      player_1_answer = input()
      points = multiplier*is_right(player_1_answer,possible_answers)
      if points == 0:
        player_1_strikes_left -= 1
        #print("WRONG!\n")
      else:
        round_points += points

    if len(possible_answers) == 0:
      player_1_score += round_points
    else:
      #print(" \nplayer 1 out of strikes. player 2, chance to steal")
      #print(f'\n{possible_answers}\n')
      #player_2_answer = input("player 2 answer: ")
      player_2_answer = input()
      points = multiplier*is_right(player_2_answer, possible_answers)
      if points != 0:
        player_2_score += round_points
      else:
        player_1_score += round_points
  else:
    #print("\nplayer 2 controls")
    while player_2_strikes_left != 0 and len(possible_answers) != 0:
      #player_2_answer = input("player 2 answer: ")
      player_2_answer = input()
      points = multiplier*is_right(player_2_answer,possible_answers)
      if points == 0:
        player_2_strikes_left -= 1
        #print("WRONG!\n")
      else:
        round_points += points

    if len(possible_answers) == 0:
      player_2_score += round_points
    else:
      #print(" \nplayer 2 out of strikes. player 1, chance to steal")
      #print(f'\n{possible_answers}\n')
      #player_1_answer = input("player 1 answer: ")
      player_1_answer = input()
      points = multiplier*is_right(player_1_answer, possible_answers)
      if points != 0:
        player_1_score += round_points
      else:
        player_2_score += round_points
  #print("\nROUND OVER!")
  #print(f'player 1 score: {player_1_score}, player 1 strikes left: {player_1_strikes_left},   player 2 score: {player_2_score}, player 2 strikes left: {player_2_strikes_left}')
#print("GAME OVER!")
###################################
######## End of your code #########
###################################
print(f'player 1 score: {player_1_score}, player 1 strikes left: {player_1_strikes_left},   player 2 score: {player_2_score}, player 2 strikes left: {player_2_strikes_left}')