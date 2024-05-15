# **FAIRmat Tutorial 13:** 

## **NOMAD for Experimental Data Management in Synthesis**
  
* **Organized by**: [FAIRmat Area A](https://www.fairmat-nfdi.eu/fairmat/areas-fairmat/area-a-fairmat)

* **May 15, 2024, 1:00 PM until 4:00 PM**

* **Registration**: https://events.fairmat-nfdi.eu/event/18/

* **Contacts:** 
   - sebastian.brueckner@physik.hu-berlin.de
   - sarthak.kapoor@physik.hu-berlin.de
   - hampus.naesstroem@physik.hu-berlin.de
   - andrea.albino@physik.hu-berlin.de
   - fairmat-events@physik.hu-berlin.de
* **Discord:**
   - [NOMAD's Discord server](https://discord.gg/53QA5gxY)
   - [Tutorial 13 Discord Thread](https://discord.com/channels/1201445470485106719/1240225326194495498)


FAIRmat Tutorial 13, presented by FAIRmat Area A Synthesis, introduces NOMAD and NOMAD Oasis as essential tools for research data management (RDM). This tutorial will specifically demonstrate how to utilize these tools for managing experimental materials science data, with a particular focus on synthesis data.

Participants will learn about NOMAD's versatile data model, which ensures data interoperability, and its various types and levels of schemas, including custom yaml schemas, community standards, plugins, and base sections. The tutorial will also cover the integration of NOMAD with Electronic Lab Notebooks (ELNs) to enhance data documentation and management.

A practical session will guide users through a typical synthesis data example, demonstrating how to start from NOMAD's built-in schemas, develop a data schema, convert it into a NOMAD plugin for automated data processing, and deploy the schema on a local NOMAD Oasis. This hands-on approach will provide invaluable insights into customizing NOMAD to fit specific experimental workflows.

The session is designed to serve various user groups, including standard users, data stewards & data scientists, and system administrators, ensuring that each participant gains a comprehensive understanding of the tool's capabilities and applications in their respective roles. Join us to explore how NOMAD can transform your approach to data management in experimental synthesis, leading to more efficient and coherent research outputs - FAIR principles in practice.

**Schedule**:
  * **Part 1.** [Introduction:](https://github.com/FAIRmat-NFDI/AreaA-Examples/tree/main/tutorial13/part1) [**Link to slides**](https://github.com/FAIRmat-NFDI/AreaA-Examples/blob/main/tutorial13/Tutorial13_NOMAD_15-05-24.pdf)
     * user roles in NOMAD
     * overview on tutorial
  * **Part 2.** [NOMAD's Base Sections and Built-in Schemas](https://github.com/FAIRmat-NFDI/AreaA-Examples/tree/main/tutorial13/part2) (for all users) [**Link to slides**](https://github.com/FAIRmat-NFDI/AreaA-Examples/blob/main/tutorial13/Tutorial13_NOMAD_15-05-24.pdf)
     * Base Sections: introduction to NOMAD's data model to ensure interoperability
     * Built-in ELNs: introduction to NOMAD's ELNs
  * **Part 3.** [Customization - Schema and Plugin development for experimental data in NOMAD:](https://github.com/FAIRmat-NFDI/AreaA-Examples/tree/main/tutorial13/part3) (for data stewards/scientists and interested users)
     * Custom yaml schema
     * NOMAD schema plugin
  * **Part 4.** [NOMAD Oasis - deploying your NOMAD Plugins](https://github.com/FAIRmat-NFDI/AreaA-Examples/tree/main/tutorial13/part4) (for system admins and data stewards/scientists)

---

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

