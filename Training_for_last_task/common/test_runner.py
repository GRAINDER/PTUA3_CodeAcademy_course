"""
Given the current source file path, run the tests in the corresponding unit test file.
Tamro Baltics, a Phoenix Company
Michael Hall
"""


DEFAULT_SOURCE_DIRECTORY = 'PycharmProjects'
DEFAULT_PROJECT_DIRECTORY = 'nbo'


def run_tests(
        # This should be __file__.
        source_file_path: str,
        # defaults to 'PycharmProjects'
        source_directory: str = DEFAULT_SOURCE_DIRECTORY,
        project_directory: str = DEFAULT_PROJECT_DIRECTORY   # defaults to 'nbo'

):
    """
    Run the unit tests in the corresponding test module.
    The test module is assumed to be named 'test_' + this_filename (without extension) and under a directory
    "tests" that has a mirror of the directory structure of the non-testing part of the project.



    For example, if the code is in:
    nbo/generator/kpis/conversion.py
    ...then the unit tests are assumed to be in:
    nbo/tests/generator/kpis/test_conversion.py
    The code is based on https://stackoverflow.com/a/31615611, with modifications by ChatGPT-4 with code plugin.
    """

    # We do local imports, since these packages will only be needed when doing testing.

    import os
    import importlib
    import unittest

    # Get this script's filename without extension
    this_filename = os.path.splitext(os.path.basename(source_file_path))[0]

    # Get absolute directory path
    abs_directory = os.path.dirname(os.path.realpath(source_file_path))

    # Identify the root directory of your project
    root_directory = os.path.join(source_directory, project_directory)

    # Find the index of root directory in absolute path
    root_index = abs_directory.index(root_directory)

    # Extract the package path
    package_path = abs_directory[root_index + len(root_directory) + 1:]

    # Replace slashes with dots to convert directory path to package name
    package_name = package_path.replace(os.sep, '.')

    # Construct the name of the corresponding test module
    test_module_name = 'tests.' + package_name + '.test_' + this_filename

    # Dynamically import the test module
    test_module = importlib.import_module(test_module_name)

    # Finally, the important part: run the tests in the test module
    suite = unittest.TestLoader().loadTestsFromModule(test_module)
    unittest.TextTestRunner(verbosity=2).run(suite)
