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

    In this workshop we will learn the basics of [NumPy](https://numpy.org/). So far we have been performing some mathematical operations and using lists - but NumPy is much more efficient at these tasks. It introduces n-dimensional arrays (`ndarray`), has better numerical accuracy, is faster, and automates a lot of array-based operations that would otherwise require lots of `for` loops.

    To use NumPy we need to import it, and the convention is to do it using the `np` alias.
    """)
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(np):
    def example_axis():
        # Python way
        print("-" * 50)
        print("Looping over lists in Python")
        print("-" * 50)
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        output = []
        for x in nums:
            output.append(2*x)
        print(output)

        # NumPy way
        print("-" * 50)
        print("Applying multiplication to a NumPy array")
        print("-" * 50)
        arr = np.arange(10)
        print(2 * arr)

    example_axis()
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
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Scientific Python (SciPy)
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
