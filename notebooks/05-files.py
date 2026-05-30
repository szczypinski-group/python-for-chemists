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

    On your own computer, you would ideally know where the files you want to interact with are. As those workshop notebooks live in your browser memory, you need to specify locations exactly (or drop the files into temprary cache in the "Files" tab). The `mo.notebook_location()` function can be used for this here but it is a bit funny with network locations. So we will save files directly in the "current working directory"
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Reading and writing files

    In the programming world we have to **open** and **close** files to make sure everything works properly. In Python, we should deal with files using the `with` environment - it will do the opening and closing operations for us automatically. We can open the file in one of three main modes: "r"ead, "w"rite (replaces the content), and "a"ppend (adds to the content).

    ```python
    with open(FILE_PATH, MODE) as f:
        operations (f is the local variable for the file)
    ```
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Writing example files

    Let's start by writing some files to local memory. Of course, on your computer you would probably have some files already present! I have created some files (content in the hidden celll below) to use throughout this workshop.
    """)
    return


@app.cell(hide_code=True)
def _():
    csv_data = """Entry,Substrate,Catalyst,Solvent,Temp_C,Yield_Percent,ee_Percent
    1,CC(=O)c1ccccc1,3375-31-3,DCM,25.5,82,94
    2,CC(=O)c1ccccc1,3375-31-3,THF,25.2,45,88
    3,CC(=O)c1ccccc1,3375-31-3,Toluene,59.6,91,92
    4,CC(=O)c1ccccc1,14694-95-2,DCM,24,0,nd
    5,CC(=O)c1ccccc1,14694-95-2,THF,60.2,12,40
    6,O=Cc1ccccc1,3375-31-3,DCM,25.1,78,91
    7,O=Cc1ccccc1,3375-31-3,MeCN,78.5,5,nd
    8,O=Cc1ccccc1,1295-35-8,DCM,-5.5,55,98"""

    json_data = """[
      {"Entry": 1, "Substrate": "CC(=O)c1ccccc1", "Catalyst": "3375-31-3", "Solvent": "DCM", "Temp_C": 25.5, "Yield": 82, "ee": 94},
      {"Entry": 2, "Substrate": "CC(=O)c1ccccc1", "Catalyst": "3375-31-3", "Solvent": "THF", "Temp_C": 25.2, "Yield": 45, "ee": 88},
      {"Entry": 3, "Substrate": "CC(=O)c1ccccc1", "Catalyst": "3375-31-3", "Solvent": "Toluene", "Temp_C": 59.6, "Yield": 91, "ee": 92},
      {"Entry": 4, "Substrate": "CC(=O)c1ccccc1", "Catalyst": "14694-95-2", "Solvent": "DCM", "Temp_C": 24.0, "Yield": 0, "ee": "nd"},
      {"Entry": 5, "Substrate": "CC(=O)c1ccccc1", "Catalyst": "14694-95-2", "Solvent": "THF", "Temp_C": 60.2, "Yield": 12, "ee": 40},
      {"Entry": 6, "Substrate": "O=Cc1ccccc1", "Catalyst": "3375-31-3", "Solvent": "DCM", "Temp_C": 25.1, "Yield": 78, "ee": 91},
      {"Entry": 7, "Substrate": "O=Cc1ccccc1", "Catalyst": "3375-31-3", "Solvent": "MeCN", "Temp_C": 78.5, "Yield": 5, "ee": "nd"},
      {"Entry": 8, "Substrate": "O=Cc1ccccc1", "Catalyst": "1295-35-8", "Solvent": "DCM", "Temp_C": -5.5, "Yield": 55, "ee": 98}
    ]"""


    toml_data = """[[reactions]]
    Entry = 1
    Substrate = "CC(=O)c1ccccc1"
    Catalyst = "3375-31-3"
    Solvent = "DCM"
    Temp_C = 25.5
    Yield = 82
    ee = 94

    [[reactions]]
    Entry = 2
    Substrate = "CC(=O)c1ccccc1"
    Catalyst = "3375-31-3"
    Solvent = "THF"
    Temp_C = 25.2
    Yield = 45
    ee = 88

    [[reactions]]
    Entry = 3
    Substrate = "CC(=O)c1ccccc1"
    Catalyst = "3375-31-3"
    Solvent = "Toluene"
    Temp_C = 59.6
    Yield = 91
    ee = 92

    [[reactions]]
    Entry = 4
    Substrate = "CC(=O)c1ccccc1"
    Catalyst = "14694-95-2"
    Solvent = "DCM"
    Temp_C = 24.0
    Yield = 0
    ee = "nd"

    [[reactions]]
    Entry = 5
    Substrate = "CC(=O)c1ccccc1"
    Catalyst = "14694-95-2"
    Solvent = "THF"
    Temp_C = 60.2
    Yield = 12
    ee = 40

    [[reactions]]
    Entry = 6
    Substrate = "O=Cc1ccccc1"
    Catalyst = "3375-31-3"
    Solvent = "DCM"
    Temp_C = 25.1
    Yield = 78
    ee = 91

    [[reactions]]
    Entry = 7
    Substrate = "O=Cc1ccccc1"
    Catalyst = "3375-31-3"
    Solvent = "MeCN"
    Temp_C = 78.5
    Yield = 5
    ee = "nd"

    [[reactions]]
    Entry = 8
    Substrate = "O=Cc1ccccc1"
    Catalyst = "1295-35-8"
    Solvent = "DCM"
    Temp_C = -5.5
    Yield = 55
    ee = 98
    """


    return csv_data, json_data, toml_data


@app.cell
def _(csv_data, json_data, toml_data):
    with open("reaction_screening.csv", "w") as _file:
        _file.write(csv_data)

    with open("reaction_screening.json", "w") as _file:
        _file.write(json_data)

    with open("reaction_screening.toml", "w") as _file:
        _file.write(toml_data)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Reading files

    You might remember that strings are basically sequences of characters - in Python files are sequences of lines. So we can iterate over them quite easily.
    """)
    return


