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
    # Working with files

    Most data from instruments will already come as some type of files. There are good ods these are **comma-separated value** (CSV) files. You can also export CSV files from Excel or LibreOffice. We will focus on CSV files as they are really common and reasonably easy to read: each line of the text file is a different row, and each item in a row is separated by commas.

    Here is an example CSV file containing reaction optimisation trials:

    ```csv
    Entry,Substrate,Catalyst,Solvent,Temp_C,Yield_Percent,ee_Percent
    1,CC(=O)c1ccccc1,3375-31-3,DCM,25.5,82,94
    2,CC(=O)c1ccccc1,3375-31-3,THF,25.2,45,88
    3,CC(=O)c1ccccc1,3375-31-3,Toluene,59.6,91,92
    4,CC(=O)c1ccccc1,14694-95-2,DCM,24,0,nd
    5,CC(=O)c1ccccc1,14694-95-2,THF,60.2,12,40
    6,O=Cc1ccccc1,3375-31-3,DCM,25.1,78,91
    7,O=Cc1ccccc1,3375-31-3,MeCN,78.5,5,nd
    8,O=Cc1ccccc1,1295-35-8,DCM,-5.5,55,98

    ```

    You can see it contains seven columns:

    1. **Entry**: those are integer identifiers of the reaction.
    2. **Substrate**: molecules represented as [SMILES](https://en.wikipedia.org/wiki/Simplified_Molecular_Input_Line_Entry_System) strings (you will learn about those).
    3. **Catalyst**: represented as [CAS numbers](https://en.wikipedia.org/wiki/CAS_Registry_Number).
    4. **Solvent**: a simple string with solvent name.
    5. **Temp_C**: temperature in Celsius as a float.
    6. **Yield_Percent**: reaction yield.
    7. **ee_Percent**: enantiomeric excess as an integer (or "nd" if _not determined_).

    > **Note**: I generated this table with AI so it makes no chemical sense. It is just meant to have different data types to demonstrate some functions.

    ## Notebooks and local scripting

    On your own computer, you would ideally know where the files you want to interact with are. As those workshop notebooks live in your browser memory, you need to specify locations exactly (or drop the files into temprary cache in the "Files" tab). The `mo.notebook_location()` function is used for this here.
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Reading files

    In the programming world we have to **open** and **close** files to make sure everything works properly. In Python, we should deal with files using the `with` environment - it will do the opening and closing operations for us automatically. We can open the file in one of three main modes: "r"ead, "w"rite (replaces the content), and "a"ppend (adds to the content).

    ```python
    with open(FILE_PATH, MODE) as f:
        operations (f is the local variable for the file)
    ```

    You might remember that strings are basically sequences of characters - in Python files are sequences of lines. So we can iterate over them quite easily.
    """)
    return


@app.cell
def _():
    with open(mo.notebook_location() / "public" / "reaction_screening.csv", "r") as file:
        for line in file:
            print(line)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    As a simple exercise, let's generate a set (a collection of objects without repeats) of our substrates (_substrate scope_) and a list of enantiomeric excesses where the not determined entries are replaced with zeros.
    """)
    return


app._unparsable_cell(
    r"""
    def cleanup_screening():
        substrates = set()
        ees = []

        with open(mo.notebook_location() / "public" / "reaction_screening.csv") as f:
            for line in f:
                # Continue in the loop if "Entry" is in the current line
                if # COMPLETE HERE :
                    # COMPLETE HERE
                else:
                    # Identify the SMILES string in the line
                    smiles = # COMPLETE HERE
                    # Add the SMILES to a set: set.add()
                    substrates.add(smiles)

                    # Identify the ee in the line and remove whitespaces
                    ee = # COMPLETE HERE

                    if ee == "nd":
                        ee = 0
                    elif:
                        ee = int(ee)

                    # Those four lines can be simply replaced with:
                    # ee = int(ee) if ee != "nd" else 0

                    ees.append(ee)
                
        return substrates, ees
    
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(cleanup_screening):
    cleanup_passed = False

    try:
        substrates, ees = cleanup_screening()
        substrates_passed = substrates == {"CC(=O)c1ccccc1", "O=Cc1ccccc1"}
        ees_passed = ees == [94, 88, 92, 0, 40, 91, 0, 98]

        cleanup_passed = substrates_passed and ees_passed

    except Exception:
        cleanup_passed = False

    if cleanup_passed:
        cleanup_feedback = mo.callout("✅ Correct!", kind="success")
    else:
        cleanup_feedback = mo.callout("❌ Not quite.", kind="danger")

    cleanup_feedback
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Writing files

    The following example should be reasonably straightforward now.
    """)
    return


@app.cell
def _():
    def writing_example():
        ees = [94, 88, 92, 0, 40, 91, 0, 98]

        with open(mo.notebook_location() / "public" / "example_file.txt", "w") as file:
            ees_string = str(ees)
            file.write(ees_string)

    writing_example()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Other useful formats

    This section is a bit more advanced - you might want to skip it, but if you are interested there is lots of useful real-world stuff here!

    ### Dictionaries

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
    catalysts_dict = {
        "3375-31-3": "Pd(OAc)2",
        "14694-95-2": "Rh(PPh3)3Cl",
        "1295-35-8": "Ni(cod)2"
    }
    return (catalysts_dict,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    As they are also an iterable, we can write `for` loops that perform some actions for each element of the dictionary. There is a number of different ways to do so - we might be interested in just the keys (e.g., to create a new dictionary with the same keys), just the values (because we don't understand CAS numbers), or all the pairs.
    """)
    return


@app.cell
def _(catalysts_dict):
    print("-" * 25)
    print("Iterating over keys.")
    print("-" * 25)

    for cas in catalysts_dict:
        print(f"CAS number is: {cas}.")

    print("\n", "-" * 25)
    print("Iterating over values.")
    print("-" * 25)

    for cat_name in catalysts_dict.values():
        print(f"Catalyst is: {cat_name}.")

    print("\n", "-" * 25)
    print("Iterating over both.")
    print("-" * 25)

    for cas, cat_name in catalysts_dict.items():
        print(f"Catalyst with CAS of {cas} is: {cat_name}.")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### JSON and TOML

    [`JSON`](https://en.wikipedia.org/wiki/JSON) and [`TOML`](https://toml.io/en/) files are great way of storing data in a more structured way than just `CSV`. JSON files look very similar to (potentially nested) dictionaries and can be reasonably well.
    """)
    return


if __name__ == "__main__":
    app.run()
