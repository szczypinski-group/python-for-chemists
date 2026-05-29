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
    # Spectrum analysis exercise

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


@app.cell
def _():
    import numpy as np

    def load_data(
        file_path 
    ):
        """Load data from OceanOptics Maya spectrometer.
    
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
        
        """

        with open(file_path, "r") as f:
            start_data = ">>>>>Begin Processed Spectral Data<<<<<"
            line = 1
            while True:
                if f.readline().strip() == start_data:
                    break
                line += 1

        # Load data from file
        data = np.genfromtxt(file_path, skip_header=line, skip_footer=1)
        wavelength = data[:, 0]
        signal = data[:, 1]

        return wavelength, signal

    return load_data, np


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

    where $\lambda$ is the wavelength, $A$ is the scale factor, $B$ is the offset, $\lambda_0$ is the centre, and $\omega$ is the width.

    > Use the mathematical functions from `numpy`. They are almost always better than the ones in `math`.
    """)
    return


@app.function
def gaussian(
    x,
    w,
    amp,
    x0,
    off,
):
    """Return Gaussian function values.

    Parameters
    ----------
    x : float | np.ndarray
        Wavelength.
    w : float
        Full width at half maximum.
    amp : float
        Scale factor.
    x0 : float
        Centre position.
    off : float
        Offset.

    Returns
    -------
    float | np.ndarray
        Gaussian function value at `x`.

    """
    return # FIXME: return the value of G(x)


@app.cell
def _(np):
    def gaussian(
        x,
        w,
        amp,
        x0,
        off,
    ):
        """Return Gaussian function values.

        Parameters
        ----------
        x : float | np.ndarray
            Wavelength.
        w : float
            Full width at half maximum.
        amp : float
            Scale factor.
        x0 : float
            Centre position.
        off : float
            Offset.

        Returns
        -------
        float | np.ndarray
            Gaussian function value at `x`.

        """
        return amp * np.exp(-4 * np.log(2) * ((x - x0) / w) ** 2) + off

    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Final plot with residuals
    """)
    return


if __name__ == "__main__":
    app.run()
