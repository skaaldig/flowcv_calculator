import math


def liquid_cv(inlet, outlet, flow, gravity):
    cv = flow * math.sqrt((gravity / (inlet - outlet)))
    return cv
