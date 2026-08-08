# Landscape Estimator

A command line tool I built when I was doing landscaping work. It asks for the square footage of the area, the depth in inches, your material cost per cubic yard, and your labor rate, then prints a job summary with material cost, labor hours, and a grand total.

The math is straightforward but having it in a script meant I never had to do the conversion by hand on the job site again. Cubic yards round up, because you always want more than less. Labor is a flat half hour per cubic yard, which was a decent rule of thumb for the crews I worked with and is the one number here you'd want to tune to your own.

Built with Python (`estimator.py`), standard library only. Run it with `python3 estimator.py`.
