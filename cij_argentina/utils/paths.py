from pyprojroot import here
from pathlib import Path
from typing import (
    Union,
    Callable,
    Iterable,
)

def make_dir_function(
    dir_name: Union[str, Iterable[str]]
) -> Callable[..., Path]:
    """
    Generate a function that converts a string or iterable of strings into
    a path relative to the project directory.

    @param dirname: Name of the subdirectories to extend the path of the main
    project.

    @returns A function that returns the path relative to a directory that can
    receive 'n' number of arguments for expansion.
    """

    def dir_path(*args) -> Path:
        if isinstance(dir_name, str):
            return here().joinpath(dir_name, *args)
        else:
            return here().joinpath(*dir_name, *args)

    return dir_path

project_dir = make_dir_function("")

for dir_type in [
        ["data"],
        ["data", "raw"],
        ["data", "processed"],
        ["outputs"],
        ["outputs", "figures"],
        ["outputs", "tables"],
        ["assets"]
    ]:
    dir_var = '_'.join(dir_type) + "_dir"
    exec(f"{dir_var} = make_dir_function({dir_type})")