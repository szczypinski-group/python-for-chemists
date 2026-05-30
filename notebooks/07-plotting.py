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
    # Plotting with Python

    In this workshop we will look a bit more into [`matplotlib`](https://matplotlib.org/) - the most widely used library for creating visualisations in Python. It has long history and hence some quirks with it. The interface has changed quite a bit in the recent years to make it more [_object-oriented_](https://en.wikipedia.org/wiki/Object-oriented_programming) - so we will only use this more "modern" approach to plotting. This might feel technical as you're reading through but will make it easier for your to understand how to change different plot elements in the future.

    Professional looking plots can really elevate your reports and - in the future - manuscripts. With `matplotlib` you need to put a little bit of effort to develop your style but then it pays off.  In professional settings, a plot is the best way to represent your data and a necessary artifact of research.

    We will learn how to make plots that are:

    1. **Legibile**: when printed and on screen
    2. **Reproducible**: generated programmatically from the data
    3. **Accessible**: using colour-blind-friendly palettes
    4. **Consistent**: showing your trademark style
    5. **Standardised**: following chemistry conventions
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Basic `matplotlib` structure

    In `matplotlib` we build up the elements on a canvas. We have two major objects to interact with:

    - **the figure** (`fig`): this is the canvas; it controls the size, the background,  final export etc.
    - **the axes**(`ax`): this is the actual drawing area; you can have many axes in one figure (think of subplots) and it controls elements related to the plot itself.
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np

    def basic_plot():
        # Lets get some simple data
        rng = np.random.default_rng(seed=2025)
        x = np.linspace(0, 10, 20)
        y = 3 * x + 15 + rng.normal(loc=0, scale=2, size=len(x))

        # Initialise the figure and the axes
        # figsize=(width, height) in inches
        fig, ax = plt.subplots(figsize=(6, 4))

        # Draw scatter plot on the axes
        # In black with circle markers
        ax.scatter(
            x, y,
            color="black",
            marker="o",
            label="Points"
        )

        # Draw a fashed line on the axes, in red
        # Could use data from scipy.optimize here
        ax.plot(
            x,
            3 * x + 15,
            label="Expected",
            linestyle="--",
            color="red",
        )

        return fig

    basic_plot()
    return np, plt


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Adding labels and legends

    This looks already quite good. But a plot without labels is not really "data". Let's look at how we can annotate the plot further.

    > **Note**: in chemistry we often forego the legend and annotate the figure fully in the caption. This could say:
    >
    > **Figure 1.** Response of the detector, showing raw data (palatinate dots) and the resulting sinusoidal fit (palatinate line).
    """)
    return


@app.cell
def _(np, plt):
    def labelled_plot():
        fig, ax = plt.subplots(figsize=(6, 4))

        # Data
        rng = np.random.default_rng(seed=2025)
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        y_scatter = np.sin(x) + rng.normal(loc=0, scale=0.05, size=len(x))

        ax.scatter(
            x,
            y_scatter,
            color="purple",
            marker=".",
            label="Raw data"
        )

        ax.plot(
            x, y, 
            color="purple",
            linewidth="0.7",
            label="Oscillation"
        )

        ax.set_xlabel("Time / s")        
        ax.set_ylabel("Intensity / a.u.") 
        ax.set_title("Detector Response")
        ax.legend() # Shows the labels

        return fig

    labelled_plot()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## LaTeX in labels

    In sciences, we often have comlicated labels in our plots. You can use [LaTeX](https://en.wikipedia.org/wiki/LaTeX) for formatting the labels in `matplotlib`.
    """)
    return


@app.cell
def _(np, plt):
    def latex_labels():

        # As before, let's plot some time based data
        fig, ax = plt.subplots(figsize=(5, 4))

        t = np.linspace(0, 5, 20)
        y1 = np.exp(-t)
        y2 = np.exp(-0.5 * t)

        # THE WHITE MARKER TRICK:
        # mfc='white' makes markers hollow-looking and very distinct
        # (mfc = marker face colour)
        # mew=1.5 makes them look sharp
        # (mew = marker edge width)

        ax.plot(
            t, y1, 
            "o-", 
            color="orange", 
            label="Catalyst 1", 
            mfc="white", 
            mew=1.5
        )
        ax.plot(
            t, y2, 
            "s-", 
            color="blue", 
            label="Catalyst 2", 
            mfc="white", 
            mew=1.5
        )

        # LaTeX for math/units
        # Not that we need to use "raw" strings, as LaTeX contains {}
        ax.set_xlabel(r"Time, $t$ / min")
        ax.set_ylabel(r"Concentration, $c$ / mol$\cdot$l$^{-1}$")

        ax.legend()

        return fig

    latex_labels()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Multiple subplots

    Often, you need to compare two different things side-by-side (e.g., a Raw Spectrum vs. a Calibrated Plot). We can tell `plt.subplots` how many rows and columns we want.
    """)
    return


@app.cell
def _(plt):
    def multi_panel():
        # Create 1 row and 2 columns
        # 'axes' is now a list containing two frames: axes[0] and axes[1]
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))

        # Left Frame
        axes[0].set_title("Plot A")
        axes[0].plot([1, 2, 3], [10, 20, 30])

        # Right Frame
        axes[1].set_title("Plot B")
        axes[1].bar(["He", "Ne", "Ar"], [4, 20, 40])

        return fig

    multi_panel()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    We can even go all crazy with `subplot_mosaic()` - less common in chemistry, but belowed by some fields like bioinformatics. It takes a text-based map describing our layout. As it gets more and more complicated, you might be better off aligning those plots in a separate graphics editor (like open-source vector editor [Inkscape](https://inkscape.org/)).
    """)
    return


