## Summary
This repo contains an example usage of pytest.

## Setup
You will need python installed
Project uses pytest, so you need to run `pip install pytest`

TODO: replace this with a requirements file to facilitate installing dependencies


## How to run tests
### Using pyCharm
- right-click the file name and select run tests
- click the run icon shown beside the method definition

### Running from the terminal

- Run all existing tests -> `pytest`
- Run specific test file -> `pytest tests/test_my_functions.py`
- Enable print statements and logging to be output even for passing tests -> `pytest tests/test_my_functions.py -s`
- Run tests with specifc TAG -> `pytest -m "slow"`


## References

[FreeCodeCamp - Pytest Tutorial](https://www.youtube.com/watch?v=cHYq1MRoyI0)