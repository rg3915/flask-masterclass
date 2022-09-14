autopep8:
	find app -name "*.py" | xargs autopep8 --in-place

isort:
	isort -m 3 *

lint: autopep8 isort
