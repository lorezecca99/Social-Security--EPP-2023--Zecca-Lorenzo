# Macroeconomic consequences of eliminating social security in the US


[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/lorezecca99/proj_ss/main.svg)](https://results.pre-commit.ci/latest/github/lorezecca99/proj_ss/main)
[![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Usage

To get started, create and activate the environment with

```console
$ conda/mamba env create
$ conda activate proj_ss
```

To build the project, type

```console
$ pytask --ignore task_plot.py --ignore task_paper.py
$ pytask
```

## Credits

This project was created with [cookiecutter](https://github.com/audreyr/cookiecutter)
and the
[econ-project-templates](https://github.com/OpenSourceEconomics/econ-project-templates).

## Project's description

This project replicates the study of Conesa and Krueger (1999): we consider a discrete time overlapping generations model, 
where the economy is populated by a continuum with given mass 
growing at a constant rate "n" of ex-ante identical individuals.
We compare two steady states: 
one in which the government runs a social security system, financed 
through taxes on labor; and another one, where the there is no public 
pension system, and eranings from labor are not taxed. However, we will cover only 
the comparion between the two steady states, neglecting the transition dynamics analysis.

The organization of the project is the follow.
In the folder "data_management", we have two functions: "import_data.py", to import the dataset from Dropbox (importing directly the dataset in the folder would not be possible given its dimension and the limitation of Github's basic version), and "clean_data.py" to prepare the dataset for the estimation/prediction phase. Then the two "task" files use the dependencies indicated and produce the initial and cleaned dataset (saved in "bld/python/data").\
Then, the analisys forlder containts the functions, and respective tasks, to predict the age-efficiency profile of workers between 20 and 64 years of age, plot such a profile (saved in "bld/python/age_efficiency"), and run the code to compute and save the results (saved in "bld/python/results") for the two steady states. Finally, the file "task_plot.py" plots the profile for savings, labor supply, earnings, and consumption by age in both economies, with and without social security.\
In addition, the folder "paper" containts the latex file to import the table and the figures, and to produce the final pdf.

Once having cloned the repository and set the environment ("proj_ss"), you may need to first run everything but negleting the files "task_plot.py" and "task_paper.py". The first does not run without first saving the results, so to avoid error in dependencies we can just ignore it. Also, ignoring the task for the paper may be necessary since it requires to compile the pdf in which the outputs of "task_plot.py" are used as inputs. Only then, you will be able to run pytask without any issue.
