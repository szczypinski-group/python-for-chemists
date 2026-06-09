# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Variables and basic operations

    Variables are essentially names for values and objects. The can have almost any name but they:

    - cannot start with a number (e.g., `14all` instead of `one_for_all`)
    - cannot contain an operator (e.g., `two-two` instead of `two_minus_two`)
    - are case sensitive (`DeltaG` and `deltaG` are different variables)
    - cannnot be a "Python keyword" (e.g., `and` or `except`)

    Furthermore, there are some [style recommendations](https://peps.python.org/pep-0008/):

    - variables should use `snake_case` (i.e., all lowercase with underscores) rather than `CamelCase` (i.e., with words starting with uppercase); they **cannot** use `kebab-case` as minus sign is an operator!
    - variable names should be reasonably descriptive - it is best to avoid one-one letter variables outside simple iterators (we'll cover that later).
    - it is bad practice to redefine variables (`marimo` will not let you do that) - code gets confusing very fast!

    ## Best `marimo` practices

    The `marimo` team put together a useful [Best Practices](https://docs.marimo.io/guides/best_practices/) guide. It all boils down to trying to encapsulate your code as functions and avoiding using global variables because of potential name clashes (see subsequent notebooks). If you want the variable to be local to the cell, you can prefix its name with `_`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Comments

    Throughout this workshop, we Markdown cells to annotate the code. This is useful for building a narrative. But sometimes you want to include comments in your code that you do not want Python to read at all. Those are done with a hash symbol.
    """)
    return


@app.cell
def _():
    some_energy = -14 # units: kJ

    # This line is ignored
    # We want to display the absolute value:

    print(abs(some_energy))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Assigning variables

    In Python variable assignment is performed with an equal sign. The value on the right is assigned to the variable name on the left. Let's assign some global variables `first_name` and `year` that will be used for more examples.
    """)
    return


app._unparsable_cell(
    r"""
    # We define strings with single or double quotes, e.g.
    # first_name = "Filip"

    first_name = # FIXME: assign a name to the first_name variable

    # We define integer and floating point numbers with no quotes
    # year = 2026

    year = # FIXME: assign a number (no quotes) to the year variable
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `print()` function

    Just like in mathematics, Python functions take their arguments inside the brackets. So to print the value of a variable to the screen, we can simply use `print(variable_name)`.

    There are are also some fancy ways to parse the arguments to the print function, most common ones being `f-strings` (where the value of the variable is substituted inside a string) and `r-strings` (where the text is parsed as _raw_, which is useful for scientific instrument outputs containing unusual characters like the backslash `\`).
    """)
    return


@app.cell
def _(first_name, year):
    # Simple use of print
    print(first_name)

    # These two are equivalent
    print("This year is", year)
    print(f"This year is {year}.")

    # We can also perform operations on variables
    print(f"Next year is {year + 1}.")

    # Some use of raw strings ("\n" is the new line character)
    print("This \n will be \n three lines.")
    print(r"This \n will be \n one line.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Common variable types

    > If it looks like a duck and quacks like a duck, it's a duck.

    At the simplest level, Python is "duck typed". This means that we do not need to worry about specifying the type of a variable on assignment (we can do that, but this is a more advanced topic). The type of variable is directly inferred and the operations will be interpreted in a way that (most often) "just makes sense".

    ### Integers and floating points

    Those are self explanatory. They can be used for mathematical operations and often cast between one another. Try executing the following code cells.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Mathematical operators

    In the most basic way, Python can be used as a simple calculator. For more advanced operations (or more efficient ways to perform operations on precise floating-point variables) such as matrix multiplication, we use the `numpy` library covered later.

    | Operator | Name                     | Example  | Result         |
    | -------- | -------------------------| -------- | -------------- |
    | `+`      | Addition                 | `3 + 2`  | `5`            |
    | `-`      | Subtraction              | `3 - 2`  | `1`            |
    | `*`      | Multiplication           | `3 * 2`  | `6`            |
    | `/`      | True division            | `3 / 2`  | `1.5`          |
    | `//`     | Floor (Integer) division | `3 // 2` | `1`            |
    | `%`      | Modulo (remainder)       | `3 % 2`  | `1`            |
    | `**`     | Exponentiation           | `3 ** 2` | `9`            |
    """)
    return


app._unparsable_cell(
    r"""
    # These variables are local to the marimo cell

    _time_seconds = # FIXME
    _time_minutes = _time_seconds / 60

    print(f"The time is {_time_minutes} min.")
    """,
    name="_"
)


app._unparsable_cell(
    r"""
    # This means we can reuse them in other cells

    _time_minutes = 42
    _time_seconds = # FIXME

    print(f"The other time is {_time_seconds} s.")
    """,
    name="_"
)


app._unparsable_cell(
    r"""
    _mass = 1.6
    _light_speed = 3.0e8
    _energy = # FIXME (using E=mc^2 but with correct Python operators)

    print(f"Energy is {_energy}.")
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Strings

    The other major data type is a string of characters. We define them using single or double quotes. Mathematical operations are slightly different for them as they result in concatenation.
    """)
    return


@app.cell
def _(first_name):
    print(first_name * 2)
    print(first_name + " is learning Python")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It can sometimes get a bit confusing if your characters are numbers - this often happens when importing data from instruments. But they can also be converted into numbers!
    """)
    return


app._unparsable_cell(
    r"""
    _answer = # FIXME: write a number as a string (with quotes)
    # THEN fix this cell and write a number as an integer or float

    print(f"Multiplying a string: {_answer * 2}")
    print(f"Converting to float: {float(_answer)*2}")
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can introduce strings with single or double quotes. This is particularly useful if we have quotes inside the string:
    """)
    return


@app.cell
def _():
    _nickname = "Elias 'EJ' Corey"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### String methods and formatting

    You can do a lot of cool processing to the text with Python functions. Here are some examples for now - more about [methods](https://www.w3schools.com/python/python_ref_string.asp) and [formatting](https://www.w3schools.com/python/ref_string_format.asp) can be found online.
    """)
    return


@app.cell
def _():
    ugly_benzene = "benzene   "
    print(f"Molecule with C6H6 formula is called '{ugly_benzene}'.")
    return (ugly_benzene,)


@app.cell
def _(ugly_benzene):
    # Lets remove trailing spaces with `rstrip()`
    # And capitalise the first letter with `capitalize()`

    print(f"Molecule with C6H6 formula is called '{ugly_benzene.rstrip().capitalize()}'.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Lists

    We often deal with collections of items, not just a single value. Internally, they can store any data type - and those can be mixed (e.g., you can have a list of numbers and a string "NA" for then a number is missing). You can even create lists of lists, or other objects! We can add elements to the list with the `append()` function.
    """)
    return


@app.cell
def _():
    masses_list = [1.01, 4.00, 6.94, 9.01, 10.81, 12.01]
    return (masses_list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Accessing list elements

    We can use an index (with square brackets) to extract an element of a collection. The index numbering starts with zero! A convenient shortcut is that negative indices are counted from the back of the list.
    """)
    return


@app.cell
def _(masses_list):
    print("Hydrogen mass is", masses_list[0])

    # Let's add a new mass to the list with append()
    masses_list.append(14.01)
    print("Last mass we recorded is", masses_list[-1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also _slice_ a list to retrieve multiple elements. A convention that occurs throughout Python is that the first index is included but the second is not, with a format `[start : stop : step]`.

    The default `step` is implied to be `1`. If we omit the `start` or `stop`, those will be the first and last element, respectively.
    """)
    return


@app.cell
def _(masses_list):
    print(f"Every other mass: {masses_list[::2]}.")
    print(f"From second to the end: {masses_list[1:]}.")
    print(f"From second and without the last one: {masses_list[1:-1]}.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, a string is basically a collection of characters, so we can expect similar behaviour!
    """)
    return


@app.cell
def _(first_name, masses_list):
    print(f"'{first_name}' without the first letter: '{first_name[1:]}'.")
    print(f"'{first_name}' has {len(first_name)} characters and our table has {len(masses_list)} masses.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Built-in functions

    We have seen some built-in operations and functions in the examples above. Some other useful functions include:

    | Function | Description |
    | --- | --- |
    | `abs()` | Absolute value |
    | `min()` | Minimum value of a collection |
    | `max()` | Maximum value of a collection |
    | `float()` | Convert a value to a float |
    | `int()` | Convert a value to an integer |
    | `list()` | Convert an object to a list |
    | `tuple()` | Convert an object to a tuple |
    | `set()` | Convert an object to a set |
    | `str()` | Convert an object to a string |
    | `len()` | Length of an object |
    | `round()` | Round a value |
    | `type()` | Return object type (e.g., `float`) |
    | `zip()` | Zips two lists together |

    Feel free to create some new cells to experiment with those functions. Remember that functions take arguments (inside the brackets) and need to be somewhat meaningful (e.g., a comparison between the elements needs to exist for a minimum value to be found).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Getting help

    Every built-in function has documentation: `help(min)`
    """)
    return


@app.cell
def _():
    help(max)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Error messages

    If your input is wrong, Python will give you an error message. Those are extremely useful: they will specify which line of your code is wrong, indicate the problem with a pointer (`^`), and display a (potentially) helpful message!
    """)
    return


app._unparsable_cell(
    r"""
    print("hello world"
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Functions from other modules

    The power of Python lies in its modules. There are hundreds of functions available in collections that form part of the [standard library](https://docs.python.org/3/library/index.html) and even more are available to install online. The most common repository of Python packages is [PyPI](https://pypi.org/).

    Once you have a package installed (either because it was formed as part of the standard library or you installed it using `pip install` in terminal), you need to import it.

    ### Recommended standard library modules

    It is worth being aware of these and using them when appropriate. More documentation can be found online.

    | Module | Description |
    | --- | --- |
    | `math` | Common mathematical functions |
    | `random` | Random number generators |
    | `pathlib` | Useful operations for file paths |
    | `datetime` | Basic date and time types |
    | `itertools` | Common mathematical functions |
    | `shutil` | Higher level file operations (e.g., copying) |
    | `pickle` | Serialisation of Python objects |
    | `csv` | Reading and writing CSV files (e.g., from instruments) |
    | `tomllib` | Parsing TOML files |
    | `json` | Reading and writing JSON files |

    ### Importing

    To use functions or variables (or any other objects) from a module, you have to import them. You can do it in a number of ways:

    - importing the entire module: `import module`
    - importing the module with an alias `import module as m`
    - importing a specific function `from module import function`

    Let's see that in practice with different ways of using the square root function from the `math` module.

    The code snippets below also demonstrate a useful formatting trick, where the floating point number is displayed as a string with X decimal points:

    `variable:.Xf`
    """)
    return


app._unparsable_cell(
    r"""
    # Coordinates of point 1, as x y z
    coords1 = [1, 1, 1]

    # Coordinates of point 2, as x y z
    coords2 = [3, 4, 5]

    # Difference (pairwise)
    dx = coords1[0] - coords2[0]
    dy = # FIXME
    dz = # FIXME
    """,
    name="_"
)


@app.cell
def _(dx, dy, dz):
    # Importing the entire module
    # Using dot to specify the sqrt function from math

    import math

    distance1 = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    print(f"Distance is {distance1:.2f}.")
    return


@app.cell
def _(dx, dy, dz):
    # Importing the entire module under an alias
    # Like above, but "math" is now just "m"

    import math as m

    distance3 = m.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    print(f"Distance is {distance3:.2f}.")
    return


@app.cell
def _(dx, dy, dz):
    # Specifically importing sqrt from math
    # It is now locally known directly as sqrt
    # So no "dot notation" needed

    from math import sqrt

    distance2 = sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    print(f"Distance is {distance2:.2f}.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advanced topics

    This section is a bit **more advanced** - you might want to skip it, but if you are interested there is lots of useful real-world stuff here!

    ## Sets and tuples

    The main differences between those and lists is that sets are unordered and do not contain repeat elements. Lists are _mutable_ (can be modified after creation), while tuples are _immutable_ (cannot be changed).
    """)
    return


@app.cell
def _():
    masses_set = {1.01, 4.00, 6.94, 9.01, 10.81, 12.01}
    masses_tuple = (1.01, 4.00, 6.94, 9.01, 10.81, 12.01)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dictionaries

    Python dictionaries are collections that connect key and values. Maybe we would like to know what catalysts the CAS numbers correspond to. A dictionary is a great way to store that data. They are defined with the following syntax (keys and values can be of any type):

    ```python
    dictionary = { KEY : VALUE }
    ```

    We can look-up a value with:

    ```python
    dictionary[KEY]
    ```
    """)
    return


@app.cell
def _():
    masses_dict = {
        "hydrogen": 1.01,
        "helium": 4.00,
        "lithium": 6.94,
        "beryllium": 9.01,
        "boron": 10.81,
        "carbon": 12.01,
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dataclasses

    In the next workshop, you will learn about classes and [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming). One type of pre-defined classes are those that are designed solely to store data – we could do it in dictionaries but we perhaps a better interface is provided by the special `dataclass` class. Benefit of using classes like this is that many default methods are already defined in a practical way.

    To define a [dataclass](https://docs.python.org/3/library/dataclasses.html), we use the `@dataclass` [_decorator_](https://www.w3schools.com/python/python_decorators.asp):

    ```python
    from dataclasses import dataclass

    @dataclass
    class ExampleDataclass:
        some_field : data_type
        other_field : data_type
    ```

    we can then define methods within the class, use some built-in ones, and keep our code well compartmentalised. They can be very easily converted into dictionaries with a built-it `asdict()` function.
    """)
    return


@app.cell
def _():
    from dataclasses import dataclass, asdict

    @dataclass
    class Person:
        name : str
        cis_id: str

    _filip = Person(name="Filip", cis_id="pbpm73")
    asdict(_filip)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Try writing a data class that stores basic information about reaction conditions in the lab notebook.
    """)
    return


app._unparsable_cell(
    r"""
    from dataclasses import dataclass

    @dataclass
    class Reaction:
        # FIXME: write a class that stores solvent (string), 
        # and temperature (float), time (integer)
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
