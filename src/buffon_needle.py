import numpy as np
import random as rd
import math
import  matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class BuffonNeedleSimulation:
    def __init__(self, needle_length: float, stripe_width: float, num_needles: int, n_stripes: int = 5, seed: int = 1000) -> None:
        '''Initializes the Buffon's Needle experiment with the given needle length, stripe width, and number of needles.

        :param needle_length: The length of the needle.
        :type needle_length: float
        :param stripe_width: The width of the stripes.
        :type stripe_width: float
        :param num_needles: The number of needles to drop.
        :type num_needles: int
        :param seed: The seed for the random number generator, defaults to 1000
        :type seed: int, optional
        '''
        np.random.seed(seed)
        rd.seed(seed)   
        self.needle_length = needle_length
        self.stripe_width = stripe_width
        self.num_needles = num_needles
        self.n_stripes = n_stripes
        self.hits = 0
        self.tries = 0

    def init_plot_variables(self):
        """Initializes the variables used for plotting."""
        self.needle_x = []
        self.needle_y = []
        self.colors = []
        self.stripe_height = (self.n_stripes - 1) * self.stripe_width + self.needle_length * 2

    def drop_needles(self):
        """Drop all needles.
        """

        self.center_points = np.random.uniform(0, self.stripe_width / 2, self.num_needles)
        self.angles = np.random.uniform(0, 90, self.num_needles)

        # Check if the needle crosses a line
        self.hits = np.sum(self.center_points <= (self.needle_length / 2) * np.sin(np.radians(self.angles)))
        self.tries = self.num_needles

    def drop_needle_plot(self):
        """Drops a needle for plotting.
        """
        # Randomly choose a position of the needle's center and an angle between 0 and 90 degrees
        center_x = rd.uniform(0, self.stripe_width / 2)
        center_y = self.stripe_height / 2 + rd.choice([1,-1]) * rd.uniform(0, self.stripe_height / 2 - self.needle_length / 2)
        angle = rd.uniform(0, 90)

        side = rd.choice([1, -1])
        stripe = rd.randint(0, self.n_stripes - 1)
        center_plot_x = side * center_x + stripe * self.stripe_width
        

        x1 = center_plot_x + (self.needle_length / 2) * math.sin(math.radians(angle))
        y1 = center_y + (self.needle_length / 2) * math.cos(math.radians(angle))

        x2 = center_plot_x - (self.needle_length / 2) * math.sin(math.radians(angle))
        y2 = center_y - (self.needle_length / 2) * math.cos(math.radians(angle))
        
        self.needle_x.append((x1, y1))
        self.needle_y.append((x2, y2))

        # Check if the needle crosses a line
        if center_x <= (self.needle_length / 2) * math.sin(math.radians(angle)):
            self.colors.append('red')
            self.hits += 1
        else:
            self.colors.append('blue')

        self.tries += 1

    def drop_needle_simulate(self):
        center_x = rd.uniform(0, self.stripe_width / 2)
        angle = rd.uniform(0, 90)

        if center_x <= (self.needle_length / 2) * math.sin(math.radians(angle)):
            self.hits += 1
        self.tries += 1

    def simulate(self):
        for _ in range(self.num_needles):
            self.drop_needle_simulate()

        if self.stripe_width <= self.needle_length:
            raise ValueError("Needle length must be less than gap width")

        # Estimate π using the Buffon's Needle formula
        estimated_pi = (2 * self.needle_length * self.tries) / (self.hits * self.stripe_width)
        print(f"Estimated pi: {estimated_pi:.5f}")
        return estimated_pi
    
    def update(self, frame):
        self.drop_needle_plot()
        estimated_p = self.tries / self.hits if self.hits > 0 else 0

        title = f"Simulation Frame: {frame + 1}\n"
        title += f"Estimated pi: {estimated_p:.5f}, nº hits: {self.hits}, nº tries: {self.tries}\n"
        subtitle = f"Needle Length: {self.needle_length}, Gap Width: {self.stripe_width}, Number of Needles: {self.num_needles}"
        self.ax.set_title(f"{title}{subtitle}")
        plt.plot(
            [self.needle_x[frame][0], self.needle_y[frame][0]],
            [self.needle_x[frame][1], self.needle_y[frame][1]],
            c=self.colors[frame]
        )

    def init(self):
        self.init_plot_variables()
        self.ax.clear()
        self.ax.set_xlim(0 - self.needle_length, self.stripe_width * (self.n_stripes - 1) + self.needle_length)
        for stripe in range(self.n_stripes):
            self.ax.axvline(x=stripe * self.stripe_width, c='black')
        self.ax.set_ylim(0, self.stripe_height)

    def animate(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.init()
        if self.num_needles > 1000:
            interval = 10
        elif self.num_needles > 100:
            interval = 100
        else:
            interval = 1000
        
        ani = FuncAnimation(self.fig, self.update, frames=self.num_needles, interval=interval, repeat=False)

        plt.show()

    def run_experiment(self):
        """Runs the experiment.
        """
        self.drop_needles()
        estimated_pi = self.tries / self.hits if self.hits > 0 else 0
        #print(f"Estimated pi: {estimated_pi:.5f}")
        return estimated_pi
