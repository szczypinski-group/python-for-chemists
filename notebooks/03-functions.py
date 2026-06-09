# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.13.15",
# ]
# ///

import marimo

__generated_with = "0.23.9"
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

    Once we have _defined_ a function (with `def`) we _call_ it, by typing its name and any arguments in the parentheses. Only once we've called it, the code inside the function will be executed!

    ```python
    function_name()
    ```

    > **Note**: if a function definition is on its own in a Python cell in `marimo`, it can be imported into your other notebooks. It's [_reusable_](https://docs.marimo.io/guides/reusing_functions/). This is very powerful - you can keep a "main notebook" with your useful helper functions for data analysis and import them when needed!
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Indentation

    In some programming languages, blocks of code are enclosed in curly brackets or isolated some other way. In Python, we use whitespaces (tabs and spaces) for that - there are no strict rules, but you have to be consistent. I recommend a single tab (converted to four spaces) as the indentation pattern - this is the default in most notebooks and editors.

    ```python
    # This is the default code level

    import math

    # Variables defined at this code level
    # are available everywhere deeper
    # so can be considered "constants"
    # Python convention is to name them in ALL-CAPS

    LIGHT_SPEED = 3.0e8

    def get_energy(mass):
        # Everything at this indent level is a block

        # Variables defined here are only available
        # within this block (or deeper in)
        # we can also use function arguments (`mass`)
        # within thie block (i.e., function definition).

        print("We are inside now")

        # `energy` is only inside the function
        # uses function argument and a constant

        energy = mass * LIGHT_SPEED ** 2

        return energy

    # Back to the default level
    # Rest of the code ...

    ```
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Let's see that in practice in a Python cell (I'm using the advanced `try`...`except` block so that the code can execute - it would throw an error otherwise, try for yourself):
    """)
    return


@app.cell
def _(mass):
    import math

    LIGHT_SPEED = 3.0e8

    def get_energy(mass):
        print(f"LIGHT_SPEED inside the function: {LIGHT_SPEED}")
        return mass * LIGHT_SPEED ** 2

    _electron = 9.10e-31
    _electron_energy = get_energy(_electron)

    try:
        print(mass)
    except Exception as e:
        print(f"Outside the function: {e}.")

    print(f"Energy of an electron: {_electron_energy} J.")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Let's write a simple function that will convert Celsius to Kelvin and see how we can then expand on its functionality.
    """)
    return


@app.function
def print_kelvin(temp):
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
    print_kelvin(temp=45)
    print_kelvin(temp=body_temp)

    # We can omit the argument names.
    print_kelvin(20)
    print_kelvin(body_temp)
    return (body_temp,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Functions also do not need to have any arguments. Try completing the function below to just print "Hello!"
    """)
    return


app._unparsable_cell(
    r"""
    # Here we define the function:
    def hi():
        # COMPLETE HERE

    # Let's see if it works, here we call it:
    hi()

    # Running this cell should display "Hello!"
    """,
    name="_"
)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## `return` statements

    Most often we do not want the function to just print some result to the screen - we want save the result of calculation as a variable to use it. This is when the `return` statements come in handy. Imagine wanting to calculate the $\Delta G_\textrm{rxn}$ for a reaction, knowing the equilibrium constant $K_\textrm{eq}$ and the temperature in $\degree C$.

    Complete the following cell and execute it to see if it worked.
    """)
    return


app._unparsable_cell(
    r"""
    def get_kelvin(temp):
        # you can define an auxiliary variable (e.g. "kelvin_temp")
        # or redefine the local variable with temp += ...
        # or return the result of an operation straight away

        # FIXME: include a return statement


    def gibbs(k_eq, temp):
        dG = - 8.314472 * get_kelvin(temp) * math.log(k_eq)
        return dG
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(body_temp, get_kelvin, gibbs):
    def function_passed():
        passed = False
        try:
            test_c = get_kelvin(body_temp) == 309.75
            test_g = abs(gibbs(10, 18) - (-5574.00)) < 1.0

            passed = test_c and test_g

            if passed:
                return mo.callout("✅ Correct", kind="success")
            else:
                return mo.callout("❌ Not quite.", kind="danger")   

        except Exception as e:
            passed = False
            return mo.callout(f"❌ Python error: {e}.", kind="danger")

    function_passed()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Arguments

    We have seen that a function can take any number of arguments (the variables in parenthesis after the function name). They can only be used **inside the function** and have no meaning anywhere else in the code. That means that you could in principle also have a variable called `temp` elsewhere in the code and just call:

    ```python
    temp = 35

    get_kelvin(temp=temp)
    ```

    Arguments that do not have any value assigned to them when defining a function are called _positional arguments_. They are compulsory to be passed when calling the funciton.

    Some arguments can have a default value. We call them _keyword arguments_. Let's redefine our function so that it could also sometimes return the temperature value in Fahrenheits. We will use an `if`-statement for this - more on it soon.

    Also note how we have now split the arguments across multiple lines - this is purely esthetic. I like doing that so that lines are shorter ([max 79 characters](https://peps.python.org/pep-0008/#maximum-line-length)) and I can easily compare two Python files side by side on my laptop.
    """)
    return


