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

     2. Built-in ELNs: introduction to NOMAD's ELNs (30mins)
        Livedemo, no slides, use only basic ELNs
        Story:
            * start with picking from basic ELNS.
            * generic sample ELN:
            * generic process
            (* customized process --> look up tutorial 8 how to do that!) just drop a yaml schema with customized process
            * play with XRD plugin
        goal:
            * how to use the existing classes

    wrap up part 2
    summary: explain limitations of yaml schema and contextualize the use of part 3 machinery --> link to our repos as examples to reuse and contribute

    --- Break ---  (10mins) --> 14:00 start next session

    explain limitations of yaml schema and contextualize the use of part 3 machinery --> link to our repos as examples to reuse and contribute
    reuse our existing plugins and deploy them accordingly as we explain in 4
    --> Andrea produces some slides



    explain kind of plugins
    refer to tutorial 12 and explain limitations of Jupyter notebook and why we do like we show here (this is the state of the art!)

  3. Customization - Schema and Plugin development for expiremntal data in NOMAD: (for data stewards/scientists and interested users) - 45 - 60min
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

  4. NOMAD Oasis - deploying your NOMAD plugins (for system admins and data stewards/scientists) 15mins for shwoing + 30mins open to hang around and do 4 themselves
    goal: deploy a plugin on a local Oasis


-- end of the tutorial 16:00h -- 

- storyline
	- only base on BaseSections
	- annealing example, standard log file, small reader, a simple plot
	- populate sth in the results section
	- create a sample, link to XRD
	- NOMAD plugins as outlook --> goal of standardization

## todos
* deploy plugins on central NOMAD Oasis Test + app?
* provide a visible to all upload
* course material:
    * slides
    * markdown docs including all the steps and actions we do in the practical part
