# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Flow control

    As you have noticed by now, Python code is executed from top to bottom. Sometimes we want to execute certain block of code conditionally or multiple times.
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Boolean operators

    _Boolean logic_ is when expressions are evaluated as either `True` of `False`. These can be used for adding conditions to your code:

    | Operator | Description |
    | --- | --- |
    | `==` | Equal
    | `!=` | Not equal |
    | `>=` | Greater than or equal |
    | `<=` | Less than or equal |
    | `>` | Greater than |
    | `<` | Less than |
    | `is` | Identity |
    | `is not` | Negative identity |
    | `in` | Inclusion in sequence |

    The `is` and `is not` are potentially confusing as they are not about being equal but being **exactly the same thing**.

    Finally, different Boolean comparisons can be compound through standard logic operators:

    | Operator
    | --- |
    | `and` |
    | `or` |
    | `not` |
    | `any([Sequence])` |
    | `all([Sequence])` |

    Most of them are quite intuitive but the following cell with explore some more interesting examples.
    """)
    return


@app.cell
def _():
    elements = ["H", "He", "Na", "Be", "B", "C", "N"]

    print(f"Test for inclusion of hydrogen in elements: {"H" in elements}.")
    print(f"Test for inclusion of oxygen in elements: {"O" in elements}.")

    print(f"8 is equal to 8.0: {8 == 8.0}.")
    print(f"8 is 8.0: {8 is 8.0}.")

    print(f"Eight is a non-negative integer: {8 >= 0 and type(8) is int}")
    print(f"All of those are true: {all([True, True, False])}")
    print(f"Any of those is true: {any([True, True, False])}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## `if` statements

    We use the `if`-`else` statement when we want to conditionally execute different blocks of code. The overall syntax roughly follows simple English sentence structure - note the indents and colons:

    ```python
    if CONDITION:
        block to execute if CONDITION is True

    elif OTHER_CONDITIONS:
        block to execute if CONDITION is not True
        but OTHER_CONDITION is True

    else:
        block to execute if no condition is True
    ```
    """)
    return


@app.function
def check_pH(
    pH : float
) -> None:
    if pH == 7:
        print('The solution is neutral.')
    elif pH > 7:
        print('The solution is basic.')
    else:
        print('The solution is acidic.')


@app.cell
def _():
    check_pH(6)
    check_pH(7)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Let's now try to solve a simple problem. We want to figure out whether there is Co or Fe in a formula, or maybe neither?

    > **Hint**: remember that strings are basically sequences of characters, so you can use the inclusion operator!
    """)
    return


app._unparsable_cell(
    """
    def check_elements(
        formula : str
    ) -> str:
        \"\"\"Check if there is Fe or Co in the formula.\"\"\"
        if # FIXME: check for Co
            return f\"Cobalt is in {formula}.\"
        elif # FIXME: else check for Fe
            return f\"Iron is in {formula}.\"
        else:
            return f\"None are in {formula}.\"

    prussian_blue = \"Fe4[Fe(CN)6]3\"

    check_elements(prussian_blue)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(check_elements, prussian_blue):
    def str_check_pass():
        exercise_1_passed = False

        try:
            exercise_1_passed = check_elements(prussian_blue) == "Iron is in Fe4[Fe(CN)6]3."

            if exercise_1_passed:
                return mo.callout("✅ Correct!", kind="success")
            else:
                return mo.callout("❌ Not quite.", kind="danger")

        except Exception as e:
            return mo.callout(f"❌ Python error: {e}", kind="danger")

    str_check_pass()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## `for` loops

    Loops allow us to execute the same code multiple times. This is then programming becomes really powerful, allowing you to redo the same operation thousands (or more!) times. The `for` loops is the most common loop used in Python. It basically goes over an _iterator_ and executes until it has exhausted the sequence. The overall structure is:

    ```python
    for LOOP_VARIABLE in ITERATOR:
        ...
    ```

    It is important to remember that the loop variable is taken from the iterator, so will have different value every time.
    """)
    return


@app.cell
def _():
    for value in [4, 2, 0, "a", "b", "c"]:
        print(value * 2)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    It is very common to want to keep track of which iteration of the loop we are going through. For example, imagine that for some reason we want to raise numbers to the powers that correspond to their position in a sequence. The `enumerate()` function is used for that and it returns a tuple `(counter, element)`, where the `counter` starts from 0.
    """)
    return


