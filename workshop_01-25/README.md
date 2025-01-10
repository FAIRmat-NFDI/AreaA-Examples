# **FAIRmat Workshop: parser development**
  
* **Organized by**: [FAIRmat Area A](https://www.fairmat-nfdi.eu/fairmat/areas-fairmat/area-a-fairmat)

* **Jan 15, 2024, 10:00 AM until Jan 16, 2024 5:00 PM**

* **Contacts:**
  * <sebastian.brueckner@physik.hu-berlin.de>
  * <sarthak.kapoor@physik.hu-berlin.de>
  * <hampus.naesstroem@physik.hu-berlin.de>
  * <andrea.albino@physik.hu-berlin.de>
  * <fairmat-events@physik.hu-berlin.de>

* **Discord:**
   [NOMAD's Discord server](https://discord.gg/53QA5gxY)

This workshop, presented by FAIRmat Area A Synthesis, introduces NOMAD and NOMAD Oasis essential features for research data management (RDM). 

Participants will learn about NOMAD's data model, and its various types and levels of schemas, including custom yaml schemas, community standards, and base sections. Later, the main strategies to develop a parser to instantiate and fill new entries with data from the lab will be covered. Each feature will be demonstrated in the framework of python packages created from a [template reposiroty](https://github.com/FAIRmat-NFDI/nomad-plugin-template), these packages are referred to as **plugins**.

The development of the code will be done within a [development environment](https://github.com/FAIRmat-NFDI/nomad-distro-dev).

The workshop is based on practical sessions that will guide users through some typical data example, demonstrating how to start from existing schemas, extend a data schema, work within the framework of a NOMAD plugin for automated data processing, and deploy the schema on a local NOMAD Oasis. This hands-on approach will provide invaluable insights into customizing NOMAD to fit specific experimental workflows.

* **Schedule**:

  * start summary of tutorial things
  * fork dev-distro
  * develop plugin:
    * main basic ideas
    * plugin infrastructure
    * schema:
    * data structure
    * visualizations
    * normalizations
    * inherit and modify
    * parser
    * search app
  * deployment
  * basic analysis
    * search data
    * query
    * get data in Jupyter

---

## Python files documentation

A brief explanation for each python file in this folder is provided below.

Each python file is not meant to be a standalone script to execute, rather to contain a snippet of code, complemented with the necessary import statements, ready to be included into your own plugin package code. Three categories have been created, namely __schema__ and __parser__ and __app__.

### Schema

#### m_def attribute

Get started with definition of your class.

#### Nest or reference

Data modeling strategies: composition in the same archive or in different archives.

#### Plotting

Few examples of commonly used `m_def` attributes accross existing plugins.

### Parser

#### Create non editable entries

Entries will end up as binary files in the `archive` folder. They cannot be modified! Do not use `EditQuantity` annotations in the schema.

#### Create editable entries

Entries will end up as plain text files in the `raw` folder. They can be modified.

#### Matching files

The snippet of code instructung a parser how to match a file will be included in the `__init__.py` file.

Some remarkable matching pattern:

* [Match a zip file](https://github.com/FAIRmat-NFDI/nomad-measurements/blob/main/src/nomad_measurements/xrd/__init__.py)
* [Stack multiple file names](https://github.com/FAIRmat-NFDI/nomad-measurements/blob/main/src/nomad_measurements/xrd/__init__.py)
* [Stack multiple file mimetypes](https://github.com/FAIRmat-NFDI/nomad-measurements/blob/main/src/nomad_measurements/xrd/__init__.py)
* [Stack multiple file mimetypes - 2](https://github.com/IKZ-Berlin/lakeshore-nomad-plugin/blob/main/src/lakeshore_nomad_plugin/hall/measurement_parser/__init__.py)
* [wide xlsx file matching](https://github.com/IKZ-Berlin/nomad-ikz-plugin/blob/main/src/nomad_ikz_plugin/movpe/movpe1/growth_excel/__init__.py)

#### Handling a reference

Create a reference to an entry and place it in another entry.

#### Create an HDF5 file

Handle HDF5 files creation.


### App

#### Example app

An app is a dashboard in the search panel that will allow to filter and show important data for you.


## Glossary

This glossary provides definitions for key terms used for software development in this project. Understanding these terms will help you navigate and use the project more effectively.

### NOMAD and NOMAD Oasis
**NOMAD (Novel Materials Discovery)**: A repository and data management platform for materials science data.  
**NOMAD Oasis**: A customizable version of the NOMAD repository that can be deployed and managed independently by organizations or research groups.

### Research Data Management (RDM)
Refers to the organization, storage, preservation, and sharing of data collected and used during a research project. Effective RDM ensures that data is accurate, accessible, and reusable.

### Data Schema
A structured framework or blueprint that defines the organization, structure, and constraints of data. It is commonly used in databases and data modeling to describe the format and relationships of data elements.

### Data Model
An abstract representation of the data structures and relationships used within a database or information system. It is formalized within schemas and it serves as a blueprint for designing and implementing a database.

### Template
An empty file whose structure is determined by a schema. Multiple templates are created from same schemas and filled with data, giving rise to an homogeneous data repository.


### Electronic Lab Notebook (ELN)
A digital platform for documenting research processes, experiments, and results. ELNs enhance data organization, sharing, and collaboration in scientific research.

### FAIR Data
Principles that stand for Findable, Accessible, Interoperable, and Reusable. These principles guide the management and sharing of data to ensure that it can be easily discovered, accessed, integrated, and reused by others.

### Repository
A centralized location where data, code, or other digital assets are stored and managed. In the context of GitHub and Git, a repository is a project space where all files, including their history and versions, are kept.

### Classes
In Python, a class is a blueprint for creating objects. Classes define the properties and behaviors of the objects created from them.

### Python
A high-level, interpreted programming language known for its simplicity and readability. It is widely used for web development, data analysis, scientific computing, artificial intelligence, and more.

### Pip
A package manager for Python that allows users to install and manage additional libraries and dependencies that are not included in the standard library. [What is Pip?](https://realpython.com/lessons/what-is-pip-overview/)

### Python Virtual Environment
An isolated environment for Python projects that allows dependencies to be installed and managed separately from the global Python installation. This helps avoid conflicts between project-specific dependencies. [What is a Python virtual environment?](https://realpython.com/python-virtual-environments-a-primer/#why-do-you-need-virtual-environments)

### Python Package
A collection of Python modules that are grouped together. Packages are used to organize and structure Python code, making it easier to manage and reuse. [What is a Python package?](https://packaging.python.org/en/latest/tutorials/packaging-projects/) 

### PyPI
PyPI (Python Package Index) is a repository of software packages developed and shared by the Python community. [Uploading a package to PyPI.](https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/)

### Integrated Development Environment (IDE)
An Integrated Development Environment (IDE) is a software application that provides comprehensive facilities to programmers for software development. [What is VSCode?](https://aws.amazon.com/what-is/ide/)

### Git
A distributed version control system that tracks changes in source code during software development. It allows multiple developers to work on a project simultaneously, managing code changes and versions efficiently. [What is Git?](https://learn.microsoft.com/en-us/devops/develop/git/what-is-git)

### GitHub
A web-based platform used for version control and collaborative software development. It uses Git for managing changes to the source code and provides additional features for project management and collaboration.

### GitHub Codespace
A cloud-based development environment provided by GitHub. It allows developers to code, build, and debug directly in the cloud without needing to set up a local development environment.

### Command Line Interface (CLI)
A text-based interface used to interact with software and operating systems. Users input commands as text and receive text-based output.

### Cruft
Built on top of CookieCutter, a utility for creating projects from templates, this tool ensures a clean and standardized project setup. It also includes an update mechanism, allowing you to seamlessly update your project when the template changes. [What is cruft?](https://cruft.github.io/cruft/)

### YAML (Yet Another Markup Language)
A human-readable data serialization format commonly used for configuration files and data exchange between languages with different data structures. It is known for its simplicity and ease of use.

### JSON (JavaScript Object Notation)
A lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is commonly used for transmitting data in web applications.

### Docker
A platform that uses containerization to deploy and manage applications. Containers package an application and its dependencies, ensuring consistency across multiple environments.

### Keycloak
An open-source identity and access management solution. It provides authentication, authorization, and user management for applications and services.

### Reference
A reference is a link to one file in NOMAD, usually contained within another file in NOMAD. It is an important tool to describe highly linked data from materials science.

