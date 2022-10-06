indenter:
	find app -name "*.html" | xargs djhtml -t 2 -i

autopep8:
	find app -name "*.py" | xargs autopep8 --in-place

isort:
	isort -m 3 *

lint: autopep8 isort indenter
