# we use enum to define constent or unique  value

from enum import Enum


class State (Enum):
    Inactice = 0
    Active = 1
    Mid = 12


print(State.Active.value)
# it will give you value of state   [<State.Inactice: 0>, <State.Active: 1>]
print(list(State))  # [<State.Inactice: 0>, <State.Active: 1>]
print(len(State))  # it will give you value of State  2
