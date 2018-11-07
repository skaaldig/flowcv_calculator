import argparse
from .formulas import liquid_cv
from .conversions import flow_converter, pressure_converter


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-medium', choices=['liquid', 'gas'],
    )
    parser.add_argument(
        '-calc', choices=['cv', 'flow_rate']
    )
    parser.add_argument(
        '--pressure_unit', choices=['psi', 'kpa', 'bar', 'mpa'],
        default='psi'
    )
    parser.add_argument(
        '-inlet', type=float,
        help="inlet pressure of your application"
    )
    parser.add_argument(
        '-outlet', type=float,
        help="outlet pressure of your application"
    )
    parser.add_argument(
        '--flow_unit', choices=['gpm', 'lph', 'lpm', 'lps', 'm3hr'],
        default='gpm'
    )
    parser.add_argument(
        '-flow_rate', type=float
    )
    parser.add_argument(
        '-gravity', type=float
    )

    args = parser.parse_args()

    # make any conversions:
    if args.pressure_unit != 'psi':
        inlet = pressure_converter(args.inlet, args.pressure_unit)
        outlet = pressure_converter(args.outlet, args.pressure_unit)
    else:
        inlet, outlet = args.inlet, args.outlet

    if args.flow_unit != 'gpm':
        flow = flow_converter(args.flow_rate, args.flow_unit)
    else:
        flow = args.flow_rate

    # calculate flow or cv
    if args.medium == 'liquid' and args.calc == 'cv':
        cv = liquid_cv(inlet, outlet, flow, args.gravity)
        return cv


if __name__ == '__main__':
    main()
