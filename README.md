## Summary
This repo contains an example usage of pytest.

It includes examples with:
- Setup and teardown methods
- Pytest mark to specify test tags
- Pytest parametrize on test inputs
- Pytest fixtures (local and global)
- Mocking with unittest

## Setup
Ensure python is installed

Project uses a couple of libs, so you need to run `pip3 install pytest requests`

## How to run tests
### Using pyCharm
- right-click the file name and select run tests
- click the run icon shown beside the method definition

### Running from the terminal

- Run all existing tests -> `pytest`
- Run specific test file -> `pytest tests/test_my_functions.py`
- Enable print statements and logging to be output even for passing tests -> `pytest tests/test_my_functions.py -s`
- Run tests with specific TAG -> `pytest -m "slow"`


## References

[FreeCodeCamp - Pytest Tutorial](https://www.youtube.com/watch?v=cHYq1MRoyI0)
[JSON PlaceHolder API](https://jsonplaceholder.typicode.com/)