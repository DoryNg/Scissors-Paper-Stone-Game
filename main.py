from random import randint
moves = ['scissors', 'paper', 'stone']

while True:
  computer = moves[randint(0,2)]
  player = input('scissors, paper or stone? (or end the game)')
  if player == 'end the game':
    print('you have ended the game')

    break
  if player == computer:
    print('it is a tie!')
  
  elif player == 'scissors':
   if computer == 'paper':
     print('you win!')
   if computer == 'stone':
     print:'sorry, you lose'

  elif player == 'paper':
    if computer == 'scissors':
      print('sorry, you lose')
    if computer == 'stone':
      print('you win!')

  elif player == 'stone': 
    if computer == 'scissors':
      print('you win!')
    if computer == 'paper':
      print('sorry, you lose')
      