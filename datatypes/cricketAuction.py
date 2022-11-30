"""
Here I create a simple cricket auction
first players will be listed for auction
then random player is released to auction
then the player was selecting to one team
if team will be full then the team couldn't
continue auction this process continue to
until all teams should be full.
"""


import random
# from createTeam import create_team, \
# team_rcb, team_srh, team_lsg, team_kkr
from createTeam import create_team
from createTeam import team_csk
from createTeam import team_rcb
from createTeam import team_srh
from createTeam import team_kkr
from createTeam import team_lsg
from constants import QUIT

player_list = []    # list for add players to auction
team_dict = {}      # dictionary for add teams with players it stores tuple of players
# tuple with all teams should be participating auction.
team_names = ("CSK", "RCB", "SRH", "LSG", "KKR")


# here auction will be started
# players will be selected to a team until team would be full
def auction():
    """ Players are ready for auction """
    while player_list:
        random_name = random.choice(player_list)
        choice = random.choice(team_names)
        if create_team(choice, random_name) == 0:
            player_list.remove(random_name)
    team_dict.__setitem__(team_names[0], tuple(team_csk))
    team_dict.__setitem__(team_names[1], tuple(team_rcb))
    team_dict.__setitem__(team_names[2], tuple(team_srh))
    team_dict.__setitem__(team_names[3], tuple(team_lsg))
    team_dict.__setitem__(team_names[4], tuple(team_kkr))


print(" Enter names to add players for auction ")
print(" If you want to Quit please enter ---quit---")
while True:
    name = input()
    if name != QUIT:  # Here QUIT is a constant
        player_list.append(name)
    else:
        break
print(player_list)
auction()


for team_name, team_players in team_dict.items():
    print("players in team ", team_name)
    for player in team_players:
        print(player)
