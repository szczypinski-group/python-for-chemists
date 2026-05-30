# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.23.8"
app = marimo.App()

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Numerical and scientific Python

    ## Numerical Python (NumPy)

    In this workshop we will learn the basics of [NumPy](https://numpy.org/). There aren't really any exercises here, it's more a selection of examples that I wish someone showed me earlier in my life. Remember that you can play around and explore different parameters in the notebook - you can just restart it if you break too much! You can also hover over methods with your mouse to get the docstrings (`numpy` and `scipy` are very thorough) or use `help(function)`. I have also included links to the documentation throughout. We will have a real exercise in another workshop!

    So far we have been performing some mathematical operations and using lists - but NumPy is much more efficient at these tasks. It introduces n-dimensional arrays (`ndarray`), has better numerical accuracy, is faster, and automates a lot of array-based operations that would otherwise require lots of `for` loops.

    To use NumPy we need to import it, and the convention is to do it using the `np` alias.
    """)
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(np):
    # Python way
    print("-" * 50)
    print("Looping over lists in Python")
    print("-" * 50)
    _nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    _output = []

    for _x in _nums:
        _output.append(2*_x)
    print(_output)

    # NumPy way
    print("-" * 50)
    print("Applying multiplication to a NumPy array")
    print("-" * 50)
    _arr = np.arange(10)
    print(2 * _arr)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### NumPy array basics

    We can create arrays in many different ways. Most common ones are included here:
    """)
    return


@app.cell
def _(np):
    # From lists
    np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    return


@app.cell
def _(np):
    # From lists with syntactic sugar
    np.array([x for x in range(10)])
    return


@app.cell
def _(np):
    # As a range with np.arange(stop)
    np.arange(10)
    return


@app.cell
def _(np):
    # As a range with np.arange(start, stop, step)
    np.arange(2, 40, 3)
    return


@app.cell
def _(np):
    # Evenly spaced with np.linspace(start, stop, size)
    # In this case: 8 numbers from 0 to 20 (inclusive).
    np.linspace(0, 20, 8)
    return


@app.cell
def _(np):
    # Evenly spaced with np.logspace(start, stop, size)
    # In this case: 8 numbers from 10^0 to 10^6.
    np.logspace(0, 6, 8, base=10)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    We mentioned that the arrays are n-dimensional. Let's create a simple empty 2D array with three rows and four columns.
    """)
    return


@app.cell
def _(np):
    np.zeros((3,4))
    return


@app.cell
def _(np):
    np.zeros((2,3,4))
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Finally, we can perform a range of array operations that we are familiar with from introductory maths courses.
    """)
    return


@app.cell
def _(np):
    array_1D = np.arange(20)
    return (array_1D,)


@app.cell
def _(array_1D):
    # Turn a 1D array into a 2D array
    array_2D = array_1D.reshape(4,5)
    print(array_2D)
    return (array_2D,)


@app.cell
def _(array_2D):
    # Reshape the data into a different format
    # This is done on per-element basis
    array_2D.reshape(5,4)
    return


@app.cell
def _(array_2D):
    # Transpose of array_2D
    array_2D.T
    return


@app.cell
def _(array_2D):
    # Per-element multiplication made easy
    # Imagine the nested for loops!
    print(5 * array_2D.T)
    return


@app.cell
def _(array_2D):
    try:
        array_2D * array_2D.T
    except ValueError as e:
        print(f"This makes no sense - {e}")
    return


@app.cell
def _(array_2D):
    # But we could do matrix multiplication!
    # The operator for it is "@"
    array_2D @ array_2D.T
    return


@app.cell
def _(array_2D):
    # Flatten back into an 1D array
    array_2D.flatten()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Array creation from CSV

    Among the most useful array creation methods when dealing with scientific equipment is generating them from CSV files. Let's try to load some CSV data from an example kinetic measurement in our catalyst screening campaign.
    """)
    return


@app.cell(hide_code=True)
def _():
    def gen_example_kinetics_csv(): 
        kinetics_csv = """# Reaction Run: Catalyst_A_Trial_1
    # Solvent: EtOAc, Temp: 25C
    Time_min,Absorbance,Ref_Absorbance
    0.0,0.000,0.010
    1.0,0.150,0.011
    2.0,0.280,0.009
    3.0,,0.010
    4.0,0.480,0.012
    5.0,0.550,0.011"""

        with open("kinetics_data.csv", "w") as f:
            f.write(kinetics_csv)

    gen_example_kinetics_csv()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    The useful overall syntax is:

    ```python
    data = np.genfromtxt(
        FILE_PATH,
        delimiter=",",
        skip_header=NUMBER_OF_LINES_TO_SKIP,
        filling_values=VALUE_IF_MISSING
    )
    ```

    In our case we do have some missing values, let's fill them with an `np.nan` (_not a number_). We also have three lines of a header that just describes what the run was.
    """)
    return


