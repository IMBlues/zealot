#!make
output ?= "./example"

test:
	rm -rf ./example/*
	cookiecutter ./ -o ${output}