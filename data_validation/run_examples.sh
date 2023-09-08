#!/bin/bash

set -u

# Validate example data

## Foods
linkml-validate -s ../src/mifc/schema/mifc.yaml -C Container -S foods test_data/Food-001.tsv

## Components
linkml-validate -s ../src/mifc/schema/mifc.yaml -C Container -S components test_data/Component-001.tsv
linkml-validate -s ../src/mifc/schema/mifc.yaml -C Container -S components test_data/Component-002.tsv