# Backend Engineering Challenge

Thank you for inviting me to completing this test challenge.
I have done main challenge and a little bonus one.
I didn't use external dependencies for main task as I was interested in implementing my own solution. Of course, for production purposes I'd rather use existing tool which better fits for the job.
As for bonus challenge I didn't want to reinvent the wheel and used convenient libs for the job.

## Assumptions

I've made several assumptions (some are based on previous questions and answers):
1. Input file is static ([1](https://github.com/Unbabel/backend-engineering-challenge/issues/5#issuecomment-491233710))
2. Input file is text file containing stringified JSONs ([2](https://github.com/Unbabel/backend-engineering-challenge/issues/11#issuecomment-496878358)) 
3. window size is integer because it is in minutes
4. I use Python 3.6+ to preserve elements order in dict with date (of course I can use OrderedDict if using Python earlier than 3.6, but I'd like to use modern version if possible)
5. I don't need to perform any checks on input lines or filter input data (e.g. event_name == translation_delivered and etc.)

## Run the app
1. Create virtualenv with your favorite tool, e.g. virtualenv, virtualenvwrapper, Pipenv, etc.
2. Install external dependencies for bonus (not required for main task)
3. Use Python 3.6+ (please refer to explanations in Assumptions #4.)
4. cd to directory with project
5. run the app

How to run the app:

	python main.py --input_file events.json --window_size 10
	
## Run tests
1. Assuming you have created virtualenv
2. cd to directory with project/tests
3. add project directory to PYTHONPATH (e.g. export PYTHONPATH=/path-to-project/tests)
4. run tests

How to run tests:

	python -m unittest

### Some explaining
Q: Why use custom input object and not 'with open(file) as file: ...'?

A: You can redefine any input object (e.g. data from database) and you don't need to change a lot of code. You just need 
input object to be an iterable.


#### Extra 
Good data needs some good visualisation, so you can produce PNG chart for sending it via email (sending is not included to bonus pack).
Bonus has some external dependencies including file 'output.json' in format as stated in challenge description

# Run bonus
1. Assuming you have created virtualenv
2. cd to directory with project
3. run bonus
4. You will be asked to provide number of lines from input file you'd like to see on chart. Choose wisely, too big number for big file might not ber readable. And remember not to join Dark Side even though they have cookies

How to run bonus:

	python bonus.py

