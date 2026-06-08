# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.13.15",
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
    # Python Notebooks

    Python notebooks are basically your interactive coding documents. While we don't always use them in research (we tend to favour standalone scripts for reproducibility), they are really useful for data processing and explorations. The notebooks for the workshops run in your browser - so **make sure to save all relevant files** to your computer before shutting it down!

    > **Note**: the earlier notebooks are a bit more read-through, but the level of engagement and your contributions will increase. If you are already familiar with Python, there should be some more advanced examples and concepts as we go, so make sure to at least quickly go through all the workshops!

    ## Types of cells

    They can be a mix of _Python cells_ and _Markdown cells_. Python cells contain code that can be run inside the notebook with any output of the code (values, text, plots) appearing directly below.

    ### Markdown

    Markdown cells (like this one) are used to help to convey information. They are not executed and support formatting in [Markdown](https://www.markdownguide.org/basic-syntax/). We denote headings with the hash signs – the more `#`, the higher the heading level. Text can be **bolded** with double asterisks (`**text**`) and *emphasised* in italics with single asterisks (`*text*`). You can also make [links](https:/https://duckduckgo.com/) and lists. The guide above gives you more formatting syntax.

    ### LaTeX

    [LaTeX](https://en.wikibooks.org/wiki/LaTeX/Basics) is useful for writing out mathematical equations in your text. We include it in-line with text by encapsulating expressions with dollar signs, e.g. $E=mc^2$ and can also have separated block equations separated between `\[` and `\]`, as below:

    \[
            f(x) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \ldots.
    \]

    See the source code for this cell for a LaTeX example, otherwise the Internet is a great resource to learn how to use it!

    ## Example use

    You can see that Python notebooks can be quite useful to present your results. You can generate plots from your data directly with Python cells and then provide some discussion in the following Markdown cell. The beauty of that is that you can easily reuse your code and don't need to keep pasting plots from Excel!

    ## Explore and interact

    To see the Markdown code used to generate this cell, click on the three dots and select "Show code" (or click `Ctrl + H` with the cell highligted). You can also double-click on the text. To add a new cell, click on the small `+` sign to the left. To execute and move to the next cell, press `Shift + Enter`.

    ## AI and LLMs

    Large Language Models have changed the way we code in real life, but they do **not** eliminate the need to understand how coding and basic algorithms function – they are great to help you draft a function or troubleshoot your code, but it is crucial for you to learn how to ask the question in the best possible way. Understanding of the underlying principles or syntax rules helps you maximise the potential of new technologies. Additionally, the skill of abstracting a problem to basic components and algorithms in order to approach it is essential throughout science.

    I recommend that for these workshops you do not use LLMs – there are plenty of links to original resources scattered throughout the notebooks to give you some background information about what we cover.
    """)
    return


if __name__ == "__main__":
    app.run()
