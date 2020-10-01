import time as thetime
from datetime import date, time, datetime

from time import gmtime, strftime
print(strftime("%z", gmtime()))


my_date = date(year=2020, month=2, day=3)

# about to start the game
game_start_time = datetime.now()

# do stuff
thetime.sleep(3.7)
game_end_time = datetime.now()

print(game_start_time)
print(game_end_time)
last_activity = datetime.now()

# When to abandon a game or a play

# def close_stale_games():
#     ''' function that closes stale games '''
#     for game in open_games():
#         if game.last_activity() < (datetime.now() - time(hour: 24)):
#             game.close()

