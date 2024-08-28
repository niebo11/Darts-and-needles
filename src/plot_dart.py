from matplotlib import pyplot as plt
from dart import Dart
import math
import argparse
import tabulate

colors = ['g','y','m']
plt.figure(figsize=(10, 6))

parser = argparse.ArgumentParser(description='Simulate the Dart Board problem.')
parser.add_argument('--pi', '-p', action='store_true', help='Whether to plot the value of pi.')
parser.add_argument('--error', '-e', action='store_true', help='Whether to plot the error of the approximation.')
parser.add_argument('--table', '-t', action='store_true', help='Whether to print the table of values.')
args = parser.parse_args()

if args.pi:
    for seed in range(3):
        pi_values=[]
        iterations=[]
        for i in range(1, 29):
            n = 2**i
            iterations.append(n)
            dart = Dart(1, n, 1500*seed)
            dart.throw_darts()
            pi_values.append(dart.estimate_pi())
        plt.semilogx(iterations, pi_values, linestyle='-', color=colors[seed])

    plt.title("Approximation of π with Powers of 2")
    plt.axhline(y=math.pi, color='r', linestyle='--', label='π')
    plt.xlabel("Number of Iterations")
    plt.ylabel("Approximation of π")
    plt.grid(True)

    # Show the plot
    plt.show()

elif args.error:
    for seed in range(3):
        error_values=[]
        iterations=[]
        for i in range(1, 29):
            n = 2**i
            iterations.append(n)
            dart = Dart(1, n, 1500*seed)
            dart.throw_darts()
            pi = dart.estimate_pi()
            error_values.append(abs((math.pi - pi)/math.pi))
        plt.semilogx(iterations, error_values, linestyle='-', color=colors[seed])

    plt.title("Relative error of approximation of π")
    plt.axhline(y=0, color='r', linestyle='--', label='π')
    plt.xlabel("Number of Iterations")
    plt.ylabel("Relative error")
    plt.grid(True)

    # Show the plot
    plt.show()

elif args.table:
    error_values=[]
    n=100
    for seed in range(100):
        dart = Dart(1, n, seed)
        dart.throw_darts()
        pi = dart.estimate_pi()
        error_values.append(abs((math.pi - pi)/math.pi))

    list = zip(range(100), error_values)
    headers = ["Seed", "Relative error"]
    print(tabulate.tabulate(list, headers, tablefmt="latex"))