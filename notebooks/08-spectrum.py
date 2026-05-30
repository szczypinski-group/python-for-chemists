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
    # Laser spectrum analysis

    In this exercise we will analyse real world data from our 2nd year Physical Chemistry practicals - emission spectrum of a laser. It will combine some elements of the previous workshops. As always, **feel free to experiment** with the code in new Python cells, you can always easily restart the kernel if things go very wrong!

    > This exercise demonstrates how you can write great lab reports as a `marimo` notebook with all **raw data, analysis, and discussion in one place**!
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Loading experimental data

    First, download the experimental data from [here](https://szczypinski-group.github.io/python-for-chemists/notebooks/public/signal.txt) and upload it to your working directory in the browser (you can just drag and drop into the `FILES` tab on the left). Explore the raw file either on your computer, directly in `marimo` or by loading the text and printing it to the screen. You might notice that the file looks more or less like this:

    ```
    SOME LINES OF EXPERIMENTAL DETAILS
    >>>>>Begin Processed Spectral Data<<<<<
    ROWS OF: {wavelength} {intensity}
    >>>>>End Processed Spectral Data<<<<<
    ```

    We can imagine that as part of the experiment you will be analysing lots of similar files like this, where the header with experimental details is of variable length. It is probably worth writing a `load_data()` function that takes as an argument the file path and returns two NumPy arrays: `wavelength` and `intensity`.

    **Useful functions**

    - [`pathlib.Path.read_text()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_text)
    - [`np.genfromtxt()`](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html)
    - [`str.strip()`](https://docs.python.org/3/library/stdtypes.html#str.strip)
    """)
    return


app._unparsable_cell(
    """
    # FIXME: include necessary imports

    def load_data(
        file_path 
    ):
        \"\"\"Load data from OceanOptics Maya spectrometer.

        This function loads the text from the specified file,
        looks at which line the data begins and loads the data
        from that line using `np.genfromtxt()`.

        Parameters
        ----------
        file_path : str | Path
            Path to the data file.

        Returns
        -------
        wavelength : np.ndarray
            Array of wavelengths (nm).

        intensity : np.ndarray
            Array of emission intensity at each wavelength.

        \"\"\"

        with open(file_path, \"r\") as f:
            start_data = \">>>>>Begin Processed Spectral Data<<<<<\"
            # FIXME: write a loop that identifies where the data starts
            # FIXME: the number of header lines should be stored as `line`

        # Load data from file
        data = np.genfromtxt( # FIXME )
        wavelength = # FIXME: load as first column of `data`
        intensity = # FIXME: load as second column of `data`

        return wavelength, intensity
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(load_data):
    def pass_load():
        passed = False

        try:
            wavelength, intensity = load_data("signal.txt")
            if (wavelength[0] == 200.29 and intensity[0] == 5.00 and wavelength[-1] == 1113.04 and intensity[-1] == 0.00):
                passed = True

            if passed:
                return mo.callout("✅ Correct", kind="success")
            else:
                return mo.callout("❌ Not quite.", kind="danger")   

        except Exception as e:
            passed = False
            return mo.callout(f"❌ Python error: {e}.", kind="danger")

    pass_load()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Inspecting the data

    It is always worth plotting the raw data quickly to see if we can identify any general features, such as the overall shape and interesting regions.

    ### Useful functions:
    - [`matplotlib.pyplot.plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
    """)
    return


app._unparsable_cell(
    r"""
    import matplotlib.pyplot as plt

    wavelength, intensity = load_data("signal.txt")

    # We are defining it as a function to avoid variable name clashes
    # But this is not technically necessary - just easier for now.

    def rough_plot(wavelength, intensity):
        fig, ax  = plt.subplots()

        ax.plot(
            # FIXME: plot intensity(wavelength)
        )

        ax.set_xlim([,]) # FIXME: set useful limits

        # FIXME: add labels and legend
        # FIXME: make publication quality (can reuse style)

        return fig

    rough_plot(wavelength, intensity)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Fitting parameters of a Gaussian

    It looks like we have something akin a Gaussian response between 620 and 655 nm. We should use non-linear optimisation to fit a Gaussian to our data and see how it looks.

    Try implementing the following Gaussian definition into Python, so that we can then use SciPy to perform the fitting:

    \[

    G(\lambda) = A \exp \left( -4 \ln2 \left( \frac{\lambda - \lambda_0}{\omega} \right)^2 \right) + B

    \]

    where $\lambda$ is the wavelength, $A$ is the scale factor, $B$ is the offset, $\lambda_0$ is the centre, and $\omega$ is the width. Remember that for `scipy.optimize()` to work well, your first function parameter has to be your independent variable and the remaining parameters will be optimised. The function should return the value of G($\lambda$) had all the other parameters been known.

    > Use the mathematical functions from `numpy`. They are almost always better than the ones in `math`.

    > Remember that entire NumPy arrays can be passed as arguments instead of single numbers, and then the function will return an array of per-element results.
    """)
    return


@app.function
def gaussian(
    x,
    x0,
    amp,
    w,
    off,
):
    """Return Gaussian function values.

    Parameters
    ----------
    x : float | np.ndarray
        Wavelength (nm).
    x0 : float
        Centre position (nm).
    amp : float
        Scale factor (amplitude, au)
    w : float
        Full width at half maximum (nm).
    off : float
        Offset (au).

    Returns
    -------
    float | np.ndarray
        Gaussian function value at `x`.

    """
    # FIXME: return value of G(x, x0, amp, w, off)


@app.cell(hide_code=True)
def _(np):
    def pass_gaussian():
        passed = False

        try:
            input = np.linspace(240, 260, 20)
            output = gaussian(input, 250, 10, 10, 5)
            expected = np.array([ 5.625     ,  6.08651796,  6.77627297,  7.73085349,  8.94823503,
           10.3681358 , 11.86372526, 13.25300655, 14.33212158, 14.92349117,
           14.92349117, 14.33212158, 13.25300655, 11.86372526, 10.3681358 ,
            8.94823503,  7.73085349,  6.77627297,  6.08651796,  5.625     ])

            passed = np.allclose(output, expected)

            if passed:
                return mo.callout("✅ Correct", kind="success")
            else:
                return mo.callout("❌ Not quite.", kind="danger")   

        except Exception as e:
            passed = False
            return mo.callout(f"❌ Python error: {e}.", kind="danger")

    pass_gaussian()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Now it is time to fit the parameters of the Gaussian to our data. It is always good to have an initial guess for the parameter values to help the optimised arrive at the best solution. We do it with parameter `p0` for `curve_fit()` which is a list with values in the same order as they appear in the definition of function we will be fitting. It does not need to be perfect - just sometimes you might end up with numerical instability if the optimiser starts too far off.

    > **Tip**: Notation `*a` means [_unpack_ list](https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments) `a`, i.e. it will pass each element of the list `a` as a separate argument. This can be useful when providing positional arguments. You can do the same with dictionaries (`**dict`) to pass its `key=value` pairs; this is often used for unspecified keyword arguments.

    ### Useful functions

    - [`scipy.optimize.curve_fit()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)
    """)
    return


@app.cell
def _(curve_fit, load_data):
    # FIXME: include necessary import, we want to have curve_fit() available

    def fit_gaussian():
        p0 = [] # FIXME: add initial guess for the parameters
    
        wavelength, intensity = load_data("signal.txt")
    
        p_opt, p_cov = curve_fit() # FIXME: call curve_fit() with correct arguments

        return p_opt, p_cov

    return (fit_gaussian,)


@app.cell(hide_code=True)
def _(fit_gaussian, load_data, np):
    def pass_fitting():
        passed = False

        try:
            p_opt, _ = fit_gaussian()
            wavelength, _ = load_data("signal.txt")
            g_fit = gaussian(wavelength, *p_opt)

            passed = np.isclose(g_fit.max(), 59291.70, atol=10)

            if passed:
                return mo.callout("✅ Correct", kind="success")
            else:
                return mo.callout("❌ Not quite.", kind="danger")   

        except Exception as e:
            passed = False
            return mo.callout(f"❌ Python error: {e}.", kind="danger")

    pass_fitting()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Final plot with residuals

    A good report should include professionally-produced plots. We can easily layer different plots on the same `axes` object in `matplotlib` simply be calling `ax.plot()` multiple times. Your final plot should contain:

    1. Scatter plot of raw data with small dot markers.
    2. Line plot of the fitted Gaussian on top of the raw data.
    3. A dashed vertical line at the maximum of the fitted Gaussian.
    4. Second subplot showing the residuals of your fit.

    And of course should have clear labels!

    ### Useful functions
    - [`matplotlib.pyplot.subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)
    - [`matplotlib.Axes.plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
    - [`matplotlib.Axes.scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html)
    """)
    return


app._unparsable_cell(
    r"""
    def final_plot():
        # Load raw data into np.arrays
        wavelength, intensity = load_data("signal.txt")

        # Modelled data np.array
        g_fit = gaussian(wavelength, *p_opt)
        residuals = # FIXME: calculate the residuals

        # Object-oriented plotting with matplotlib.
        # This demonstrates another approach to plotting.

        # ax1: top plot (raw and modelled data)
        # ax2: bottom plot (residuals)
        # Plots will share x axis and be 3:1 ratio
        fig, (ax1, ax2) = plt.subplots(
            nrows=2,
            ncols=1,
            sharex=True,
            height_ratios=[3, 1], 
        )

        ax1.scatter() # FIXME: plot raw data
        ax1.plot() # FIXME: plot modelled data

        # Useful method to set limits based on values
        # Rather than slicing the original arrays with indices
        ax1.set_xlim([620, 655])

        ax2.plot() # FIXME: plot residuals

        # Save the final plot at publishable resolution
        fig.savefig("laser_emission.png", dpi=300)

        # Save the final plot as vector graphic for future
        fig.savefig("laser_emission.svg", dpi=300)

        return fig

    final_plot()
    """,
    name="_"
)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    The following figure does not conform to the requirements above but is an outcome I would personally be satisfied with in my reports and manuscripts. The whole process was also much more reproducible and robust than if you tried to perform similar fitting and plotting in Excel - and you can just copy the code for your future practicals!
    <img src="public/example_figure.png" width="600" />
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Next steps

    You are now well-equiped to switch all you data analysis needs for laboratory chemistry into Python and `marimo` notebooks. Have a look at the **Advanced Topics and Applications** notebooks from the [Scientific Computing for Chemists with Python](https://weisscharlesj.github.io/SciCompforChemists/notebooks/introduction/intro.html). There are some truly amazing applications of Python for real research chemistry applications: signal analysis, simulations, statistical plotting, automated NMR data analysis, or cheminformatics. Some of them will require a local Python installation (e.g., to use [RDKit](https://www.rdkit.org/docs/index.html)), so we will leave them for you to explore in your spare time!
    """)
    return


if __name__ == "__main__":
    app.run()