@app.cell
def _():
    numbers = [2, 4, 6, 0, 1]

    for i, number in enumerate(numbers):
        print(f"{number} to the power of {i}: {number ** i}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Ranges

    A useful sequence to iterate over is a range of integers, we can do it with the `range()` function. Maybe we want to know how much $^{235}$U is left aftert six half-lives?

    > **Note**: in Python we can update the value of a variable in one line, e.g., `x = x + 1` (or even shorter `x += 1`) will increment `x` by 1.

    > **Convention**: it is common in Python to just want to repeat some code `N` times without using the variable, in which case we can just "ignore" the loop counter and use `for _ in range(N)`.
    """)
    return


app._unparsable_cell(
    """
    def uranium_left(
        initial_mass : float,
        half_lives: int,    
    ) -> float:
        \"\"\"Get mass of uranium after given number of half-lives.

        Arguments
        ---------
        initial_mass
            The original mass of the sample (in grams).

        half_lives
            Number of half-lives.

        Returns
        -------
        Mass of the sample after half_lives half-lives.

        \"\"\"

        mass = initial_mass
        for _ in range(half_lives):
            mass = # FIXME: half the amount of uranium per loop iteration

        return mass

    uranium_sample = 255.4
    print(f\"Uranium left after six half-lives is: {uranium_left(half_lives=6, initial_mass=uranium_sample):.2f} g.\")
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(uranium_left, uranium_sample):
    def uranium_pass():
        uranium_passed = False

        try:
            uranium_passed = abs(uranium_left(uranium_sample, 6) - 3.990625) < 0.1
            if uranium_passed:
                return mo.callout("✅ Correct!", kind="success")
            else:
                return mo.callout("❌ Not quite.", kind="danger")

        except Exception as e:
            return mo.callout(f"❌ Python error: {e}", kind="danger")

    uranium_pass()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Ranges can also get more exciting and the complete syntax is:

    ```python
    range(start, stop, step)
    ```

    Where `start` (inclusive) defaults to `0`, `stop` (exclusive) is required, and `step` defaults to `1`.
    """)
    return


@app.cell
def _():
    for a in range(3, 43, 4):
        print(f"Weird element from the range: {a}.")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Nested loops

    As en exercise, let's try to implement the famous _bubble sort_ algorithm. It's visualised here in a video as a [Hungarian folk dance](https://www.youtube.com/watch?v=lyZQPjUT5B4). When thinking about algorithms, it's very useful to write out some psuedocode that expains what it would do. It is also common to visualise them with diagrams, a nice online tool for that is [draw.io](https://www.drawio.com/). Designing what your code will do is the **critical step** - implementing it in Python is usually the easy bit. There are lots of tools and articles online that help you implement what you have in mind - but you need to learn the basics to **know what questions to ask**!

    Pseudocode for bubble sort could look something like this:

    ```
    Get the Total_Length of the list

    For each Pass from 1 to Total_Length:
        For each Item_Index from 0 to (Total_Length - Pass):

            Look at list[Item_Index] and list[Item_Index+1]

            IF list[Item_Index] is GREATER THAN list[Item_Index+1]:
                Swap their positions

            ELSE:
                Leave them alone and move to the next pair
    ```
    """)
    return


app._unparsable_cell(
    r"""
    def sort_masses(mass_list):
        # How many times do we need to loop
        n = # FIXME: need to go through all elements of the list

        for i in range(1,n):
            for j in # FIXME: we want to go total_length - already passed
                # FIXME:
                # 1. Compare mass_list[j] and mass_list[j+1]
                # 2. If the left one is greater than the right one, swap them
                #    (you will need some temporary variable to store one value)
            # Now i last elements mass_list[:-i] should be sorted
        # Now all of mass_list is sorted

        return mass_list

    # Unsorted atomic masses: He, Ne, Ar, Kr, Xe
    masses = [39.948, 20.180, 131.293, 4.0026, 83.798]
    masses = sort_masses(masses)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(masses):
    # The correct order
    def sort_feedback():
        expected = [4.0026, 20.18, 39.948, 83.798, 131.293]
        sort_passed = False

        try:
            sort_passed = (masses == expected)
            if sort_passed:
                return mo.callout("✅ Correct! The noble gases are now ordered by mass.", kind="success")
            else:
                return mo.callout("❌ Not quite.", kind="danger")

        except Exception as e:
            return mo.callout(f"❌ Python error: {e}", kind="danger")

    sort_feedback()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Dictionaries are also iterable, we can write `for` loops that perform some actions for each element of the dictionary. There is a number of different ways to do so - we might be interested in just the keys (e.g., to create a new dictionary with the same keys), just the values, or all the pairs.
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
    return (masses_dict,)


@app.cell
def _(masses_dict):
    print("-" * 25)
    print("Iterating over keys.")
    print("-" * 25)

    for name in masses_dict:
        print(f"Element is: {name}.")

    print()
    print("-" * 25)
    print("Iterating over values.")
    print("-" * 25)

    for mass in masses_dict.values():
        print(f"Element's mass is: {mass}.")

    print()
    print("-" * 25)
    print("Iterating over both.")
    print("-" * 25)

    for name, mass in masses_dict.items():
        print(f"Mass of {name} is {mass}.")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## `while` loops

    Those are somewhat common but can lead to faulty termination if the condition is not carefully checked. The syntax is:

    ```python
    while CONDITION:
        block executed when condition is True
    ```

    It is imperative to ensure that the condition can actually terminate and that something is changed as part of the execution - otherwise the loop will go on forever! I personally do not really use them for that reason.
    """)
    return


@app.cell
def _():
    uranium_mass = 255.4
    hl_counter = 1

    while uranium_mass > 10:
        uranium_mass = uranium_mass / 2
        print(f"After {hl_counter} half-lives, there is {uranium_mass} g of uranium left.")

        hl_counter += 1

    print("That is less than 10 g, so we stop now!")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Controlling the loops: `break` and `continue`

    Sometimes (again, quite rarely) you might want to stop going through the loop because some other condition has been satisfied. Common example is going through the text file line by line until you find a line that implicates your data has been loaded.

    Let's re-write the `while` loop from the previous example to now use `break`. Also, see how useful it could be to define it as a function - we might often want to end up with different final mass of uranium or maybe our starting sample is smaller! So let's define those as optional arguments. Functions are the best and help you expand your code over a long project with ease 😊
    """)
    return


@app.cell
def _():
    def uranium_counter(
        uranium_mass = 255.4,
        minimum_mass = 10,
        maximum_iterations = 20,
    ):
        for half_life in range(maximum_iterations):
            uranium_mass = uranium_mass / 2
            if uranium_mass <= minimum_mass:
                break

        print(
            f"We have less than {minimum_mass} g ({uranium_mass:.2f} g actually) "
            f"of uranium after {half_life+1} half-lives. Stopping."
        )

    uranium_counter()
    uranium_counter(uranium_mass=40, minimum_mass=0.2)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    The `continue` statement is similar but will just stop the current loop block and move onto the next iteration. Could be useful when we want to selectively perform an expensive calculation. Though honestly, you might as well just use a simple `if`-`else` clause for that.
    """)
    return


