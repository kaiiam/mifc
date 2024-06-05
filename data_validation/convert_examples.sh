#!/bin/bash

set -u

# Convert example data

## Foods
linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S foods test_data/Food-001.tsv -o results/yaml/Food-001.yaml
linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S foods test_data/Food-001.tsv -o results/json/Food-001.json
linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S foods test_data/Food-001.tsv -o results/ttl/Food-001.ttl

linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S foods test_data/Food-002.tsv -o results/yaml/Food-002.yaml
linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S foods test_data/Food-002.tsv -o results/json/Food-002.json


## Components
linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S components test_data/Component-001.tsv -o results/yaml/Component-001.yaml
linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S components test_data/Component-001.tsv -o results/json/Component-001.json
linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S components test_data/Component-001.tsv -o results/ttl/Component-001.ttl

linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S components test_data/Component-002.tsv -o results/yaml/Component-002.yaml
linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S components test_data/Component-002.tsv -o results/json/Component-002.json

linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S components test_data/Component-003.tsv -o results/yaml/Component-003.yaml
linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S components test_data/Component-003.tsv -o results/json/Component-003.json


##Provenance
linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S provenances test_data/Provenance-001.tsv -o results/yaml/Provenance-001.yaml
linkml-convert -s ../src/mifc/schema/mifc.yaml -C Container -S provenances test_data/Provenance-001.tsv -o results/json/Provenance-001.json

