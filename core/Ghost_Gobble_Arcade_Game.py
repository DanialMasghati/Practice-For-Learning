# def eat_ghost(pac, enm):
#     # pac = False
#     if pac == True:
#         return True
#     else:
#         return False


# def score(power, dot):
#     if power == True and dot == True:
#         return True


# def lose(pac, power):
#     if pac == True and power == True:
#         return True
#     elif pac == True and power == False:
#         return False
def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    return (not power_pellet_active) and touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)

# print(eat_ghost(True, True))
# print(score(True, True))
# print(lose(True, False))
