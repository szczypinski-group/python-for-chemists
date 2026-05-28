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
    # Creating new functions

    The usefulness of programming comes in reusing code. If you want to calculate a value once or plot a single graph, tools like a calculator or Excel might be sufficient. But if you find yourself repeating the same operation many times and striving for consistency - Python will help you automate that process easily.

    The same way that we could use functions from external modules or the standard library, we can write our own functions to use them later. The standard syntax for defining a function is:

    ```python
    def function_name(arguments):
        return statement
    ```

    where the `arguments` are essentially variables used **inside** the function and `return` keyword specifies what the function should give back to the user (typically so that it can be assigned to a variable or printer). The `return` part is optional (e.g., if you just want the function to print).

    Let's write a function that will convert Celsius to Kelvin and see how we can then expand on its functionality.
    """)
    return


@app.function
def from_celsius0(temp):
    print(f"Temperature in Kelvin is {temp+273.15} K.")


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Using the function is just as simple as "calling" it with all the necessary arguments inside the brackets. It is fine to omit the argument names, but trust me - it makes it much easier to understand your code if you do use them explicitly!
    """)
    return


@app.cell
def _():
    body_temp = 36.6

    # We can call the function just like before.
    from_celsius0(temp=45)
    from_celsius0(temp=body_temp)

    # We can omit the argument names.
    from_celsius0(20)
    from_celsius0(body_temp)
    return (body_temp,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Functions also do not need to have any arguments. Try completing the function below to just print "Hello!"
    """)
    return


app._unparsable_cell(
    r"""
    def hi():
        # COMPLETE HERE

    # Let's see if it works. Running this cell should display "Hello!"
    hi()
    """,
    name="_"
)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## `return` statements

    Most often we do not want the function to just print some result to the screen - we want to use it. This is when the `return` statements come in handy. Imagine wanting to calculate the $\Delta G_\textrm{rxn}$ for a reaction, knowing the equilibrium constant $K_\textrm{eq}$ and the temperature in $\degree C$.

    Complete the following cell and execute it to see if it worked.
    """)
    return


@app.cell
def _():
    # Running this cell should display:
    # Body temperature in Kelvin is 309.75 K.
    # dG at 18 C is -5574.002 J K-1 mol-1.

    import math

    def from_celsius1(temp):
        return # COMPLETE HERE


    def gibbs(k_eq, temp):
        dG = - 8.314472 * from_celsius1(temp) * math.log(k_eq)
        return dG

    return from_celsius1, gibbs


@app.cell(hide_code=True)
def _(body_temp, from_celsius1, gibbs):
    exercise_1_passed = False

    try:
        test_c = from_celsius1(body_temp) == 309.75
        test_g = abs(gibbs(10, 18) - (-5574.00)) < 1.0

        exercise_1_passed = test_c and test_g

    except Exception:
        exercise_1_passed = False

    if exercise_1_passed:
        feedback = mo.callout("✅ Correct!", kind="success")
    else:
        feedback = mo.callout("❌ Not quite.", kind="danger")

    feedback
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Arguments

    We have seen that a function can take any number of arguments (the variables in parenthesis after the function name). They can only be used **inside the function** and have no meaning anywhere else in the code. That means that you could in principle also have a variable called `temp` elsewhere in the code and just call:

    ```python
    temp = 35

    from_celsius(temp=temp)
    ```

    Arguments that do not have any value assigned to them when defining a function are called _positional arguments_. They are compulsory to be passed when calling the funciton.

    Some arguments can have a default value. We call them _keyword arguments_. Let's redefine our function so that it could also sometimes return the temperature value in Fahrenheits. We will use an `if`-statement for this - more on it soon.

    Also note how we have now split the arguments across multiple lines - this is purely esthetic. I like doing that so that lines are shorter ([max 79 characters](https://peps.python.org/pep-0008/#maximum-line-length)) and I can easily compare two Python files side by side on my laptop.
    """)
    return


@app.function
def from_celsius2(
    temp,
    fahrenheit = False,
):
    # If the user passes with fahrenheit=True, we return those:
    if fahrenheit:
        return temp * (9/5) + 32

    else:
        return temp + 273.15


@app.cell
def _(body_temp):
    print(f"Body temperature in Kelvin is: {from_celsius2(body_temp)} K.")
    print(f"Body temperature in Fahrenheit is: {from_celsius2(body_temp, fahrenheit=True):.2f} F.")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    When using proper names of the arguments, we do not need to worry about the order. I would typically recommend doing it, so that the code is easier to read.
    """)
    return


@app.cell
def _(body_temp):
    # temp first, fahrenheit second
    print(f"Body temperature in Fahrenheit is: {from_celsius2(temp=body_temp, fahrenheit=True):.2f} F.")

    # fahrenheit first, temp second
    print(f"Body temperature in Fahrenheit is: {from_celsius2(fahrenheit=True, temp=body_temp):.2f} F.")

    # split for shorter code lines
    print(
        f"Body temperature in Fahrenheit is: "
        f"{from_celsius2(temp=body_temp, fahrenheit=True):.2f} F."
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Docstrings

    You might have notices that if you hover your mouse over a built-in function earlier in this workshop, you get a little box that describes what arguments it takes and what it does. Those are defined by so-called docstrings - strings placed at the top of the function. Traditionally they are multi-line strings where the first line provides a short summary, followed by longer description and information about what variables it takes, and what is returned.

    Here, we will use the [numpy convention](https://numpydoc.readthedocs.io/en/latest/format.html) for our docstrings. Some developers prefer the [Google convention](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).

    They are not necesasry but it is a good habit to include them - the future you will thank you greatly for doing it as you go! Let's write a docstring for our temperature conversion function.
    """)
    return


@app.function
def from_celsius3(
    temp,
    fahrenheit = False,
):
    """Convert temperature from Celsius.

    Arguments
    ---------
    temp : int | float
        Temperature in Celsius.

    fahrenheit : bool
        If True, the function will return a value
        in Fahrenheit. By default, False.

    Returns
    -------
    float
        Temperature in Kelvin or Fahrenheit.

    """
    if fahrenheit:
        return temp * (9/5) + 32

    else:
        return temp + 273.15


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Now try typing `from_celsius3()` in the next cell and see how you get a little helpful paragraph about the function!
    """)
    return


@app.cell
def _(from_):
    from_
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Type definitions

    Another non-compulsory but very useful addition is to explicitly specify the types expected for each argument and the return statement. In more sophisticated editors (or _integrated development environments,_ IDEs), this will give you warnings if you are trying to pass a wrong value to your function. Believe me, most errors in your future coding will result from passing wrong arguments.
    """)
    return


@app.function
def from_celsius_final(
    temp : float | int,
    fahrenheit : bool = False,
) -> float:
    """Convert temperature from Celsius.

    Arguments
    ---------
    temp
        Temperature in Celsius.

    fahrenheit
        If True, the function will return a value
        in Fahrenheit. By default, False.

    Returns
    -------
    Temperature in Kelvin or Fahrenheit.

    """
    if fahrenheit:
        return temp * (9/5) + 32

    else:
        return temp + 273.15


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    While it might feel completely unnecessary, starting your function definition with docstrings and explicit types, helps you structure your thoughts and makes coding much easier down the line.
    """)
    return


if __name__ == "__main__":
    app.run()
