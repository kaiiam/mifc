## Add your own custom Makefile targets here

.PHONY: clean-examples clean-examples all-all

clean-examples:
	rm -rf examples/output

examples-all: clean-examples examples/output

all-all: clean all test examples-all
