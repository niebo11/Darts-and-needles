# Darts and needles

In this project we find the codes used to reproduce different experiment for throwing darts and buffon's needle to compute an approximation for pi.

## Requirements

The project and all the experiments have been done using python 3.10.4. And the following libraries are required to reproduce the same results as the owner:

- matplotlib
- numpy
- functools

## How to use

To reproduce the experiments, it is only needed to use the main script. However the plots obtained in the report are using the script `plot_buffon.py` and `plot_dart.py`.

To run an experiment, run the following command in the src folder:

```python
python main.py
```

All parameters are not required because default values are set. But the parameters to modify the experiment are:

- `type` (`t`), the type of experiment to run. Choices are 'dart' or 'buffon'.
- `needle_length` (`nl`), the length of the needle.
- `stripe_width` (`nw`), the width of the stripes.
- `num_tries` (`n`), number of needles or darts to be thrown.
- `plot` (`p`), optional to see animated gif of the simulation.
- `num_stripes` (`ns`), number of stripes to see better plotting of the simulation.
- `seed` (`s`), the seed used to reproduce the experiment.

