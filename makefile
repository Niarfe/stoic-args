.PHONY: default
default: clean
	@cat makefile

.PHONY: list                 # This command.  List available commands with this makefile
list:
	@cat makefile | grep -E "^\.PHONY" | sed 's/^.\{8\}//'

env:                         # create virtual env and load requirements
	python3 -m venv env
	. env/bin/activate; pip install --upgrade pip; pip install -r requirements.txt

.PHONY: clean                # remove pesky .DS_Store files!
clean:
	@find . -name ".DS_Store" | xargs rm
	@find . -name "__pycache__" | xargs rm -rf

.PHONY: test                 # run the local tests
test: 
	pytest -vvx tests
