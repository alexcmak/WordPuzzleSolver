# Windows: python -m pytest

# mac
#
# python3 -m venv alex_env
# source ./alex_env/bin/activate
# python3 -m pip install pytest
# pytest

# pytest is by convention. This test file must be in the form test_Something.py

import PuzzleSolver

def test_RunPuzzle():

	PuzzleSolver.ReadPuzzle()

	assert PuzzleSolver.CheckWest(8,5, "BANANA") == True
	assert PuzzleSolver.CheckWest(8,5, "APPLE") == False
	assert PuzzleSolver.CheckSouthWest(2,4, "APPLE") == True