@app.cell
def _():
    with open("reaction_screening.csv", "r") as _file:
        for line in _file:
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

        with open("reaction_screening.csv") as f:
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
                    else:
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
    ## Other useful formats

    This section is a bit **more advanced** - you might want to skip it, but if you are interested there is lots of useful real-world stuff here!

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

    [`JSON`](https://en.wikipedia.org/wiki/JSON) and [`TOML`](https://toml.io/en/) files are great way of storing data in a more structured way than just `CSV`. JSON files look very similar to (potentially nested) dictionaries and can be reasonably human-readable. There even exist standard library modules for dealing with those files - that's how common they are! I recommend using the standard libraries, as they will also figure out the type of data and the overall structures (dictionaries, lists).
    """)
    return


@app.cell
def _():
    import json

    with open("reaction_screening.json", "r") as _file:
        # Loads JSON file - as lists and dictionaries directly!
        reaction_json = json.load(_file)

    reaction_json
    return json, reaction_json


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Let's see how easy it is to access structured data like this:
    """)
    return


@app.cell
def _(reaction_json):
    reaction_json[2]["ee"]
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Or maybe we want to know the name of the catalyst that produced the highest yield?
    """)
    return


@app.cell
def _(catalysts_dict, reaction_json):
    # Identify the maximum using the value of the "Yield" for comparisons
    best_reaction = max(reaction_json, key=lambda x: x["Yield"])

    # Look up the catalyst in our human-friendly dictionary
    print(
        "Highest-yielding catalyst was "
        f"{catalysts_dict[best_reaction["Catalyst"]]}."
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    We can load data from TOML files in the same way. The only difference is that the file needs to be opened in the "binary" format (`mode="rb"). There is no functionality in the standard library to write TOML files yet. But those are very easy to modify by hand, they are more difficult to "break" than JSON files.

    In this example, we load the data from a TOML file. We will now end up with a list called `reactions`, but otherwise it is all equivalent.
    """)
    return


