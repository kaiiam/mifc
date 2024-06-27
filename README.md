# MIFC

**About MIFC**

The Minimum Information (about any) Food Composition (MIFC), data standard. MIFC provides a general-purpose schema for the description of Food Composition Tables and Databases (FCT/D). MIFC is intended to enumerate, standardize and validate (meta)/data relevant to FCT/D. MIFC is a Minimum Information Standard (MIS) for food composition data. MIS are sets of guidelines and data reporting formats that are used to standardize scientific data. 

**Contribution**

MIFC is an open-source project. MIFC development is led by the United States Department of Agriculture USDA) FoodData Central (FDC), as well as the open source MIFC Standard Consortium. Contributors welcome! Please help us improve the content of MIFC by making issues and or submitting pull requests.

**Note**

This working version of MIFC is a prototype and not an officially adopted USDA resource.


## Website

[https://kaiiam.github.io/mifc](https://kaiiam.github.io/mifc)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [mifc](src/mifc)
    * [schema](src/mifc/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/mifc/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all-all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