@app.function
def from_celsius_usa(
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
    print(f"Body temperature in Kelvin is: {from_celsius_usa(body_temp)} K.")
    print(f"Body temperature in Fahrenheit is: {from_celsius_usa(body_temp, fahrenheit=True):.2f} F.")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    When using proper names of the arguments, we do not need to worry about the order. I would typically recommend using the order in the definition, so that the code is easier to read (also the order must be correct if argument names are not used.)
    """)
    return


@app.cell
def _(body_temp):
    # temp first, fahrenheit second
    print(f"Body temperature in Fahrenheit is: {from_celsius_usa(temp=body_temp, fahrenheit=True):.2f} F.")

    # fahrenheit first, temp second
    print(f"Body temperature in Fahrenheit is: {from_celsius_usa(fahrenheit=True, temp=body_temp):.2f} F.")

    # Split for shorter code lines
    print(
        f"Body temperature in Fahrenheit is: "
        f"{from_celsius_usa(temp=body_temp, fahrenheit=True):.2f} F."
    )

    # Split function call even further
    _temp_f = from_celsius_usa(
        temp=body_temp,
        fahrenheit=True
    )
    print( f"Body temperature in Fahrenheit is: {_temp_f:.2f} F.")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Docstrings

    You might have noticed that if you hovered your mouse over a built-in function earlier in this workshop, you got a little box that describes what arguments it takes and what it does. Those are defined by so-called docstrings - strings placed at the top of the function. Traditionally they are multi-line strings where the first line provides a short summary, followed by longer description and information about what variables it takes, and what is returned.

    Here, we will use the [numpy convention](https://numpydoc.readthedocs.io/en/latest/format.html) for our docstrings. Some developers prefer the [Google convention](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).

    They are not necesasry but it is a good habit to include them - the future you will thank you greatly for doing it as you go! Let's write a docstring for our temperature conversion function.
    """)
    return


@app.function
def from_celsius(
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
    Now try typing `from_celsius()` in the next cell and see how you get a little helpful paragraph about the function!
    """)
    return


@app.cell
def _(from_):
    from_
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Advanced topics
    """)
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
    Note that if the value returns nothing then its return type is `None`.
    """)
    return


@app.function
def print_temp(
    temp : float | int,
) -> None:
    """Print value of the temperature.

    Arguments
    ---------
    temp
        Temperature in Celsius.

    """
    print(f"Temperature is {temp} degrees.")


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    While it might feel completely unnecessary, starting your function definition with docstrings and explicit types helps you structure your thoughts and makes coding much easier down the line.
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Classes

    This is a **more advanced topic** that you might want to skip on your first exposure to Python.

    You can see above that we defined two separate variables for each point and calculated the difference between them with another set of variables. What if we had 1,000 different points? We can create a [`class`](https://docs.python.org/3/tutorial/classes.html) that contains all the information about the points (_attributes_) and some useful functions (_methods_) related to them. We will learn more about functions in the next section, but let's consider this example:
    """)
    return


