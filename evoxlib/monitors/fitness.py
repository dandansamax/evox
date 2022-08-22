import jax.numpy as jnp
import bokeh
from bokeh.plotting import figure, show
from bokeh.models import Spinner
from evoxlib.core.module import Module


class FitnessMonitor:
    def __init__(self, n_objects=1):
        # single object for now
        assert n_objects == 1
        self.n_objects = n_objects
        self.history = []
        self.min_fitness = float("inf")

    def update(self, F):
        self.min_fitness = min(self.min_fitness, jnp.min(F).item())
        self.history.append(self.min_fitness)

    def show(self):
        plot = figure(
            title="Fitness - Iteration",
            x_axis_label="Iteration",
            y_axis_label="Fitness",
        )
        fitness_line = plot.line(
            list(range(len(self.history))), self.history, line_width=2
        )
        spinner = Spinner(
            title="Line Width",
            low=0,
            high=60,
            step=1,
            value=fitness_line.glyph.line_width,
            width=64,
        )
        spinner.js_link("value", fitness_line.glyph, "line_width")
        layout = bokeh.layouts.layout(
            [
                [spinner],
                [plot],
            ]
        )
        show(layout)

    def get_min_fitness(self):
        return self.min_fitness