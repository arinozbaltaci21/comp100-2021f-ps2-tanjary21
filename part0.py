question = "Name something a baby does that would be unacceptable in a roommate."

possible_answer = "MAKE MESS/TOSS FOOD"
player_answer = "mess"
is_correct = None
###################################
####### Start of your code ########
###################################
def is_right(player_answer, possible_answer):
  possible_answer = possible_answer.lower().replace("'s","").replace("/"," ").replace(".","")
  player_answer = player_answer.lower().replace("'s","").replace("/"," ").replace(".","")

  return player_answer in possible_answer

is_correct = is_right(player_answer, possible_answer)
###################################
######## End of your code #########
###################################
print(is_correct)