@app.cell
def _():
    def square_squares(
        stop=50
    ):
        for number in range(stop):
            if number % 2 == 1:
                continue
            print(f"Square of {number} is {number ** 2}.")

    square_squares()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Finally, sometimes you might come across a `pass`. This does nothing - developers use it as placeholders for empty code blocks so that some tests might pass but functions will need to be implemented:

    ```python
    def complex_function(a):
        pass

    def square_function(a):
        return complex_function(a) ** 2
    ```

    In this example, we have implemented the squaring function and left the complex function to be done later. Finished code rarely has `pass` statements.
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Advanced topics

    ## Error handling

    This is a **more advanced** topic. You might want to skip it on your first read-through. You might have noticed that sometimes code does not work: an _exception_ is thrown. Once an error like this happens, the script breaks and is no longer executed. Sometimes we don't want that to happen - maybe we want to use a default value instead or we want to print the error to the screen and continue with some later analysis.

    There are many [built-in errors](https://docs.python.org/3/library/exceptions.html) that we can encounter and we can also define new errors (inheriting from the `Exception` class) as developers. To work around exceptions we use the `try`-`except` clauses:

    ```python
    try:
        block of code

    except Exception:
        contingency code

    finally:
        code to be executed nonetheless
    ```

    It _might_ become a bit more obvious with the following example.
    """)
    return


@app.cell
def _():
    def division(num, denom):
        try:
            return num / denom
        except ZeroDivisionError:
            print("DIVISION: ZeroDivisionError - keep the numerator.")
            return num

    def error_example(numerator):
        denominators = [1, 2, 3, 4, "5", 6, 0, "NA"]
        for x in denominators:
            try:
                value = division(numerator, x)
            except TypeError:
                print("EXAMPLE: Wrong type, try casting as int.")
                try:
                    value = division(numerator, int(x))
                except Exception:
                    print("EXAMPLE: No idea what happened - return -1.")
                    value = -1
            finally:
                print(f"Input: 1 / {x}, output: {value:.3f}.")

    error_example(1)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Raising exceptions

    For completeness, you might want to raise some errors in your code. A common example would be when some input file is missing and you want to notify the user, or maybe some operation makes no chemical sense, even if it is mathematically possible. Let's consider calculating pressure of the ideal gas:

    \[
    p = \frac{nRT}{V}
    \]

    We would want to make sure that we do not get any negative argument - it makes no sense to be below 0 K, at negative volume or with negative number of moles!
    """)
    return


@app.cell
def _():
    def calculate_pressure(
        moles,
        temp_kelvin,
        volume_litres,
    ):
        """Calculate pressure in atmospheres."""
        R = 0.082057

        if temp_kelvin < 0:
            raise ValueError(f"Temperature ({temp_kelvin} K) is below absolute zero!")

        if moles < 0:
            raise ValueError(f"Cannot have negative moles ({moles}).")

        if volume_litres <= 0:
            # We raise a more specific error here
            raise ValueError(f"Volume must be positive. Provided: {volume_litres} L.")

        pressure = (moles * R * temp_kelvin) / volume_litres
        return pressure

    try:
        calculate_pressure(20, -5, 10)

    except Exception as e:
        print(f"Error encountered: {e}")
    return


if __name__ == "__main__":
    app.run()
