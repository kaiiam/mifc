# mifc

A minimum information standard checklist formalizing the description of food composition data and related metadata.

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

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
