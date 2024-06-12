## Add your own custom Makefile targets here

.PHONY: clean-examples clean-examples

clean-examples:
	rm -rf examples/output

examples-all: clean-examples examples/output