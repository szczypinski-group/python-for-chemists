# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo",
# ]
# ///
import marimo

__generated_with = "0.23.8"
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

    We use the `if`-`else` statement when we want to conditionally execute different blocks of code. The overall syntax roughly follows simple English sentence structure - note the idents and colons:

    ```python
    if CONDITION:
        block to execute if CONDITION is True

    elif OTHER_CONDITIONS:
        block to execute if CONDITION is not True
        but OTHER_CONDITION is True

    else:
        block to execuite if no condition is True
    ```
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Indentation

    In some programming languages, blocks of code are enclosed in curly brackets or isolated some other way. In Python, we use whitespaces (tabs and spaces) for that - there are no strict rules, but you have to be consistent. I recommend a single tab (converted to four spaces) as the indentation pattern - this is the default in most notebooks and editors.

    ```python
    # This is the default code level

    import math

    a = 100

    if a > 0:
        # Everything at this indent level is a block
        print("We are inside now")
        if a > 10:
            # And this is another indented block
            print("We are even more inside")
        # Back to the previous level (same block!)
        print(a)

    # Back to the default level
    # Rest of the code ...

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
    Let's now try to solve a simple problem. We want to figure out whether it is Co or Fe that makes up Prussian blue, or maybe neither?

    > **Hint**: remember that strings are basically sequences of characters, so you can use the inclusion operator!
    """)
    return


app._unparsable_cell(
    """
    prussian_blue = \"Fe4[Fe(CN)6]3\"

    def check_blue(
        formula : str
    ) -> str:
        \"\"\"Check if there is Fe or Co in the formula.\"\"\"
        if # COMPLETE HERE
            return \"Cobalt is in Prussian blue.\"
        elif # COMPLETE HERE
            return \"Iron is in Prussian blue.\"
        else:
            return \"None are in Prussian blue.\"
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(check_blue, prussian_blue):
    exercise_1_passed = False

    try:
        exercise_1_passed = check_blue(prussian_blue) == "Iron is in Prussian blue."

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
    It is very common to want to keep track of which iteration of the loop we are going through. For example, imagine that for some reason we want to raise numbers to the powers that correspond to their position in a sequence.
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
    """)
    return


app._unparsable_cell(
    """
    uranium_sample = 255.4

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
        for x in range(half_lives):
            mass =  # COMPLETE HERE

        return mass
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(uranium_left, uranium_sample):
    uranium_passed = False

    try:
        uranium_passed = abs(uranium_left(uranium_sample, 6) - 3.990625) < 0.1

    except Exception:
        uranium_passed = False

    if uranium_passed:
        uranium_feedback = mo.callout("✅ Correct!", kind="success")
    else:
        uranium_feedback = mo.callout("❌ Not quite.", kind="danger")

    uranium_feedback
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