@app.cell
def _():
    import tomllib

    with open("reaction_screening.toml", "rb") as _file:
        # Loads JSON file - as lists and dictionaries directly!
        reaction_toml = tomllib.load(_file)

    reaction_toml
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Finally, let's save our `catalysts_dict` to a JSON file - so that we can easily use it in the future. Or maybe we will want to expand it by some other properties related to each catalyst, apart from the name - molecular weight could be useful when automating calculations involving masses and concentrations.

    The `json.dump()` function is used to convert any Python object (including dictionaries and lists) into a JSON string, and then save it to a file. If you want to just get the string, you can use `json.dumps()`.
    """)
    return


@app.cell
def _(catalysts_dict, json):
    with open("catalysts.json", "w") as _file:
        json.dump(catalysts_dict, _file)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Modules to deal with files

    This is another **more advanced topic** and it involves file management.
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### `pathlib`

    You might have noticed, that in the examples above we are "dividing" the output of `mo.notebook_location()` by a string to specify a file notation. This is actually not standard Python - this functionality comes from the [`pathlib` library](https://docs.python.org/3/library/pathlib.html). It is an extremely powerful library to deal with file paths in an [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming) way. The take home message is that it is platform-independent (you remember how on Windows paths look something like `C:\Documents\file.txt` and on Linux they would use forward slashes instead, e.g. `/home/Filip/Documents` - that can cause troubles if you treat paths like strings) and allows you to reach any part of the file path, add extra paths, check if things exist, etc.

    We will not go through this library in any level of details, I recommend reading up if you are interested. But here are some examples. I also use those examples in the later parts of the course, to expose you to "more modern way" of scripting in Python.

    You can think of `Path` as another "type" - we chemists are good at it, it's like a "mole", yet another unit!
    """)
    return


@app.cell
def _():
    from pathlib import Path

    # Path is the "base" object of the library

    print(f"Current working directory is: {Path.cwd()}")
    print(f"Its parent directory is: {Path.cwd().parent}")

    # We can create new paths using the division operator

    _file = Path.cwd() / "example_file.txt"
    print(f"Imagine file: {_file}")
    print(f"The filename is: {_file.name}")
    print(f"It also has a stem ({_file.stem}) and a suffix ({_file.suffix}).")
    print(f"So we can create a new file: {_file.with_suffix(".doc")}")
    print(f"But does it exist? {_file.with_suffix(".doc").exists()}")
    return (Path,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    We can then do a whole range of standard file operators using methods such as `touch()`, `mkdir()`, `copy()`, or `unlink()`.
    """)
    return


@app.cell
def _(Path):
    example_dir = Path.cwd() / "test_directory"

    # This command will create a new directory
    # At the path we just defined
    # It will do nothing if it already exists (exist_ok)
    # And it will create parent directories if needed

    example_dir.mkdir(exist_ok=True, parents=True)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    We can also find files that match a pattern with `glob()` - remember `mo.notebook_location() ` is a `Path`!
    """)
    return


@app.cell
def _(Path):
    for json_f in Path.cwd().glob("*.json"):
        print(json_f.name)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Importantly, `pathlib` is a great way of reading and writing into files. The `Path.read_text()` and `Path.write-_text()` methods do all the file opening and closing operations - making the code much cleaner and without all those `with` statements we had above.
    """)
    return


@app.cell
def _(Path):
    catalysts_json = (Path.cwd() / "catalysts.json").read_text()
    print(catalysts_json)
    return


@app.cell
def _(Path):
    yet_anoter_file = Path.cwd() / "final_file.txt"

    yet_anoter_file.write_text("The quick brown fox jumps over the lazy dog.")
    yet_anoter_file.read_text()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Finally, we have created quite a lot of files. Lets remove them all.
    """)
    return


@app.cell
def _(Path):
    to_delete = [
        Path.cwd() / "catalysts.json",
        Path.cwd() / "final_file.txt",
        Path.cwd() / "test_directory/"
    ]

    for screen in Path.cwd().glob("reaction_screening.*"):
        to_delete.append(screen)

    for del_file in to_delete:
        if del_file.is_file():
            del_file.unlink()
        elif del_file.is_dir():
            del_file.rmdir()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### `shutil`

    If you need more advanced control over filesystem operations, then the [`shutil`](https://docs.python.org/3/library/shutil.html) library can help a lot. We won't cover it at all, but it has some other useful functionality like copying metadata or removing entire directory trees. If you are interested in that, feel free to read the documentation.
    """)
    return


if __name__ == "__main__":
    app.run()
