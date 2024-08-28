from matplotlib import pyplot as plt
from buffon_needle import BuffonNeedleSimulation
import math
import argparse

colors = ['g','y','m']
plt.figure(figsize=(10, 6))

parser = argparse.ArgumentParser(description='Simulate the Dart Board problem.')
parser.add_argument('--pi', '-p', action='store_true', help='Whether to plot the value of pi.')
parser.add_argument('--error', '-e', action='store_true', help='Whether to plot the error of the approximation.')

args = parser.parse_args()

needle_length = 1/2
stripe_width = 1
legend_labels = []

if args.pi:
    for seed in range(3):
        pi_values=[]
        iterations=[]
        for i in range(1, 29):
            n = 2**i
            iterations.append(n)
            buffon = BuffonNeedleSimulation(1/(seed+2), stripe_width, n, 10, 1500*seed)
            pi_values.append(buffon.run_experiment())

        plt.semilogx(iterations, pi_values, linestyle='-', color=colors[seed], label=f'Needle length: {1/(seed+2)}')

    plt.title("Approximation of π with Powers of 2")
    plt.axhline(y=math.pi, color='r', linestyle='--', label='π')
    plt.xlabel("Number of Iterations")
    plt.ylabel("Approximation of π")
    plt.legend()
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
            buffon = BuffonNeedleSimulation(needle_length, stripe_width, n, 10, 1500*seed)
            pi= buffon.run_experiment() 
            error_values.append(abs((math.pi - pi)/math.pi))
        plt.semilogx(iterations, error_values, linestyle='-', color=colors[seed])

    plt.title("Relative error of approximation of π")
    plt.axhline(y=0, color='r', linestyle='--', label='π')
    plt.xlabel("Number of Iterations")
    plt.ylabel("Relative error")
    plt.grid(True)

    # Show the plot
    plt.show()
