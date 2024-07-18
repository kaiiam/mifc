# MIFC

### About MIFC

The **M**inimum **I**nformation (about any) **F**ood **C**omposition (**MIFC**), data standard. MIFC provides a general-purpose schema for the description of Food Composition Tables and Databases (FCT/D). MIFC is intended to enumerate, standardize and validate (meta)/data relevant to FCT/D. MIFC is a Minimum Information Standard (MIS) for food composition data. MIS are sets of guidelines and data reporting formats that are used to standardize scientific data. 

### Contribution

MIFC is an open-source project. MIFC development is led by the United States Department of Agriculture (USDA) FoodData Central (FDC), as well as the open source MIFC Standard Consortium. Contributors welcome! Please help us improve the content of MIFC by making issues and or submitting pull requests.

### Note

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



## Usage and Pull Requests


* 1) Make sure you're up to date:

`git pull`

* 2) Start or address an issue

Gets an issue number e.g. issue https://github.com/kaiiam/mifc/issues/28

* 3) checkout a branch corresponding to that issue.

`git checkout -b issue-28`

* 4) Make relevant changes 

* 5) Add/commit changes

`git commit README.md -m 'Modify README file to include Usage and Pull Requests section'`

* 6) Push your branch to origin to create a pull request

For example the command would be something like git push origin issue-28. However you can just run `git push` and it should prompt you with the line to run E.g `git push --set-upstream origin issue-28`.

* 7) Create Pull Request

On the [Pull requests tab](https://github.com/kaiiam/mifc/pulls)

`Compare and Create Pull Request`

* 8) Switch from branch back to main:

`git checkout main`


# Working with the MIFC Repo

* 1) Activates a poetry shell from the `pyproject.toml` \
`poetry shell`

* 2) Keep poetry up to date \
`poetry update`

* 3) Update poetry.lock file \
`poetry install`

* 4) Run MIFC build and test suite \
`make all-all`



## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
