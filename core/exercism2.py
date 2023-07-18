# import lasagna
# lasagna.EXPECTED_BAKE_TIME
# TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40

# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.


def bake_time_remaining(n):
    bake_time_remaining = EXPECTED_BAKE_TIME - n
    return bake_time_remaining


# print(bake_time_remaining(30))


# TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(n):
    PREPARATION_TIME = 2*n
    return PREPARATION_TIME

# TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)


def elapsed_time_in_minutes(x, y):
    z = preparation_time_in_minutes(x)+bake_time_remaining(y)
    return z


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
