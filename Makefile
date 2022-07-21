#!make

generate:
	rm -rf ./example/*
	cookiecutter ./ -o ./example/ --no-input

test:
	rm -rf .tests/*
	cookiecutter ./ -o .tests/
	cd .tests/zealot_example/ && make run-api
