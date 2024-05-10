> [!WARNING]
> This is work in progress and some of the commands below might not work before the day
> of the tutorial (15th of May, 2024).

# Part 3: Developing a NOMAD Plugin
In this part of the tutorial you will learn how to create and develop a NOMAD plugin.

## Prerequisites
- A GitHub account, can be created for free on [github.com](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)
- Basic understanding of Python
- Basic understanding of NOMAD metainfo, see for example [tutorial 8](https://www.fairmat-nfdi.eu/events/fairmat-tutorial-8/tutorial-8-materials)

## 1. Create a Git(Hub) repository
Firstly, we recommend to use git to version control your NOMAD plugin.
There is a GitHub template repository that can be used for this at [github.com/FAIRmat-NFDI/nomad-plugin-template](https://github.com/FAIRmat-NFDI/nomad-plugin-template).

To use the template you should choose the "Create an new repository" option after pressing
the green "Use this template" button in the upper right corner.
Please note that you have to be logged into to GitHub to see this option.

![Use template](./images/use_template_dark.png#gh-dark-mode-only)
![Use template](./images/use_template_light.png#gh-light-mode-only)

Enter a name for your repository and click "Create Repository"

## 2. Generate the plugin structure
Next, we will use a cookiecutter template to create the basic structure of our NOMAD
plugin.

There are now two options for how to proceed.
1. You can use the GitHub codespaces environment to develop your plugin, or
2. If you have access to a Linux computer you can also run the same steps locally.

### 2.1a Using GitHub codespaces
To use a GitHub codespace for the plugin development you should choose the "Create
codespace on main" option after pressing the green "<> Code" button in the upper right
corner.

![Use codepace](./images/codespace_dark.png#gh-dark-mode-only)
![Use codespace](./images/codespace_light.png#gh-light-mode-only)

### 2.1b Developing locally
If you have a Linux machine and prefer to develop locally you should instead click the 
"Local" tab after pressing the green "<> Code" button, copy the path, and clone your
repository by running:

```sh
git clone PATH/COPIED/FROM/REPOSITORY
```
and move inside the top directory
```
cd REPOSITORY_NAME
```
You will also need to install [cruft](https://pypi.org/project/cruft/), preferably using
`pipx`:
```sh
# pipx is strongly recommended.
pipx install cruft

# If pipx is not an option,
# you can install cruft in your Python user directory.
python -m pip install --user cruft
```

### 2.2 Run cruft
The next step is to run cruft to use our cookiecutter template:
```sh
cruft create https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin
```
Cookiecutter prompts you for information regarding your plugin:

```no-highlight
full_name [John Doe]: Citizen Kane
email [john.doe@physik.hu-berlin.de]: citizen@kane.de
github_username [foo]: kane
plugin_name [foobar]: awesome-tools
module_name [awesome_tools]: awesome_tools
short_description [NOMAD example template]: An awesome plugin for NOMAD
version [0.1.0]:
Select license:
1 - MIT
2 - BSD-3
3 - GNU GPL v3.0+
Choose from 1, 2, 3 [1]: 2
include_schema_package [y/n] (y): y
include_normalizer [y/n] (y): n
include_parser [y/n] (y): n
include_app [y/n] (y): n

INFO:post_gen_project:Initializing python for package - src
..
INFO:post_gen_project:Remove temporary folder: licenses
INFO:post_gen_project:Remove temporary folder: macros
INFO:post_gen_project:Remove temporary folder: py_sources
```

There you go - you just created a minimal NOMAD plugin:

> [!NOTE]
> In the above prompt, we pressed `y` for schema_package, this creates a python package with a plugin entry point for a schema package.

```no-highlight
nomad-awesome-tools/
├── LICENSE
├── README.rst
├── pyproject.toml
├── move_template_files.sh
├── src
│   └── nomad_awesome_tools
│       ├── __init__.py
|       └── schema_packages
│           ├── __init__.py
│           └── plugin.py
├── tests
│   ├── conftest.py
│   └── test_awesome.py
└── MANIFEST.in
```

> [!NOTE]
> The project `nomad-awesome-tools` is created in a new directory, we have included a helper script to move all the files to the parent level of the repository.


```sh
sh CHANGE_TO_PLUGIN_NAME/move_template_files.sh
```

> [!IMPORTANT]
> The `CHANGE_TO_PLUGIN_NAME` should be substituted by the name of the plugin you've created. In the above case it'll be `sh nomad-awesome-tools/move_template_files.sh`. 

Finally, we should add the files we created to git and commit the changes we have made:
```sh
git add -A
git commit -m "Generated plugin from cookiecutter template"
git push
```

## 3. Importing a yaml schema

### 3.1 The schema
We will now convert the yaml schema package from part 2 where we described a sintering
step:

```yml
definitions:
  name: 'Tutorial 13 sintering schema'
  sections:
    TemperatureRamp:
      m_annotations:
        eln: 
          properties:
            order: 
              - "name"
              - "start_time"
              - "initial_temperature"
              - "final_temperature"
              - "duration"
              - "comment"
      base_sections:
        - nomad.datamodel.metainfo.basesections.ProcessStep
      quantities:
        initial_temperature:
          type: np.float64
          unit: celsius
          description: "initial temperature set for ramp"
          m_annotations:
            eln:
              component: NumberEditQuantity
              defaultDisplayUnit: celsius
        final_temperature:
          type: np.float64
          unit: celsius
          description: "final temperature set for ramp"
          m_annotations:
            eln:
              component: NumberEditQuantity
              defaultDisplayUnit: celsius
    Sintering:
      base_sections:
        - nomad.datamodel.metainfo.basesections.Process
        - nomad.datamodel.data.EntryData
      sub_sections:
        steps:
          repeats: True
          section: '#/TemperatureRamp'
```

We can grab this file from the tutorial repository using curl
```sh
curl -L -o sintering.archive.yaml "https://raw.githubusercontent.com/FAIRmat-NFDI/AreaA-Examples/main/tutorial13/part3/files/sintering.archive.yaml"
```


### 3.2 `metainfo-yaml2py`

We will now use an external package `metainfo-yaml2py` to convert the yaml schema package
into python class definitions.
First we install the package with `pip`:
```sh
pip install metainfo-yaml2py
```

Then we can run the `metainfo-yaml2py` command on the `sintering.archive.yaml` file
and specify the output directory, with the `-o` flag, to be our `schema_packages`
directory:
```sh
metainfo-yaml2py sintering.archive.yaml -o src/nomad_awesome_tool/schema_packages
```

### 3.3 Updating __init__.py

## 4. Adding a normalizer

### 4.1 The use case

### 4.2 Adding the code

## 5. Testing

### 5.1 Create an archive.json file

### 5.2 Run the NOMAD CLI

### 5.3 Add a test

### 5.4 Run pytest

## 6. Adding a plot (in case of time)

### 6.1 Add the code

### 6.2 Visualize the plot

## 7. Exporting a yaml schema

### 7.1 Convert to yaml schema

### 7.2 Upload yaml schema to NOMAD

### 7.3 Next step (part 4)