# %% [markdown]
# # Systematic Program Design for Python

# %% [markdown]
# ## How To Design Data - htdd and
# ## How to Design Function - htdp

# %%
from typeguard import check_type, TypeCheckError
from typing import List

# %% [markdown]
# ### Simple Atomic Data
# Use simple atomic data when the information to be represented is itself atomic in form, such as the elapsed time since the start of the animation, the x coordinate of a car or the name of a cat.

# %%
# htdp - design recipe for simple atomic data definition

# Example: Time
# Time is Natural
# interpretation: number of clock ticks since start of game

START_TIME = 0
OLD_TIME = 1000


def function_for_time(time: int):
    pass  # replace with your implementation and use time


# Template rules used:
#  - atomic non-distinct: Natural

function_for_time(START_TIME)
function_for_time(OLD_TIME)

# %% [markdown]
# ### Intervals
# Use an interval when the information to be represented is numbers within a certain range. Integer[0, 10] is all the integers from 0 to 10 inclusive; Number[0, 10) is all the numbers from 0 inclusive to 10 exclusive.

# %%
# htdp - design recipe for intervals data definition

# Example: Countdown
# Countdown is Integer[0, 10]
# interpretation: the number of seconds remaining to liftoff

C1 = 10  # start
C2 = 5  # middle
C3 = 0  # end


def function_for_countdown(countdown: int):
    if not (0 <= countdown <= 10):
        raise ValueError("countdown must be in range [0, 10]")
    pass  # # replace with your implementation and use countdown


# Template rules used:
#  - atomic non-distinct: Integer[0, 10]

function_for_countdown(C1)
function_for_countdown(C2)
function_for_countdown(C3)


# %% [markdown]
# ### Enumerations
# Use an enumeration when the information to be represented consists of a fixed number of distinct items, such as colors, letter grades etc. The data used for an enumeration could in principle be anything - strings, integers, images even.

# %%
# htdp - design recipe for Enumeration data definition

# Example: LightState
# LightState is one of:
#  - "red"
#  - "yellow"
#  - "green"
# interpretation: the color of a traffic light


def function_for_light_state(lightstate: str):
    if lightstate == "red":
        pass  # replace with your implementation and use lightstate
    elif lightstate == "yellow":
        pass  # replace with your implementation and use lightstate
    elif lightstate == "green":
        pass  # replace with your implementation and use lightstate
    else:
        raise ValueError("lightstate must be one of 'red', 'yellow', 'green'")


# Template rules used:
#  - one of: 3 cases
#  - atomic distinct: "red"
#  - atomic distinct: "yellow"
#  - atomic distinct: "green"

function_for_light_state("red")
function_for_light_state("yellow")
function_for_light_state("green")

# %% [markdown]
# ### Itemizations Data Types
# An itemization describes data comprised of 2 or more subclasses, at least one of which is not a distinct item. (C.f. enumerations, where the subclasses are all distinct items.) In an itemization the template is similar to that for enumerations: a cond with one clause per subclass. In cases where the subclass of data has its own data definition the answer part of the cond clause includes a call to a helper template, in other cases it just includes the parameter.

# %%
# htdp - design recipe for itemization data definition

from typing import Union

# Example: Bird
# Bird is one of:
#  - False
#  - Number
# interpretation: False means no bird, number is x position of bird

Bird = Union[bool, int]

B1 = False
B2 = 3


def function_for_bird(bird: Bird):
    if bird is False:
        pass  # replace with your implementation
    elif isinstance(bird, int):
        pass  # replace with your implementation and use bird
    else:
        raise ValueError("bird must be False or a integer")


# Template rules used:
#  - one of: 2 cases
#  - atomic distinct: False
#  - atomic non-distinct: Number

function_for_bird(B1)
function_for_bird(B2)


# %% [markdown]
# ### Itemization of Intervals Data Types
#
# A common case is for the itemization to be comprised of 2 or more intervals. In this case functions operating on the data definition will usually need to be tested at all the boundaries of closed intervals and points between the boundaries.

# %%
# htdp - design recipe for itemization of intervals data definition

# Example: Reading
# Reading is one of:
#  - Number > 30
#  - Number in (5, 30]
#  - Number in [0, 5]
# interpretation: distance in centimeters from bumper to obstacle
#    Number > 30    is considered "safe"
#    Number in (5, 30]   is considered "warning"
#    Number in [0, 5]    is considered "dangerous"

R1 = 40
R2 = 0.9


def function_for_reading(reading: int):
    if reading > 30:
        pass  # replace with your implementation and use reading
    elif 5 < reading <= 30:
        pass  # replace with your implementation and use reading
    elif 0 <= reading <= 5:
        pass  # replace with your implementation and use reading
    else:
        raise ValueError("Reading must be an integer and in the expected range")


# Template rules used:
#  one-of: 3 cases
#  atomic non-distinct:  Number > 30
#  atomic non-distinct:  Number in (5, 30]
#  atomic non-distinct:  Number in [0, 5]

function_for_reading(R1)
function_for_reading(R2)

# %% [markdown]
# ## Compound data (structures) Data Types
# Use structures when two or more values naturally belong together. The define-struct goes at the beginning of the data definition, before the types comment.
#
#

# %%
# htdp - design recipe for compound structure data definition

from typing import NamedTuple

