# Backend Engineering Challenge

Thank you for inviting me to completing this test challenge.

## Assumptions

I've made several assumptions based on previous questions and answers:
1. Input file is static ([1](https://github.com/Unbabel/backend-engineering-challenge/issues/5#issuecomment-491233710))
2. Input file is text file containing stringified JSONs ([2](https://github.com/Unbabel/backend-engineering-challenge/issues/11#issuecomment-496878358)) 
3. window size is integer because it is in minutes 

## Run the app
1. create virtualenv with your favorite tool, e.g. virtualenv, virtualenvwrapper, Pipenv, etc.
2. install all dependencies from requirements.txt (or Pipfile if using Pipenv)
3. run the app

How to run the app:

	python main.py --input_file events.json --window_size 10
	
### Some explaining
1. - Why use custom input object and not 'with open(file) as file: ...'?
- You can redefine any input object (e.g. data from database) and you don't need to change a lot of code. You just need 
input object to be an iterator.
2. - 

#### Extra 
