import math


def liquid_cv(inlet, outlet, flow, gravity):
    cv = flow * math.sqrt((gravity / (inlet - outlet)))
    return cv


def liquid_flow(cv, inlet, outlet, gravity):
    flow_rate = cv * math.sqrt((inlet - outlet) / gravity)
    return flow_rate


def gas_cv(flow, inlet, outlet, temp, gravity):

    if outlet > inlet / 2:
        delta_p = inlet - outlet
        cv = flow / (22.67 * inlet * (1 - ((2 * delta_p) / (3 * inlet))) * math.sqrt(delta_p / (inlet * gravity * (temp + 460))))

    else:
        cv = flow / (float(0.471) * 22.67 * inlet * math.sqrt(1 / (gravity * (temp + 460))))
    return cv


def gas_flow(cv, inlet, outlet, temp, gravity):
    if outlet > inlet / 2:
        delta_p = inlet - outlet
        flow = cv * 22.67 * inlet * (1 - ((2 * delta_p) / (3 * inlet))) * math.sqrt(delta_p / (inlet * gravity * (temp + 460)))

    else:
        flow = cv * (22.67 * inlet * float(0.471) * math.sqrt(1 / (gravity * (temp + 460))))
    return flow
