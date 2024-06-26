## Add your own custom Makefile targets here

.PHONY: careful-clean clean-examples clean-examples all-all

clean-examples: clean-tsv-yaml
	rm -rf examples/output

examples-all: clean-examples tsv-data-to-yaml examples/output

all-all: careful-clean gen-project gendoc test-python examples-all

careful-clean:
	rm -rf $(DEST) # project
	rm -rf tmp
	rm -fr docs/*
	# rm -fr $(PYMODEL)/* # src/"mifc"/datamodel/*
	rm -rf $(PYMODEL)/$(SCHEMA_NAME).* # todo do not make this target via point-and-click in an IDE! It will try to delete the whole project because PYMODEL and SCHEMA_NAME will be undefined
	rm -rf examples/output/*

.PHONY: tsv-data-to-yaml
tsv-data-to-yaml: $(patsubst src/data/examples/TSV/%.tsv,src/data/examples/valid/%.yaml,$(wildcard src/data/examples/TSV/*.tsv))

src/data/examples/valid/%.yaml: src/data/examples/TSV/%.tsv
	@echo Converting $< to $@
	$(eval INDEX_SLOT=$(shell echo $(notdir $<) | cut -d'-' -f2))
	linkml-convert \
		--schema src/mifc/schema/mifc.yaml \
		--output $@ \
		--target-class Container \
		--index-slot $(INDEX_SLOT) $<


.PHONY: clean-tsv-yaml
clean-tsv-yaml:
	@echo Removing corresponding YAML files...
	@$(foreach file,$(wildcard src/data/examples/TSV/*.tsv),\
		rm -f src/data/examples/valid/$(notdir $(basename $(file))).yaml;)
