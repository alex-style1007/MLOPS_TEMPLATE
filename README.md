# Cookiecutter Project MLOPS Usage TDSP methodology

## 1. Introduction

This document describes how to use cookiecutter to create a new project with the following structure:

- **author**: Project author.
- **Project_name**: Project name.
- **project_version**: Project version.
- **Business_Understanding**: Business understanding and stage 1.
- **Data_Manipulation**: Data manipulation and analysis, stage 2.
- **Data_conection**: Database connection.
- **Model1**: Analytical model 1.
- **deployment**: Deployment, stage 4.
- **date**: Date in DD_MM_YYYY format.
- **Client**: Client approval, stage 5.
- **Architecture**: Architecture as code (Terraform/Docker, etc.).

## 2. Installing Cookiecutter

To use cookiecutter, you first need to install it. You can do this using `pip`, the Python package manager.

```bash
pip install cookiecutter
```
## 3. Cookiecutter Configuration
1. Project Structure
Cookiecutter creates a project structure based on the following settings:

- author: Specifies the author of the project.
- project_name: Name of the project.
- project_version: Version of the project.
- business_understanding: Describes the business understanding and the first stage of the project.
- data_manipulation: Describes the data manipulation and analysis, corresponding to the second stage of the project.
- data_connection: Configures the connection to the database.
- model1: Defines the first analytical model.
- deployment: Configures the deployment of the project in the fourth stage.
- date: Date of project creation.
- client: Documents the client approval in the fifth stage.
- architecture: Defines the architecture of the project using tools such as Terraform or Docker.

2. Using Cookiecutter
To create a new project using cookiecutter, run the following command on the command line:

```bash
cookiecutter https://github.com/alex-style1007/MLOPS_TEMPLATE
```

# Use virtual environment

First you need to activate a virtual environment with the following commands:

```bash
python3 -m venv .venv
```

Then you need to activate the created environment, make sure you are standing in the project created with the cookiecutter template

```bash
source .venv/bin/activate
```

- Install Dependencies from requirements.txt:

Once the virtual environment is activated, install the dependencies specified in requirements.txt with:

```bash
pip install -r requirements.txt
```

# Use Sphinx

Sphinx is a documentation generating software that converts reStructuredText files into HTML web pages and other formats, including PDF, EPub and man. It takes advantage of the extensible nature of reStructuredText and its extensions (e.g. to automatically generate documentation from source code, write mathematical notation or highlight code).

## Setting up Sphinx:

Navigate to your project's root directory and run the following command to start setting up Sphinx:

## Generating Documentation:

Once you have configured and added content to your .rst files, you can generate the documentation with:

```bash
make html
```
Genereted html documents in the build/html files

```bash
make latexpdf
```
Genereted pdf documents in the build/latex


After running sphinx, Sphinx will create a basic directory and file structure. The basic structure of the documentation project may look like this:

```bash
{{cookiecutter.Project_name}}/
├── build/
├── source/
│   ├── _static/
│   ├── _templates/
│   ├── conf.py
│   ├── index.rst
└── Makefile

```


if latexpdf does not work, run these commands in ubuntu:

```bash
sudo update
sudo apt install latexmk texlive texlive-latex-extra texlive-lang-all
```