@app.cell
def _(np):
    def kinetics_array():
        data = np.genfromtxt(
            "kinetics_data.csv",
            # COMPLETE HERE
        )

        return data

    return (kinetics_array,)


@app.cell(hide_code=True)
def _(kinetics_array, np):
    genfromtxt_pass = False
    genfromtxt_result = np.array(([[0.   , 0.   , 0.01 ],
           [1.   , 0.15 , 0.011],
           [2.   , 0.28 , 0.009],
           [3.   ,   np.nan, 0.01 ],
           [4.   , 0.48 , 0.012],
           [5.   , 0.55 , 0.011]])
    )

    try:
        genfromtxt_pass = np.allclose(
            kinetics_array(),
            genfromtxt_result,
            equal_nan=True
        )

    except Exception:
        genfromtxt_pass = False

    if genfromtxt_pass:
        genfromtxt_feedback = mo.callout("✅ Correct!", kind="success")
    else:
        genfromtxt_feedback = mo.callout("❌ Not quite.", kind="danger")

    genfromtxt_feedback
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Indexing NumPy arrays

    This gets slightly more complicated than simple list indexing - after all, we are working in multiple dimensions.

    It is trivial in the 1D case, as we can do it the same way we did with lists. Note that the return value here is of the `np.int64()` type - this is slightly different from the built-in Python integer, but we don't need to worry about it.
    """)
    return


@app.cell
def _(array_1D):
    array_1D[4]
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    For 2D (and more), we address the elements of the row. Or we can combine the index in the format of `[row, column]`.
    """)
    return


@app.cell
def _(array_2D):
    print(array_2D)
    return


@app.cell
def _(array_2D):
    # Fourth row of array_2D
    array_2D[3]
    return


@app.cell
def _(array_2D):
    # Second element of the fourth row
    array_2D[3][1]
    return


@app.cell
def _(array_2D):
    # Or with a shorthand notation
    array_2D[3, 1]
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    We can also use the `:` slicing opperator to access different subsections of the array. Those are a bit confusing to me, so play around to get an idea yourself!
    """)
    return


@app.cell
def _(array_2D):
    print(array_2D)
    print(f"This array is of shape {array_2D.shape}.")
    return


@app.cell
def _(array_2D):
    # Elements idx 1, 2, 3 of row idx 2.
    array_2D[2, 1:4]
    return


@app.cell
def _(array_2D):
    # All elements of rows from idx 1 to the end.
    array_2D[1:, :]
    return


@app.cell
def _(array_2D):
    # Just third column
    array_2D[:, 2]
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Array methods

    There is a range of useful methods you can perform on NumPy arrays - such us different statistics or shape information. Generally, there probably exist functions for simple array operations that you do not need to implement yourself!

    Check out [NumPy User Guide](https://numpy.org/doc/stable/user/index.html) for more.
    """)
    return


