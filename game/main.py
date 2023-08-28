import random
def show_game_state(elpc,elus):
      print(f'Computadora elige {elpc} y tú eliges {elus}.')

def play_round(user, pc, user_win, pc_win):
  if user == pc:
    show_game_state(pc,user)
    print("Es un EMPATE!")
  elif (user == 'piedra' and pc == 'tijera') or (user == 'tijera' and pc == 'papel') or (user == 'papel' and pc  == 'piedra'):
    show_game_state(pc,user)
    print('USUARIO GANA!')
    user_win += 1
  else:
    show_game_state(pc,user)
    print('LA COMPUTADORA GANA!')
    pc_win += 1
  return user_win, pc_win

def run_game():
  options = ('piedra', 'papel', 'tijera')
  user_win = 0
  pc_win = 0
  round = 0
  
  while (user_win < 3) and (pc_win < 3):
    player = input("Elige piedra, papel o tijera... ")
    player = player.lower()
    computer = random.choice(options)
  
    if player in options:
      round += 1
      print('**' * 5)
      print('ROUND ', round)
      print('**' * 5)
      
      user_win, pc_win = play_round(player, computer, user_win, pc_win)
      print('USER ', user_win, ' - ', pc_win, ' PC')
    else:
      print("Elegiste mal, intenta de nuevo")
      continue

run_game() 