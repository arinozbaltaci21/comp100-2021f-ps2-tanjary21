# Family Feud

## Due Sunday, November 14, 2021 at 23:00.

 In this assignment, you will implement a simple Family Feud game. If you are not familiar with how this game is played, you can check [this YouTube video](https://youtu.be/t_uekfoX5zk) or [read this](https://www.liveabout.com/family-feud-brief-overview-1396911) briefly. Please play close attention to the scoring scheme in the video. 
 
 We will implement a much simpler version of this game:
 * We will NOT implement the initial stage which involves the buzzer, and assume that player 1 always presses the buzzer first.
 * We will not implement the *Fast Money Round*. 
 * We will only implement the main game with 4 rounds. 
 * We will assume that a player represents their entire team.

Let's build it step by step! 

 ### Part 0
Look at the "part0.py" file. You are given an example player answer and an example possible answer. Your task is to implement the program to check whether the answer from a player matches a given answer. Note that the palyer answer does not have to be exactly the same as the possible answer, there might be differences due to upper/lower case, punctuation, etc. See below some example test cases to handle this.

**Hint:** It might be useful to check the following functions: `String.lower()` and `String.replace()`

 ```
 # Test case 1
 possible_answer = "MAKE MESS/TOSS FOOD"
 player_answer = "mess"
 ###########################
 print(is_correct) # should print True
 
 # Test case 2
 possible_answer = "POO/WET SELF"
 player_answer = "wEt SeLf"
 ###########################
 print(is_correct) # should print True

 # Test case 3
 possible_answer = "CRY/AT 3 A.M."
 player_answer = "crY at 3 am"
 ###########################
 print(is_correct) # should print True

 # Test case 4
 possible_answer = "CRY/AT 3 A.M."
 player_answer = "cries at 3 am"
 ###########################
 print(is_correct) # should print False

 # Test case 5
 possible_answer = "PEE IN MY FACE"
 player_answer = "pee's in my face"
 ###########################
 print(is_correct) # should print True

 # Test case 6
 possible_answer = "NURSE'S ON MY NIPS"
 player_answer = "nuRsE on my nips"
 ###########################
 print(is_correct) # should print True
 
 ```

**Note:** You may use print statements within your code while you are debugging your code but these will interfere with the Autograder. So please make sure to remove all print statements (except the original print statement) before your last commit. Keep this in mind for all the parts.
 
 ### Part 1
 Let's make things a bit more practical. As you may have observed from the game format, there will be several possible answers that a player can guess from. Each possible answer has a certain amount of points associated with it. If the player guesses an answer that exists in the possible answers, they will be rewarded with the corresponding amount of points.

 Look at the file "part1.py". Write a program to check the player answer against the possible answers and print the appropriate points. You may implement it as a function.

 Listed below are some test cases for you to try out. The `question` and `possible_answers` are already in the "part1.py" file. You should read the `player_answer` as input from the user and assign the result to the `player_score` variable that is printed in the end.

```
question = "Name something you have to squeeze really hard before anything comes out."
possible_answers = [("LEMON/CITRUS", 25), ("KETCHUP/MUSTARD", 25), ("TOOTHPASTE", 19), ("ZIT/BLACKHEAD", 14), ("GLUE", 6), ("MY POOPER", 3), ("LOTION BOTTLE", 2), ("LIQUID SOAP/SHAMPOO", 2)]

# Test case 1
player answer: mustard
25  

# Test case 2
player answer: zit
14

# Test case 3
player answer: mayonnaise
0

```

### Part 2
Now, you will extend your work from **Part 1** such that the player can continue guessing until they run out of strikes or they guess all the possible answers. Implement your solution in "part2.py" file.

**Note:** Each correct guess should increase the player's score. The player will lose a strike if they guess something that has already been guessed before or guess something that isn't in the set of possible answers.

Here are some test cases for you to try out:
```
question = "Name something a baby does that would be unacceptable in a roommate."

possible_answers = [("CRY/AT 3 A.M.", 39), ("POO/WET SELF", 28), ("PUKE/ON ME", 9), ("BURP", 8), ("MAKE MESS/TOSS FOOD", 5), ("FART", 4), ("PEE IN MY FACE", 3), ("NURSE/ON MY NIPS", 2)]

# Test case 1
player answer: poo
player answer: wet self
player answer: wet self
player answer: wet self
player score: 28, player strikes left: 0

# Test case 2
player answer: cry
player answer: cry some more
player answer: cry a lot
player answer: wake me at 3 am
player score: 39, player strikes left: 0

# Test case 3
player answer: cry
player answer: make mess
player answer: eat my candy
player answer: poo
player answer: fart
player answer: puke on me
player answer: pee
player answer: burp
player answer: nurse
player score: 98, player strikes left: 2
```

### Part 3
Now, you will extend your work from **Part 2** such that TWO players may play a round and play against each other. 

Here are some subtle rules of the game:
* Note that we will not implement a buzzer, instead, we will assume that player 1 always rings first. Note also that we will not implement the *Fast Money Round*

* If player 1 makes a correct first guess, they get *control* of the round. Otherwise, player 2 gets *control* of the round.

* The player that has control of the round will keep guessing and collect points until they guess all the possible answers. In this case, the round is over and the points are banked to the *controlling player*'s account.

* If the *controlling player* loses all their strikes before guessing all the answers, the *other player* gets a chance to *steal* the *controlling player*'s points for the round. 
  - If the *other player* makes a correct guess, all the points earned by the *controlling player* in the current round are banked to the *other player*'s account. 
  - If the *other player* makes an incorrect guess, all the points earned by the *controlling player* in the current round are banked to the *controlling player*'s account.
  - Then the round ends.

* When a player steals the points, they do not gain the points of their guess. They only gain the points that the *controlling player* collected for the current round.


Implement your solution in "part3.py" so that we can play one round with two players. 

Here are some test cases for you to try out:
```
question = "Name something a baby does that would be unacceptable in a roommate."
possible_answers = [("CRY/AT 3 A.M.", 39), ("POO/WET SELF", 28), ("PUKE/ON ME", 9), ("BURP", 8), ("MAKE MESS/TOSS FOOD", 5), ("FART", 4), ("PEE IN MY FACE", 3), ("NURSE/ON MY NIPS", 2)]

# Test case 1 - player 1 controls, gains 84 points, loses all 3 strikes, player 2 gets chance to steal but fails, player 1 wins round 
player 1 answer: cry
player 1 answer: poo
player 1 answer: puke
player 1 answer: burp
player 1 answer: cry
player 1 answer: cry
player 1 answer: cry
player 2 answer: cry
player 1 score: 84, player 1 strikes left: 0,   player 2 score: 0, player 2 strikes left: 3

# Test case 2 - player 1 controls, gains 84 points, loses all 3 strikes, player 2 gets chance to steal and succeeds, player 2 wins round 
player 1 answer: cry
player 1 answer: poo
player 1 answer: puke
player 1 answer: burp
player 1 answer: cry
player 1 answer: cry
player 1 answer: cry
player 2 answer: fart
player 1 score: 0, player 1 strikes left: 0,   player 2 score: 84, player 2 strikes left: 3

# Test case 3 - player 2 controls, gains 84 points, loses all 3 strikes, player 1 gets chance to steal and fails, player 2 wins round
player 1 answer: eat my candy
player 2 answer: cry
player 2 answer: poo
player 2 answer: puke
player 2 answer: burp
player 2 answer: cry
player 2 answer: cry
player 2 answer: cry
player 1 answer: cry
player 1 score: 0, player 1 strikes left: 3,   player 2 score: 84, player 2 strikes left: 0

# Test case 4 - player 2 controls, gains 84 points, loses all 3 strikes, player 1 gets chance to steal and succeeds, player 1 wins round
player 1 answer: eat my candy
player 2 answer: cry
player 2 answer: poo
player 2 answer: puke
player 2 answer: burp
player 2 answer: cry
player 2 answer: cry
player 2 answer: cry
player 1 answer: fart
player 1 score: 84, player 1 strikes left: 3,   player 2 score: 0, player 2 strikes left: 0

# Test case 5 - player 1 wins round but loses 2 strikes
player 1 answer: cry
player 1 answer: poo
player 1 answer: nurse
player 1 answer: pee
player 1 answer: fart
player 1 answer: mess
player 1 answer: burp
player 1 answer: eat my candy
player 1 answer: burp
player 1 answer: puke
player 1 score: 98, player 1 strikes left: 1,   player 2 score: 0, player 2 strikes left: 3
```

### Part 4
In this part, you will extend your work from **Part 3** such that we can play multiple rounds. Implement your solution to in "part4.py".

* Note that there should be a score multiplier of x2 in the third round, and x3 in the fourth round. The first and second rounds do not have any score multipliers.
* Also note that at each round, the players get 3 fresh strikes. Remainder strikes from the previous round are not carried forward.

Here is one test case (a full game with 4 rounds) to test your program:

**Note:** `questions_4x` and `possible_answers_4x` are given in the "part4.py" file. 

* You need to extract the appropriate question and possible answers depending on the round. 
* You should implement 4 rounds
* When you are committing your final version, make sure there is only one print statement that prints the final results after the whole game is over
* Note that the possible answers are not visible to the players. We are only printing them for debugging purposes.
```
question: Name something a baby does that would be unacceptable in a roommate.
possible_answers: [('CRY/AT 3 A.M.', 39), ('POO/WET SELF', 28), ('PUKE/ON ME', 9), ('BURP', 8), ('MAKE MESS/TOSS FOOD', 5), ('FART', 4), ('PEE IN MY FACE', 3), ('NURSE/ON MY NIPS', 2)]

# round 1: player 2 gets control, earns 89 points but strikes out, player 1 successfully steals the points.
player 1 answer: eat my candy
player 2 answer: cry
player 2 answer: poo
player 2 answer: puke
player 2 answer: burp
player 2 answer: maKe MeSs
player 2 answer: toss fOOd
player 2 answer: cry
player 2 answer: cry
player 1 answer: fart

player 1 score: 89, player 1 strikes left: 3,   player 2 score: 0, player 2 strikes left: 0

question: Name something you have to squeeze really hard before anything comes out.
possible_answers: [('LEMON/CITRUS', 25), ('KETCHUP/MUSTARD', 25), ('TOOTHPASTE', 19), ('ZIT/BLACKHEAD', 14), ('GLUE', 6), ('MY POOPER', 3), ('LOTION BOTTLE', 2), ('LIQUID SOAP/SHAMPOO', 2)]

# round 2: player 1 gets control, earns 89 points, loses all strikes, player 2 successfully steals the points. Note that the points from the previous round are carried forward
player 1 answer: lemon
player 1 answer: mustard
player 1 answer: ketchup
player 1 answer: toothpaste
player 1 answer: zit
player 1 answer: glue
player 1 answer: glue
player 1 answer: butthole
player 2 answer: pooper

player 1 score: 89, player 1 strikes left: 0,   player 2 score: 89, player 2 strikes left: 3

question: We asked 100 women... If a man is ugly, he'd better have a beautiful what?
possible_answers: [('PERSONALITY', 31), ('SMILE/MOUTH', 17), ('HEART/SOUL', 17), ('BANK ACCOUNT/JOB', 14), ('CAR/ROLLS-ROYCE', 9), ('HOUSE', 4), ('WIFE/CHICK', 4), ('BODY/MAN-CAN', 3)]

# round 3: player 1 gets control, earns 99x2 points by guessing everything. 198 points are banked to player 1's score.
player 1 answer: personality
player 1 answer: mouth
player 1 answer: heart
player 1 answer: job
player 1 answer: car
player 1 answer: house
player 1 answer: wife
player 1 answer: body

player 1 score: 287, player 1 strikes left: 3,   player 2 score: 89, player 2 strikes left: 3

question: Name something a bald guy might rub on his head.
possible_answers: [('LOTION/SUNSCREEN', 51), ('OIL/BABY OIL', 18), ('WAX/POLISH', 6), ('ROGAINE/HAIR MED', 5), ('HIS HAND', 5), ('PET. JELLY/OINTMENT', 5), ('SHAMPOO/SOAP', 3), ("CHICK'S BOOBS", 2)]

# round 4: player 1 gets control, earns 93x3 points, loses all strikes, player 2 successfully steals 279 points and is banked to player 2's score
player 1 answer: lotion
player 1 answer: oil
player 1 answer: wax
player 1 answer: hair med
player 1 answer: hand
player 1 answer: jelly
player 1 answer: shampoo
player 1 answer: soap
player 1 answer: herbs
player 1 answer: other people's hair
player 2 answer: boobs

player 1 score: 287, player 1 strikes left: 0,   player 2 score: 368, player 2 strikes left: 3
```

In your final version, there should be only one print statement that shows the scores after the whole game ends:

```
player 1 score: 287, player 1 strikes left: 0,   player 2 score: 368, player 2 strikes left: 3
```