# Example: Ball
# Ball is a namedtuple with fields 'x' and 'y'
# interpretation: a ball at position x, y


class Ball(NamedTuple):
    x: int
    y: int


BALL_1 = Ball(10, 10)


def function_for_ball(ball: Ball):
    try:
        check_type(ball, Ball)
    except TypeCheckError as e:
        print(f"{e}")
        raise

    pass  # replace with your implementation and use ball.x and ball.y


# Template rules used:
#  - compound: 2 fields

function_for_ball(BALL_1)

# %% [markdown]
# ## References to other data definitions
# Some data definitions contain references to other data definitions you have defined  non-primitive data definitions). One common case is for a compound data definition to comprise other named data definitions. (Or, once lists are introduced, for a list to contain elements that are described by another data definition. In these cases the template of the first data definition should contain calls to the second data definition's template function wherever the second data appears.

# %%
# htdp - design recipe for function that references other data definition

from typing import NamedTuple

# Example: Game
# Assuming Ball is defined as before
# Game is a namedtuple with fields 'ball' and 'score'
# interpretation: the current ball and score of the game


class Game(NamedTuple):
    ball: Ball
    score: int


GAME_1 = Game(Ball(1, 5), 4)


def function_for_game(game: Game):
    try:
        check_type(game, Game)
    except TypeCheckError as e:
        print(f"{e}")
        raise

    pass  # replace with your implementation and use function_for_ball(game.ball) and game.score


# Template rules used:
#  - compound: 2 fields
#  - reference: ball field is Ball

function_for_game(GAME_1)

# %% [markdown]
# #### Guidance on Data Examples and Function Example/Tests
# For data definitions involving references to non-primitive types the data examples can sometimes become quite long. In these cases it can be helpful to define well-named constants for data examples for the referred to type and then use those constants in the referring from type. For example:

# %%
"""
# Assuming Drop and HEIGHT are defined as before

# ...in the data definition for Drop...
DTOP = Drop(10, 0)            # top of screen
DMID = Drop(20, HEIGHT // 2)  # middle of screen
DBOT = Drop(30, HEIGHT)       # at bottom edge
DOUT = Drop(40, HEIGHT + 1)   # past bottom edge

# ...in the data definition for ListOfDrop...
LOD1 = []
LOD_ALL_ON = [DTOP, DMID]
LOD_ONE_ABOUT_TO_LEAVE = [DTOP, DMID, DBOT]
LOD_ONE_OUT_ALREADY = [DTOP, DMID, DBOT, DOUT]
"""

# %% [markdown]
# ### List
# When the information in the program's domain is of arbitrary size.

# %%
# htdp - design recipe for function that process list of simple data definition

# Example: ListOfStrings
# ListOfStrings is one of:
#  - empty list
#  - a list of strings
# interpretation: a list of strings

LOS_1 = list()
LOS_2 = []
LOS_3 = list((1, 2))
LOS_4 = ["b", "c"]


def function_for_los(los: List[str]):
    if not isinstance(los, List):
        raise ValueError("los must be a list")

    if los == []:
        pass  # BASE CASE
    else:
        for s in los:
            pass  # replace with your implementation for s


# Template rules used:
#  - one of: 2 cases
#  - atomic distinct: empty list
#  - list process: Each s in the ListOfString

function_for_los(LOS_3)
function_for_los(LOS_4)

# %% [markdown]
# ### List of compound data types

# %%
# htdp - design recipe for function that process list of compound data definition

from typing import NamedTuple


# Define the Dot structure
class Dot(NamedTuple):
    x: int
    y: int


# Dot is a namedtuple with Integer x and Integer y
# interpretation: A dot on the screen, w/ x and y coordinates.

D1 = Dot(10, 30)


def function_for_dot(dot: Dot):
    try:
        check_type(dot, Dot)
    except TypeCheckError as e:
        print(f"{e}")
        raise

    pass  # replace with your implementation using dot.x and dot.y


function_for_dot(D1)

# ListOfDot is one of:
#  - empty list
#  - a list of Doct
# interpretation: a list of Dot

LOD1 = list()
LOD2 = []
LOD3 = [Dot(10, 20), Dot(3, 6)]
LOD4 = list((Dot(10, 20), Dot(3, 6)))


def function_for_lod(lod):
    if not isinstance(lod, List):
        raise ValueError("lod must be a list")

    if lod == []:  # BASE CASE
        pass  # replace with your implementation
    else:
        for d in lod:
            function_for_dot(
                d
            )  # replace with your implementation using function_for_dot on each d


# Template rules used:
#  - one of: 2 cases
#  - atomic distinct: empty list
#  - reference: d is Dot
#  - self-reference: each d in the ListOfDot

function_for_lod(LOD1)
function_for_lod(LOD2)
function_for_lod(LOD3)

# %% [markdown]
# ### A list of lists of compound data types
#

# %%
# htdp - design recipe for function that process a list of lists of compound data definition

from typing import List

ListOfLists = List[List[Dot]]


def function_for_lol(lol: ListOfLists):
    if not isinstance(lol, List):
        raise ValueError("lol must be a list")

    if lol == []:  # BASE CASE
        pass  # replace with your implementation
    else:
        for l in lol:
            function_for_lod(
                l
            )  # replace with your implementation using function_for_lod on each l
