coverage run --source=. -m unittest tests/tests.py
coverage report -m
coverage html
firefox htmlcov/index.html