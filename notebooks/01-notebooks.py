# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.13.15",
# ]
# ///

import marimo

__generated_with = "0.23.7"
app = marimo.App(app_title="Introduction to Python notebooks")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Python Notebooks

    Python notebooks are basically your interactive coding documents. While we don't always use them in research (we tend to favour standalone scripts for reproducibility), they are really useful for data processing and explorations.

    > ⚠️ **Caution!** ⚠️
    >
    > The notebooks for the workshops **run in your browser** - so make sure to **save all relevant files** to your computer before shutting it down!

    ## Types of cells

    They can be a mix of _Python cells_ and _Markdown cells_. Python cells contain code that can be run inside the notebook with any output of the code (values, text, plots) appearing directly below.

    Markdown cells (like this one) are used to help to convey information. They support formatting in [Markdown](https://www.markdownguide.org/basic-syntax/), as well as some LaTeX:

    \[
            f(x) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \ldots.
    \]

    ## Example use

    You can see that Python notebooks can be quite useful to present your results. You can generate plots from your data directly with Python cells and then provide some discussion in the following Markdown cell. The beauty of that is that you can easily reuse your code and don't need to keep pasting plots from Excel!

    ## Explore

    To see the Markdown code used to generate this cell, click on the three dots and select "Show code" (or click `Ctrl + H` with the cell highligted). You can also double-click on the text to edit the Markdown code, and click `Esc` when you are done. To add a new cell, click on the small `+` signes to the left. To execute and move to the next cell, press `Shift + Enter`.
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Running code cells

    In marimo code cells are executed automatically. You can also trigger the execution manually by clicking on the Play button (or `Ctrl + Enter`). Unlike, Jupyter, marimo will keep track of what other cells your current cell depends on and execute them for you. Don't worry if this does not make sense now - but trust me, it will make your life much easier in the future!
    """)
    return


@app.cell
def _():
    total = 0

    for i in range(1, 11):
        total += i
        print(f"Current total is: {total}")

    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Another pecularity of marimo is that - unlike in Jupyter - you cannot re-use variables. So if you had code cell now with `total = 5`, that would throw an error. Again, this might not make sense now but is an extremely good practice!
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Useful features

    ## Python kernel

    The kernel is a special program that runs in the background and executes the code. Sometimes it might crash and could be complaining even if the code is correct. This is more common with Jupyter than marimo (due to the _hidden state_ problem), but if you need to restart it, you can do it from the hamburger menu in the top right corner.
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Exploring variables

    The _variable explorer_ view  - the `(x)` button on the left hand side menu bar - can also be useful to troubleshoot your code. It displays what variables you have defined in the notebook, their types, current values, and what cells use them. This is often the first place I look when something doesn't work as expected.

    ## Document outline

    When drafting reports as marimo notebooks, your files might get long. The scroll button on the left opens the _outline view_, which lets you easily jump between different Markdown headlines in the document.
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Markdown basics

    Some useful Markdown syntax that you might want to use when preparing reports or analysing data can be found in the table underneath.

    | Markdown | Result |
    | --- | --- |
    | `# Header` | Main section header |
    | `## Subheader` | Subsection header |
    | `### Sub-subheader` | You get the idea... |
    | `*Text*` | _Text_ in italics |
    | `**Text**` | __Text__ in italics |
    | ``Text` ` | `Text` in monospace |

    You can also make lists with asterisks/dashes and numbers:

    * This is a single bullet.
    - And another one.
    - But better stay consistent.

    1. But you might prefer numbered lists.
    2. Like this one?

    And also (interactive) to-do lists with `- [ ]`

    - [ ] Finally this is a TODO list.
    - [X] That you can tick off!
    """)
    return


if __name__ == "__main__":
    app.run()
