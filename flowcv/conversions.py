
def pressure_converter(pressure, unit):
    to_psi = {
        "kpa": 6.894757293168361,
        "bar": 14.503773800722,
        "mpa": 145.03773773
    }
    if unit == "kpa":
        return pressure / to_psi[unit]
    return pressure * to_psi[unit]


def flow_converter(flow, unit):
    to_gpm = {
        "lph": 0.00440287,
        "lpm": 0.26417287472922,
        "lps": 15.850372483753,
        "m3hr": 4.402881245487
    }
    return flow * to_gpm[unit]
