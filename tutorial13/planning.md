* **Schedule (preliminary)**:
  1. Introduction: Sebastian (10-12mins)
     * tutorial is split in two parts (1+2) and (3+4) (advanced people!) 
     * start with short plugin demo --> the hook for the tutorial
     * user roles in NOMAD
     * structured data
     * schema types: yaml, plugins, etc.
     * overview on tutorial
  2. NOMAD's BaseSections and Built-In ELNs (for **all users**)
     1. BaseSections: introduction to NOMAD's data model to ensure interoperability - Andrea (10 mins)
        Content:
            * introduce concepts of inheritance and composition
            * present backbone of BaseSections (entity-activity-model)
            * particular example where subclasses are shown, use same example as we show later in built-in ELN
            * hook for next part: introducing to the available set of classes (the ones we have built the built-in ELNs on)
        Take home messages:
            * overview pic on BaseSection
            * oop approach to structure data            

     2. Built-in ELNs: introduction to NOMAD's ELNs
        Livedemo, no slides, use only basic ELNs
        Story:
            * start with picking from basic ELNS.
            * generic sample ELN:
            * generic process
            * customized process


  3. Customization - Schema and Plugin development for expiremntal data in NOMAD: (for data stewards/scientists and interested users)
     goal: reach people that want to write a plugin for an Oasis!
     prerequisite: github account (or do locally)
     idea:
        * cookie cutter from Ahmed: 
            * create from github workspace, work in codespace to create everything automatically
        * add a class
        * write python schema from scrach
        * write plugin and do nomad parse test
     1. Custom yaml schema --> cut it and mention it as decribed in tutorial 8
     2. NOMAD schema plugin

  4. NOMAD Oasis - deploying your NOMAD plugins (for system admins and data stewards/scientists)
    goal: deploy a plugin on a local Oasis


- storyline
	- only base on BaseSections
	- annealing example, standard log file, small reader, a simple plot
	- populate sth in the results section
	- create a sample, link to XRD
	- NOMAD plugins as outlook --> goal of standardization
