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

    In this exercise we will analyse real world data from our 2nd year Physical Chemistry practicals - emission spectrum of a laser. It will combine some elements of the previous workshops. As always, feel **free to experiment** with the code, you can always easily restart the kernel if things go very wrong!

    > This exercise demonstrates how you can write great lab reports as a `marimo` notebook with all **raw data, analysis, and discussion in one place**!
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Loading experimental data
    """)
    return


if __name__ == "__main__":
    app.run()