@app.cell
def _(plt):
    def mosaic_layout():
        # Define a layout where 'A' is a big top plot, 
        # and 'B' and 'C' are smaller ones below.
        layout = """
        AAAA
        BBCC
        """
        fig, axes = plt.subplot_mosaic(layout, figsize=(8, 6))

        # Panel labels
        for label, ax in axes.items():
            ax.text(
                0, 1.1, 
                f"{label.lower()}.", 
                transform=ax.transAxes, 
                fontweight='bold', 
                va='top', # vertical align
                ha='right', # horizontal align
                fontsize=10
            )

            # Cleaner look for demo
            ax.set_xticks([])
            ax.set_yticks([]) 

        axes['A'].set_ylabel("Spectrum / a.u.")
        axes['B'].set_ylabel("Kinetics")
        axes['C'].set_ylabel("Residuals")

        return fig

    mosaic_layout()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Developing `matplotlib` style

    It is important to stay consistent. We will set up a style for `matplotlib` that you can just copy into (or `import`) your new projects.

    ### Colour-blind friendly palettes

    Let's start by setting up a couple of common palettes optimised for colour-blindness. We will then set up a "cycler" in `matplotlib` so that it just uses those colours without you having to define colours explicitly!

    - [Wong palette](https://davidmathlogic.com/colorblind/#%23000000-%23E69F00-%2356B4E9-%23009E73-%23F0E442-%230072B2-%23D55E00-%23CC79A7)
    - [Tol palette](https://sronpersonalpages.nl/~pault/#sec:qualitative)
    """)
    return


@app.cell
def _():
    from cycler import cycler

    def palettes():

        WONG = [
            "#000000", 
            "#E69F00", 
            "#56B4E9", 
            "#009E73", 
            "#F0E442", 
            "#0072B2", 
            "#D55E00", 
            "#CC79A7"
        ]

        TOL_BRIGHT = [
            "#4477AA", 
            "#AA3377",
            "#228833",
            "#CCBB44",
            "#66CCEE",
            "#EE6677",
            "#BBBBBB",
            "#000000", 
        ]

        return WONG, TOL_BRIGHT

    return cycler, palettes


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### `rcParams`

    You can specify the `matplotlib` parameters in the "run command parameters" ([`rcParams`](https://matplotlib.org/stable/users/explain/customizing.html)) dictionary. You can save them as a style file and import with `ply.style.use(FILE_PATH)`. Below is an example of a - rather ugly - style setting, and your job is to change them until the final plot can be deemed "publication quality".

    The following cells are set up so that the final plot should update itself when you execute the `get_my_journal_style()` call. In real life, you can just use:

    ```python
    import matplotlib.pyplot as plt

    plt.style.use('./chemistry.mplstyle')
    ```

    or

    ```python
    rcParams_dict = {
        YOUR SETTINGS
    }

    plt.rcParams.update(rcParams_dict)
    ```

    to globally update the settings in the document.
    """)
    return


@app.cell
def _(cycler, palettes):
    COLOR_PALETTE = palettes()[1]

    def get_my_journal_style():
        style = {
            # --- FONT SETTINGS ---

            # Use sans-serif fonts; stixsans is a modern math font
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
            # STIX Two Text is decent serif option for chemistry
            # Making 1 I and l look different!
            "font.serif": ["STIX Two Text", "STIXTwoText", "STIXGeneral"],
            "mathtext.fontset": "stixsans", 

            # Perhaps too small?
            "font.size": 6,                 

            # --- FIGURE & EXPORT ---

            # 3.25in is one ACS/RCS column width 
            # (don't change that)
            "figure.figsize": (3.25, 3.25),

            # It's good to export at higher DPI for print
            # (don't change that)
            "figure.dpi": 150,
            "savefig.dpi": 600,
            "savefig.transparent": True,

            # --- COLOURS ---

            "axes.prop_cycle": cycler(color=COLOR_PALETTE),

            # --- THE BOX & TICKS ---

            # This needs heavy fixing
            "xtick.direction": "out",
            "ytick.direction": "out",
            "xtick.major.size": 15,
            "ytick.major.size": 15,
            "xtick.major.width": 5.0,
            "ytick.major.width": 5.0,
            "xtick.top": False,               
            "ytick.right": False,
            "axes.linewidth": 0.5,

            # --- MARKERS ---

            "lines.marker": "*",
            "lines.markersize": 12,


            # --- LEGEND ---

            "legend.frameon": True,
            "legend.fontsize": 5,
            "legend.handlelength": 3.0,
            "lines.markerfacecolor": "#EECC66",
            "lines.markeredgewidth": 2.5,

            # --- PADDING ---

            "axes.labelpad": -5,

            # Don't change this:
            "figure.constrained_layout.use": True
        }
        return style

    return COLOR_PALETTE, get_my_journal_style


@app.cell
def _(get_my_journal_style, np, plt):
    def figure_exercise():
        times = np.linspace(0, 10, 15)
        trials = [np.exp(-0.4*times), np.exp(-0.25*times), np.exp(-0.15*times),
                  np.exp(-0.3*times), np.exp(-0.2*times), np.exp(-0.1*times),
                  np.exp(-0.5*times), 
                 ]

        with plt.rc_context(rc=get_my_journal_style()):
            fig, ax = plt.subplots(figsize=(5, 4))

            for i, data in enumerate(trials):
                ax.plot(times, data, label=f"Trial {i+1}")

            ax.set_xlabel(r"Time, $t$ / min")
            ax.set_ylabel(r"Concentration, $c$ / mol$\cdot$L$^{-1}$")
            ax.legend()

        return fig

    figure_exercise()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    A potential publication-quality output could look something like this one. You probably prefer a sans-serif font, but I kept a serif font here to demonstrate that those can still look modern with a bit more of a "textbook vibe".
    """)
    return


@app.cell(hide_code=True)
def _(COLOR_PALETTE, cycler):
    def fts_matplotlib_style():
        style = {
            # --- FONT SETTINGS ---

            # Use sans-serif fonts; stixsans is a modern math font
            "font.family": "serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
            "font.serif": ["STIX Two Text", "STIXTwoText", "STIXGeneral"],
            "mathtext.fontset": "stixsans",
            # "mathtext.fontset": "stixsans", 
            # "mathtext.default": "regular",
            "font.size": 12,                 

            # --- FIGURE & EXPORT ---

            "figure.figsize": (3.25, 3.25), # 7 for double column
            "figure.dpi": 150,
            "savefig.dpi": 600,
            "savefig.transparent": True,

            # --- COLOURS ---

            "axes.prop_cycle": cycler(color=COLOR_PALETTE),

            # --- THE BOX & TICKS ---

            # This needs heavy fixing
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.major.size": 4,
            "ytick.major.size": 4,
            "xtick.major.width": 1.0,
            "ytick.major.width": 1.0,
            "xtick.top": True,               
            "ytick.right": True,
            "axes.linewidth": 1.0,

            # --- MARKERS ---

            "lines.marker": "o",
            "lines.markersize": 6,
            "lines.markerfacecolor": "#FFFFFF",
            "lines.markeredgewidth": 1.5,

            # --- LEGEND ---

            "legend.frameon": False,
            "legend.fontsize": 9,
            "legend.handlelength": 1.0,

            # --- PADDING ---

            "axes.labelpad": 4,
            "figure.constrained_layout.use": True
        }
        return style

    return (fts_matplotlib_style,)


@app.cell(hide_code=True)
def _(fts_matplotlib_style, np, plt):
    def figure_exercise_clean():
        times = np.linspace(0, 10, 15)
        trials = [np.exp(-0.4*times), np.exp(-0.25*times), np.exp(-0.15*times),
                  np.exp(-0.3*times), np.exp(-0.2*times), np.exp(-0.1*times),
                  np.exp(-0.5*times), 
                 ]

        with plt.rc_context(rc=fts_matplotlib_style()):
            fig, ax = plt.subplots(figsize=(5, 4))

            for i, data in enumerate(trials):
                ax.plot(times, data, label=f"Trial {i+1}")

            ax.set_xlabel(r"Time, $t$ / min")
            ax.set_ylabel(r"Concentration, $c$ / mol$\cdot$L$^{-1}$")
            ax.legend()

        return fig

    figure_exercise_clean()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Further plotting resources

    > There is no point trying to learn `matplotlib` by heart; use available online resources and browse their [Examples gallery](https://matplotlib.org/stable/gallery/index.html) to achieve the effects you want!

    Once you progress in your career to look at hundreds and thousands of data points, you might want to look into other libraries that are useful for visualisation and statistical analysis. In particular, watch out for:

    - [`pandas`](https://pandas.pydata.org/): introduces dataframes that are useful for data wrangling
    - [`plotly.express`](https://plotly.com/python/plotly-express/): great tool for interactive plots
    - [`seaborn`](https://seaborn.pydata.org/): higher-level tools for statistical visualisation
    """)
    return


if __name__ == "__main__":
    app.run()
