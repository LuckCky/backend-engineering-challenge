# Backend Engineering Challenge

Thank you for inviting me to completing this test challenge.

## Assumptions

I've made several assumptions based on previous questions and answers:
1. Input file is static ([1](https://github.com/Unbabel/backend-engineering-challenge/issues/5#issuecomment-491233710))
2. Input file is text file containing stringified JSONs ([2](https://github.com/Unbabel/backend-engineering-challenge/issues/11#issuecomment-496878358)) 
3. window size is integer because it is in minutes
4. Python 3.6+ to preserve elements order in dict with date (of course I can use OrderedDict if using Python earlier than 3.6, but I'd like to use modern version if possible) 

## Run the app
1. create virtualenv with your favorite tool, e.g. virtualenv, virtualenvwrapper, Pipenv, etc.
2. install all dependencies from requirements.txt (or Pipfile if using Pipenv)
3. cd to directory with project
4. run the app

How to run the app:

	python main.py --input_file events.json --window_size 10
	
## Run tests
1. create virtualenv
2. cd to directory with tests
3. add project directory to PYTHONPATH
4. run tests

How to run the app:

	python -m unittest

### Some explaining
1. - Why use custom input object and not 'with open(file) as file: ...'?
- You can redefine any input object (e.g. data from database) and you don't need to change a lot of code. You just need 
input object to be an iterator.
2. - 

#### Extra 
