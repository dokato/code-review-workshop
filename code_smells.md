## Bad Smells

List of Bad Coding smells in Code Snippets

### Module `graph_neighbourhood.py`

**Pros**

- Good code formatting and organisation
- General good naming for variables and functions
- Well use of `__main__` block to organise the statements to be executed when running the module directly.
- Good use of `ArgumentParser` to clearly define the CLI (`Command Line Interface`)

**Cons**
- Module is not self-consistent (iow _lack of encapsulation_ in the `main` block)
    * Core function and processing should be abstracted into an importable function!
- Unused imports
- Lack of docstrings, and documentation
    * There are triple-quotes in the top of the module, but empty. Also having this a `main` block usually implies that some documentation should be added/needed.
    * Documentation of CLI is poor and sometimes missing
    * Complete lack of docstring in `neighbourhood` function
    * Only partial use of `type-hints` in function signature
    * Function signature doc is wrong (i.e. `return type`)
- `neighbourhood` function implementation is very cryptic
    * Code doesn't adhere to the `explicit is better than implicit` rule from the _Zen of Python_
    * 8 possible directions of indices (e.g. `n, s, ne, sw, ..`) should be easily generated by calling `itertools.product`
    * `filter` with `starmap` is simply undeadable to be comprehensible. Explicit `for` and `if` constructs should be used, instead!

**AOB**

- `logfile` is opened, and never closed!
- `nn` variable name is misleading, and not communicative enough. Also see last `for` loop
- call to `neighbourhood` in the inner `for-loop` should be cached and improved 
    * maybe use `functools.partial` to fix call with `borders` parameter



### Module `plotting.py`

**Pros**

- Good code formatting, and organisation
- Clear module docstring
- Generally good variable names (but still requires improvements)

**Cons**

- Globals require revision and improvements:
    * `CHART_FOLDER` points to a local path to the machine
    * `default_color_map` (which is supposed to be a CONSTANT) doens't adhere with PEP8 - iow. should be all uppercase.
- `bar_plot` function is a mess :D
    * long list of parameters (lack of encapsualtion)
    * duplicated code (e.g. see lines `157-182`)
    * function with no-effect (more later)
    * lack of cohesion (mix of data processing and data visualisation)
    * long list of parameters
    * outdated docstring
    * name of parameters should be improved (e.g. `width` refers to bar width, but after `figsize` might be confused with `figure width`.)
    * default values for some parameters are mostly `None` but should instead comply with their corresponding `type-hints`.
    * very long implementation - should be better structured
    * also, plotting function should always return the `Axis` object (e.g. see `pd.DataFrame.plot`) rather than just _plotting_. In this case, also the last `if-branch` with `filename` should be removed.


### Module `track_reconstruction.py`

**Pros**

- code formatting, and import organisation

**Cons** (function `fit_data`)

- lack of any documention of docstring
    * function parameters should benefit from use of `type-hint` for parameters, as well as for the return type
- (in fact) type-hinting would have clarified the complete lack of encapsulation in the return values (as well as parameters)
- lack of encapsulation in parameters is also reflected on the many cases of duplicated code;
- there is lack of comments (and inline ones are quite poor)
    * no clear explanation nor rationale on conditions (e.g. what do conditions on `L59,69` mean?)
- some `print` and `debug` code should be removed
- no clear definition of what the function is doing (following from _lack of documentation_)
- variable names should be improved