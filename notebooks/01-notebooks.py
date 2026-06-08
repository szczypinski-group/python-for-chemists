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

    ## Using `marimo` as a standalone tool

    If you don't want to use the browser-based notebooks in the future but have a locally availably `marimo` notebooks, you can install them locally as a standalone tool (that is what I do).

    > **Note**: this cannot be done on University-managed Windows machines yet. You can do it on Linux or on your personal computer.

    For installing anything Python-related, I **very strongly recommend** the `uv` package (unfortunately, you cannot get it from AppsAnywhere yet). Installation instructions for all platforms are [here](https://docs.astral.sh/uv/getting-started/installation/). Once you have `uv` installed, you can use marimo extremely easily - check the [website](https://docs.astral.sh/uv/guides/integration/marimo/) for instructions but they basically boil down to typing:

    ```sh
    uvx marimo edit
    ```
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Git and version control

    Modern coding projects use [version control](https://en.wikipedia.org/wiki/Version_control) for controlling and tracking different version of the source code. Probably the most widespread version control system is [Git](https://en.wikipedia.org/wiki/Git) - it was developed by Linus Torvalds for the development of the Linux kernel.

    ## GitHub

    GitHub is one of the most populars developer platforms for storing, managing, and sharing code. It uses Git and provides a number of other useful features. Since 2018 it has been owned by Microsoft, so feel free to [explore alternatives](https://european-alternatives.eu/category/version-control-services) if you disagree with Microsoft practices.

    My recommendation for my research group is that **all **code development should be done with version control on GitHub - you might have noticed that these workbooks are also a GitHub repository! Best practice is to work on the non-`main` branch for any actual development and then create a "pull request" for the tested code to be included in the main branch. For more information about how to use GitHub, see: https://docs.github.com/en/get-started/start-your-journey/hello-world/.

    > **Recommendation**: If you do not have a GitHub account, it is a good idea to create one now. Go to https://github.com/, sign up, create a new (private if you wish) repository called "python-introduction", and upload this notebook there. You can use it as a base for all Python in these workbooks and then create new repositories if needed, e.g., for lab write-ups or your MChem project!
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Python projects: complete workflow

    This is a **_much_ more advanced topic**. You might want to skip it as you will not be able to currently do this on a University-managed Windows computer. However, I am including it for your future reference as I believe it is very important and useful. You should be able to do it on a Linux machine or your personal computer.

    For implementing different versions of Python and packages, use the `pip` interface from the `uv` package. Installation instructions for all platforms are [here](https://docs.astral.sh/uv/getting-started/installation/). Most of your code should probably be what `uv` considers a [library](https://docs.astral.sh/uv/concepts/projects/init/#libraries), i.e. isolated code with `src` layour, `py.typed` indicator, and metadata stored in a `pyproject.toml` file.

    ```sh
    uv init --lib YOUR-PROJECT
    ```

    And that is basically it. For any dependency (e.g. `matplotlib`) just use:

    ```sh
    uv add matplotlib
    ```

    If you want the dependency to only be added to a specific group (e.g., developer dependencies are only installed if you get you software as `pip install package[dev]`):

    ```sh
    uv add --dev pre-commit
    ```

    > **Note**: have a look at our [pyMultiwfn repository](https://github.com/szczypinski-group/pyMultiwfn) for a real-life example. In particular, have a look at the contents of the `.pre-commit-config.yaml` (which defines the settings of `pre-commit`) and the `pyproject.toml` file (all other metadata, including Python versions, linting settings, etc.). Don't worry about `uv.lock` - this is added automatically by `uv`. I highly recommend having a `README.md` (which is then rendered on the GitHub repository main page) and `LICENSE` (for copyright protection).

    ## Depositing with GitHub

    Once you have created your code, it is important to add in to GitHub. Create a **new repository** (top right), give it a name, and set its visibility (probably **Private** to begin with). **Do not initialise** with any files (README, etc.) as you will already have them on your local computer.

    Then, on your local machine where you crated the code (see section above):

    ```sh
    # Navigate to the folder
    cd PATH/TO/YOUR-PROJECT
    # Initialise the repository
    git init
    # Set up the main branch
    git branch -M main
    ```
    
    You might want to add files to `.gitignore` so that theyy are not versioned by git, you can do it by editing the file or from the command line e.g.:

    ```sh
    echo "__pycache__/" > .gitignore
    ```

    And when you are ready, make the first commit:

    ```sh
    # Stage all modified files
    git add .
    # Commit with a message
    git commit -m "Initial commit"
    ```

    You will also need to add the GitHub repository as `remote`. Copy the address from GitHub (big `<> Code` button) and then:

    ```sh
    git remote add origin git@github.com:USERNAME/your-repo-name.git
    git push -u origin main
    ```
   
    ## Linting and testing

    As mentioned above, make sure you have `ruff` installed:

    ```sh
    uv tool install ruff@latest
    uv add --dev ruff
    ```
    
    and same for `pre-commit`:

    ```sh
    uv add --dev pre-commit
    uv run pre-commit install
    ```

    Now `git` will stop you from committing code that does not conform to the standards set up in the package specification.

    ## Best practices

    > **Important**: Commit often in small hunks - **code dumps are almost impossible to review!**
    
    1. We try to follow appropriate style guides (e.g., [Python PEP8](https://peps.python.org/pep-0008/), [Markdown](https://google.github.io/styleguide/docguide/style.html), [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)).
    2. Install a linter for your IDE, I recommend [ruff](https://docs.astral.sh/ruff/installation/) with some good default settings (see example `pyproject.toml`).
    3. Structure your code as a Python project and install [pre-commit](https://pre-commit.com/) to ensure consistency. **Use [uv](https://docs.astral.sh/uv/) for package and environment managing.**
    4. Use [type-checking](https://docs.python.org/3/library/typing.html) in your Python code (by including `py.typed` file), make sure that you write docstrings (`interrogate`) and tests (`pytest`) as you go. Comment often to help others understand your intentions.
    5. Familiarise yourself with command line editors such as `vim` or `nano` for quick edits on the supercomputing cluster.
    6. Follow [git best practices](https://docs.github.com/en/get-started/using-git). **Commit often**, branch/fork actively! If your commit is getting too large, **use patch mode**: `git add --patch --interactive`.
    7. Use the [Python standard library](https://docs.python.org/3/library/index.html) whenever possible (e.g., `time`, `pathlib`) instead of external codes to reduce complexity and dependencies.

    """)
    return


if __name__ == "__main__":
    app.run()
