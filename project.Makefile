## Add your own custom Makefile targets here

.PHONY: careful-clean clean-examples clean-examples all-all

clean-examples:
	rm -rf examples/output

examples-all: clean-examples examples/output

all-all: careful-clean clean-examples all test examples-all

careful-clean:
	rm -rf $(DEST) # project
	rm -rf tmp
	rm -fr docs/*
	# rm -fr $(PYMODEL)/* # src/"mifc"/datamodel/*
	rm -rf $(PYMODEL)/$(SCHEMA_NAME).*
