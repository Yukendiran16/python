import random
from createTeam import create_team, \
    team_rcb, team_srh, team_lsg, team_kkr
from createTeam import team_csk

player_list = []
team_dict = {}
team_names = ("CSK", "RCB", "SRH", "LSG", "KKR")


def auction():
    while player_list:
        random_name = random.choice(player_list)
        choice = random.choice(team_names)
        create_team(choice, random_name)
        player_list.remove(random_name)
    team_dict.__setitem__(team_names[0], tuple(team_csk))
    team_dict.__setitem__(team_names[1], tuple(team_rcb))
    team_dict.__setitem__(team_names[2], tuple(team_srh))
    team_dict.__setitem__(team_names[3], tuple(team_lsg))
    team_dict.__setitem__(team_names[4], tuple(team_kkr))


print(" Enter names to add players for auction ")
while True:
    name = input()
    if name != "quit":
        player_list.append(name)
    else:
        break
print(player_list)
auction()
print(team_dict)
