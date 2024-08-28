import random as rd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from functools import partial
from matplotlib.animation import FuncAnimation
import numpy as np

class Dart:
    x: float
    width: float

    def __init__(self, width: float, num_darts: int, seed: int = 1000) -> None:
        '''Initializes the dart board with the given width and height.

        :param width: The width of the dart board.
        :type width: float
        :param height: The height of the dart board.
        :type height: float
        :param seed: The seed for the random number generator, defaults to 1000
        :type seed: int, optional
        '''
        np.random.seed(seed)
        self.num_darts = num_darts
        self.x = -width/2
        self.width = width
    
    def throw_darts(self) -> list[tuple[float, float]]:
        '''Simulates the throwing of n darts at the dart board.

        :param n: The number of darts to throw.
        :type n: int
        '''
        self.x_points = np.random.uniform(self.x, self.x + self.width, self.num_darts)
        self.y_points = np.random.uniform(self.x, self.x + self.width, self.num_darts)

        distance = self.x_points**2 + self.y_points**2
        self.inside_circle = (distance <= (self.width/2)**2).astype(int)

    def estimate_pi(self) -> float:
        '''Estimates the value of pi using the Monte Carlo method.
        
        :return: The estimated value of pi.
        :rtype: float
        '''
        return 4 * np.sum(self.inside_circle) / len(self.inside_circle)

    def draw_figure(self):
        '''Draws the dart board.
        
        :return: None
        '''
        self.fig, self.ax = plt.subplots()

        square = patches.Rectangle(
            (self.x, self.x),
            self.width,
            self.width,
            linewidth=2,
            edgecolor='b',
            facecolor='none'       
        )
        
        circle = patches.Circle(
            (0, 0),
            radius=self.width/2,
            linewidth=2,
            edgecolor='b',
            facecolor='none'       
        )

        self.ax.add_patch(square)
        self.ax.add_patch(circle)

        self.ax.set_xlim(self.x - 0.1, self.x + self.width + 0.1)
        self.ax.set_ylim(self.x - 0.1, self.x + self.width + 0.1)

        plt.gca().set_aspect('equal', adjustable='box')
    
    def update(self, frame):
        self.ax.set_title(f'Darts: {frame+1}/{len(self.x_points)}\nEstimated Pi: {4 * np.sum(self.inside_circle[:frame+1]) / (frame+1):.5f}')
        self.ax.plot(self.x_points[frame], self.y_points[frame], 'r+')
        return self.ax
    
    def draw_points(self):
        self.draw_figure()
        self.frame_counter = self.ax.text(
            self.x + self.width + 0.2,
            self.x + self.width,
            '',
            fontsize=12,
            ha='center',
            va='center'
        )
        ani = FuncAnimation(
            self.fig,
            partial(self.update),
            frames=len(self.x_points),
            blit=True,
            repeat=False
        )

        plt.show()

    def run_experiment(self, plot):
        """Runs the experiment.

        :param plot: Whether to plot the experiment.
        :type plot: bool
        """
        self.throw_darts()
        estimated_pi = self.estimate_pi()
        print(f"Estimated pi: {estimated_pi:.5f}")

        if plot:
            self.draw_points()