@app.cell
def _(array_2D):
    print(f"The array ranges from {array_2D.min()} to {array_2D.max()} with a mean value of {array_2D.mean()}.")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Random numbers

    Sometimes in scientific computing we need random numbers. Often we would do it to simulate noise in instrument measurements. We will explore that a bit more in the plotting workshop, but let's get the basics of it right.

    Computers **cannot** generate random numbers. They are always generated based on some (typically very complex) algorithm. To ensure reproducibility between experiments, it is good practice to have a fixed _random seed_ - a value that "seeds" our pseudo-random number generator and yields the same "random" results every time.

    In NumPy, we do it with:

    ```python
    import numpy as np

    rng = np.random.default_rng(seed=SEED)
    ```

    Then, there is a variety of distributions that NumPy can draw from  - more details are in their [documentation](https://numpy.org/doc/stable/reference/random/generator.html). Commonly, we would try to get uniformly or normally distributed random numbers.

    ```python

    # Array of N floats, between [0,1)
    random_float = rng.random(size=N)

    # Array of N uniformlly-distributed integers between [LOW, HIGH)
    random_int = rng.integer(low=LOW, high=HIGH, size=N)

    # Array of N uniformlly-distributed floats between [LOW, HIGH)
    random_float2 = rng.uniform(low=LOW, high=HIGH, size=N)

    # Array of N normally-distributed floats between [LOW, HIGH)
    # Centred at MEAN with std. dev. of WIDTH
    random_normal = rng.normal(loc=MEAN, scale=WIDTH, size=None)
    ```

    In the following example we will use the current timestamp (seconds since 00:00:00 UTC on 1st January 1970) - a common way in computing applications. Let's imagine we are trying to simulate noise coming from pixels on a 100x100 CCD detector: that should follow the **Poisson distribution**.
    """)
    return


@app.cell
def _(np):
    from datetime import datetime

    # Using datetime to get the timestamp.
    current_seed = int(datetime.now().timestamp())
    print(f"Random seed is {current_seed}")

    # Creating the random number generator (rng).
    rng = np.random.default_rng(seed=current_seed)

    # Generating detector noise.
    ccd_noise = rng.poisson(lam=2, size=(100,100))

    print(f"We created array of size {ccd_noise.shape}.")
    print(ccd_noise)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Scientific Python (SciPy)

    The power and widespread adoption of Python in scientific computing comes from the libraries available out there. Most important of those is [SciPy](https://scipy.org/) - it is writen on top of NumPy and provides high-level algorithms for maths, science, and engineering. They are highly optimised and - let's be honest - most likely better written than whatever you or I can come up with.

    > **Take home message**: what you need to code probably already exist. Check [SciPy Documentation](https://docs.scipy.org/doc/scipy/tutorial/index.html#user-guide) first to save you days of scripting!

    Some of the examples here might _appear_ more advanced. But you will get good grasp of them when you apply it to some real data!

    ### Constants

    SciPy comes with a very wide [range of constants](https://docs.scipy.org/doc/scipy/reference/constants.html#module-scipy.constants), coded in with a high-level of precision.
    """)
    return


@app.cell
def _():
    import scipy

    # No more manual typing!
    print(f"Speed of light: {scipy.constants.c} m/s")
    print(f"Planck constant: {scipy.constants.h} J s")
    print(f"Molar gas constant: {scipy.constants.R} J/(mol K)")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Curve fitting

    > We will do more about plotting in the next notebook, so here just execute those cells for visualisation.

    The [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html) is a library you will probably use most for any physical (and organic!) labs. It can take raw data and finds the best parameters for your model. You no longer need to derive linear relationships and trasform your data for equations that are difficult to fit by hand. We will use it a lot in the "hands on" workshops.

    To use the `curve_fit()` function we need to first define our model function (what we believe happens mathematically). The first argument of that function is our $x$ data; the return value should be the $y$ data. SciPy will then fit the other arguments as parameters to give us the best fit.

    In this example, we will find a first-order rate constant from a simulated kinetics experiment.
    """)
    return


@app.cell(hide_code=True)
def _(np):
    def generate_kinetics():
        t_data = np.linspace(0, 10, 30)

        A0_true = 1.0  
        k_true = 0.45 

        rng = np.random.default_rng(seed=42)
        noise = rng.normal(0, 0.03, size=t_data.size)

        # [A] = [A]0 * exp(-kt)
        abs_data = A0_true * np.exp(-k_true * t_data) + noise

        return t_data, abs_data

    time_data, example_kinetics_data = generate_kinetics()
    print(example_kinetics_data)
    return example_kinetics_data, time_data


@app.cell
def _(example_kinetics_data, np, time_data):
    from scipy.optimize import curve_fit

    def first_order_decay(time, initial_conc, k):
        return initial_conc * np.exp(-k * time)

    # popt contains the optimised parameters [initial_conf, k]
    # pcov contains the covariance matrix

    popt, pcov = curve_fit(
        first_order_decay,
        time_data, # 30 measurements within 10 minutes
        example_kinetics_data # from previous cell (with noise)
    )

    print(f"Calculated Rate Constant (k): {popt[1]:.4f}")
    return (popt,)


@app.cell(hide_code=True)
def _(example_kinetics_data, np, popt, time_data):
    import matplotlib.pyplot as plt

    # Extract optimized parameters
    a0_opt, k_opt = popt

    # Generate a smooth curve for the fit line
    t_smooth = np.linspace(0, 10, 100)
    abs_fit = a0_opt * np.exp(-k_opt * t_smooth)

    # Calculate the half-life for the legend
    half_life = np.log(2) / k_opt

    # Create the plot
    plt.figure(figsize=(8, 5))

    # Plot noisy experimental data as dots
    plt.scatter(time_data, example_kinetics_data, color="black", alpha=0.6, label="Experimental Data")

    # Plot the optimized theoretical fit as a solid line
    plt.plot(t_smooth, abs_fit, color="red", linewidth=2, 
             label=fr"Fit ($k$ = {k_opt:.3f} min$^{{-1}}$)")

    # Add a horizontal/vertical line to show the half-life visually (optional but cool)
    plt.axvline(half_life, color="green", linestyle="--", alpha=0.3, label=fr"Half-life ($t_{{1/2}}$ = {half_life:.2f} min)")

    # Formatting
    plt.title("First-order kinetics")
    plt.xlabel("Time / min")
    plt.ylabel("[A] / M")
    plt.legend()
    plt.grid(True, alpha=0.2)
    plt.show()
    return (plt,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Signal processing

    The [`scipy.signal`](https://docs.scipy.org/doc/scipy/reference/signal.html) module helps us with general processing of real-world data, such as peak finding or noise filtering.

    Let's use this module to identify where the peak is in a simulated HPLC chromatogram trace. Note that all "indices" returned by those functions refer to the **position of the element within the array** rather than to the specific value. So we still need to find the time or absorbance that those indices correspond to.
    """)
    return


