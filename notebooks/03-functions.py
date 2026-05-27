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
    # Creating new functions
    """)
    return


if __name__ == "__main__":
    app.run()
