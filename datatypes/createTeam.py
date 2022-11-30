team_csk = []
team_rcb = []
team_srh = []
team_lsg = []
team_kkr = []


def create_team(choice, random_name):
    """ Here teams will be created
        if one team is full then it returns some msg
        else player added until team full. """
    success = 0
    match choice:
        case "CSK":
            if len(team_csk) < 3:
                team_csk.append(random_name)
            else:
                success = 1
                print("team full for csk")
        case "RCB":
            if len(team_rcb) < 3:
                team_rcb.append(random_name)
            else:
                success = 1
                print("team full for rcb")
        case "SRH":
            if len(team_srh) < 3:
                team_srh.append(random_name)
            else:
                success = 1
                print("team full for srh")
        case "LSG":
            if len(team_lsg) < 3:
                team_lsg.append(random_name)
            else:
                success = 1
                print("team full for lsg")
        case "KKR":
            if len(team_kkr) < 3:
                team_kkr.append(random_name)
            else:
                success = 1
                print("team full for kkr")
    return success