@app.cell(hide_code=True)
def _(np):
    def generate_chromatography():
        time_trace = np.linspace(0, 5, 1000)

        center = 3.5
        width = 0.1
        height = 1.2
        peak = height * np.exp(- (time_trace - center)**2 / (2 * width**2))

        rng = np.random.default_rng(seed=123)
        baseline_drift = 0.01 * time_trace  # The signal slowly climbs
        noise = rng.normal(0, 0.02, size=time_trace.size)

        intensity_trace = peak + baseline_drift + noise

        return time_trace, intensity_trace

    hplc_time, hplc_trace = generate_chromatography()
    print(hplc_trace)
    return hplc_time, hplc_trace


@app.cell
def _(hplc_time, hplc_trace):
    from scipy.signal import find_peaks, peak_widths

    # Finding the peak in hplc_trace
    indices, properties = find_peaks(
        hplc_trace,
        height=1, # minimum peak height
        prominence=0.2 # prominence over baseline
    )
    peak_time = hplc_time[indices[0]]
    peak_height = properties['peak_heights'][0]

    # Finding the LHS and RHS of the peak (for integrals)
    widths, width_heights, left_ids, right_ids = peak_widths(
        hplc_trace,
        indices,
        rel_height=0.9
    )

    # peak_widths() returns arrays of interpolated indices
    # those are floats - need to convert them to integers
    lhs = int(left_ids[0])
    rhs = int(right_ids[0])

    left_time = hplc_time[lhs]
    right_time = hplc_time[rhs]
    return left_time, lhs, peak_height, peak_time, rhs, right_time


@app.cell(hide_code=True)
def _(
    hplc_time,
    hplc_trace,
    left_time,
    peak_height,
    peak_time,
    plt,
    right_time,
):
    plt.figure(figsize=(8, 4))
    plt.plot(hplc_time, hplc_trace, color="black", alpha=0.6, label="HPLC Signal")

    # Mark the found peak with red 'x' marks
    plt.plot(peak_time, peak_height, "x", color="red", markersize=10, label="Peak centre")

    plt.plot(left_time, 0.1, "*", color="blue", markersize=10, label="Peak limits")
    plt.plot(right_time, 0.1, "*", color="blue", markersize=10)

    # Label the peaks with their retention times
    plt.title("Automated Peak Detection")
    plt.xlabel("Retention Time / min")
    plt.ylabel("Absorbance / AU")
    plt.legend()
    plt.show()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Integration

    The [`scipy.integrate`](https://docs.scipy.org/doc/scipy/reference/integrate.html) module provides several ways for numerical integration Let's continue with our example and integrate between the identified left- and right-hand side of the HPLC peak.
    """)
    return


@app.cell
def _(hplc_time, hplc_trace, lhs, rhs):
    from scipy.integrate import trapezoid

    # Simple command to integrate a slice of the data
    peak_area = trapezoid(
        y=hplc_trace[lhs:rhs],
        x=hplc_time[lhs:rhs]
    )

    print(
        "Integral of the absorbance between "
        f"{hplc_time[lhs]:.2f} and {hplc_time[rhs]:.2f} min "
        f"is {peak_area:.4f}."
    )
    return


if __name__ == "__main__":
    app.run()
