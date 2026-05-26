# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.13.15",
# ]
# ///

import marimo

__generated_with = "0.23.7"
app = marimo.App()

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Python Notebooks

    Python notebooks are basically your interactive coding documents. While we don't always use them in research (we tend to favour standalone scripts for reproducibility), they are really useful for data processing and explorations. The notebooks for the workshops run in your browser - so **make suret to save all relevant files** to your computer before shutting it down!

    ## Types of cells

    They can be a mix of _Python cells_ and _Markdown cells_. Python cells contain code that can be run inside the notebook with any output of the code (values, text, plots) appearing directly below.

    Markdown cells (like this one) are used to help to convey information. They are not executed and support formatting in [Markdown](https://www.markdownguide.org/basic-syntax/), as well as some [LaTeX](https://en.wikibooks.org/wiki/LaTeX/Basics):

    \[
            f(x) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \ldots.
    \]

    ## Example use

    You can see that Python notebooks can be quite useful to present your results. You can generate plots from your data directly with Python cells and then provide some discussion in the following Markdown cell. The beauty of that is that you can easily reuse your code and don't need to keep pasting plots from Excel!

    ## Explore

    To see the Markdown code used to generate this cell, click on the three dots and select "Show code" (or click `Ctrl + H` with the cell highligted). You can also double-click on the text. To add a new cell, click on the small `+` signes to the left. To execute and move to the next cell, press `Shift + Enter`.
    """)
    return


if __name__ == "__main__":
    app.run()
