import argparse
from dart import Dart
from buffon_needle import BuffonNeedleSimulation


def parser():
    parser = argparse.ArgumentParser(description='Simulate the Buffon Needle problem and the Dart Board problem.')

    # Add arguments
    parser.add_argument('--type', '-t', type=str, choices=['buffon', 'dart'], default='dart', help='The type of experiment to run.')
    parser.add_argument('--needle_length', '-nl', type=float, default=1, help='The length of the needle.')
    parser.add_argument('--stripe_width', '-sw', type=float, default=2, help='The width of the stripes.')
    parser.add_argument('--num_tries', '-n', type=int, default=1000, help='The number of tries to throw/drop the needle/dart.')
    parser.add_argument('--width', '-w', type=float, default=1, help='The width of the dart board.')

    parser.add_argument('--plot', '-p', action='store_true', help='Whether to plot the experiment.')
    parser.add_argument('--num_stripes', '-ns', type=int, default=10, help='The number of stripes.')
    parser.add_argument('--seed', '-s', type=int, default=1000, help='The seed for the random number generator.')   

    args = parser.parse_args()

    return args


def main():
    args = parser()
    if args.type == 'buffon':
        if not args.plot:
            buffon = BuffonNeedleSimulation(args.needle_length, args.stripe_width, args.num_tries, args.num_stripes)
            pi = buffon.run_experiment()
            print(f'Pi is approximately {pi}.')
        else:
            buffon = BuffonNeedleSimulation(args.needle_length, args.stripe_width, args.num_tries, args.num_stripes)
            buffon.animate()


    elif args.type == 'dart':
        dart = Dart(args.width, args.num_tries)
        dart.run_experiment(args.plot)


if __name__ == '__main__':
    main()