@app.class_definition
class PointExample:
    def __init__(
        self,
        x: float,
        y: float,
        z: float,
    ):
        self.x = x 
        self.y = y
        self.z = z


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    > **Note**: so called "magic methods" in Python start with two underscores (e.g., `__init__`). They preform some special functions related to the inner working of the programming language; in this case, `__init__` initialises an instance of the class.

    Where `self` is the conventional name for the first parameter, which corresponds to the instance of the class _itself_. We can can create points consistently as _instances_ of class `Point` and access them usign the familiar "dot" notation:
    """)
    return


@app.cell
def _():
    _point1 = PointExample(1, 1, 1)
    _point2 = PointExample(3, 4, 5)

    print(f"Point(x={_point2.x}, y={_point2.y}, z={_point2.z})")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    but the main strength comes from then isolating relevant methods together. Try writing a method that returns the distance between two points for this new complete class representing a `Point`.

    > **Note**: as we will be defining arguments for methods inside the `Point` class, the `Point` does not yet exist - we can pass it as a string in the type hints (see `distance_from()` below).
    """)
    return


@app.cell
def _(diff_x, diff_y, diff_z, sqrt):
    class Point:
        """Represents a point in 3D space.

        Attributes
        ----------
        x, y, z : float
            Coordinates in the 3D space.

        Methods
        -------
        distance_from(point)
            Returns Euclidean distance from another point.

        """
        def __init__(
            self,
            x: float,
            y: float,
            z: float,
        ):
            self.x = x 
            self.y = y
            self.z = z

        def __str__(
            self
        ):
            return f"Point(x={self.x}, y={self.y}, z={self.z})"

        def distance_from(
            self,
            point : "Point"
        ):
            # FIXME: Define local variables for diff_x/y/z

            return sqrt(diff_x ** 2 + diff_y ** 2 + diff_z ** 2)

    _point1 = Point(x=1, y=1, z=1)
    _point2 = Point(3, 4, 5)

    _point1.distance_from(_point2)
    return (Point,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    It is often useful to define some more magic methods, such as `__str__` or `__repr__` – those are used when you try to print the object as a string. Compare the output of those two commands:
    """)
    return


@app.cell
def _(Point):
    import numpy as np

    def check_point():
        _point1 = Point(1, 1, 1)
        _point2 = Point(3, 4, 5)

        try:
            passed = np.isclose(_point1.distance_from(_point2), 5.39, atol=0.01)

            if passed:
                return mo.callout("✅ Correct", kind="success")
            else:
                return mo.callout("❌ Not quite.", kind="danger")  

        except Exception as e:
            passed = False
            return mo.callout(f"❌ Python error: {e}.", kind="danger")

    check_point()
    return


@app.cell
def _(Point):
    print(f"Class for which we defined __str__: {Point(1,1,1)}")
    print(f"Class for which we didn't: {PointExample(1,1,1)}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Lambda functions

    This is another **more advanced topic** that you might want to ignore when learning the basics. A lambda function is a small, anonymous (unnamed), one-line function.

    The syntax for lambda functions is rather implicit:

    ```python
    lambda arguments: expression
    ```
    """)
    return


@app.cell
def _():
    to_kelvin_lab = lambda c: c + 273.15
    print(to_kelvin_lab(25))
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Lambda functions are useful when defining short one-line functions, most commonly as arguments to another function. The most common example is sorting functions. Most function that perform some sorting operation (e.g., `sort()` or `min()`) take an optional `key` argument, which is the function defining the comparison operator.

    Imagine we store solvent information as a tuple: `(name, boiling_point, density)` and want to sort by the value of the `boiling_point` or `density`:
    """)
    return


@app.cell
def _():
    _solvents = [("Ethanol", 78, 0.789), ("Water", 100, 1.000), ("Chloroform", 61, 1.483)]

    print(f"Sorted by boiling point: {sorted(_solvents, key=lambda x: x[1])}")

    def max_density(solvents):
        pass
        # FIXME: Use max() with lambda function key to return solvent of max density

    try: 
        print(f"Maximum density solvent is: {max_density(_solvents)[0].lower()}.")

    except Exception as e:
        print(f"Python error: {e}.")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    This is yet another place where `dataclass` becomes a very useful structure, as it adds further semantics to your lambda functions.
    """)
    return


app._unparsable_cell(
    r"""
    from dataclasses import dataclass

    @dataclass
    class Solvent:
        name : str
        boiling_point : float
        density : float

    _solvents = [
        Solvent("ethanol", 78, 0.789),
        Solvent("water", 100, 1.000),
        Solvent("chloroform", 61, 1.483)
    ]

    print(
        "Solvent with highest density is: ",
        f"{max(
            _solvents, key=lambda x: # FIXME: identify the comparison element
        )}."
    )
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
