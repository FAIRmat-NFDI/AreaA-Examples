# Part 6: Using Base Classes and References

In this tutorial we will show you how to use inheritance and composition to extend the functionality of your custom schemas. We will also show how you can reference other entries.

## Prerequisites
1. A NOMAD account.
    - You can easily make one on 
    [nomad-lab.eu](https://nomad-lab.eu/fairdi/keycloak/auth/realms/fairdi_nomad_prod/login-actions/registration?client_id=nomad_public&tab_id=X58B5qImrj8) 
    if you don't already have one.
2. A text editor.
    - Default editor works (i.e. Notepad).
    - Dedicated YAML editor like [Notepad++](https://notepad-plus-plus.org/) or an IDE 
    like [VScode](https://code.visualstudio.com/) is recommended.
3. The `my_schema.schema.archive.yaml` file from part 4.

## Exercise
1. Update the `my_schema.schema.archive.yaml` file from part 4 with a `MySubstance` 
section definition.
2. Add inheritance to `nomad.datamodel.data.EntryData` and 
`nomad.datamodel.metainfo.eln.Substance` using the `base_sections` property.
3. Reupload the schema and create an instance of your favorite substance.
4. Change the `type` of the `material` property in the `MySubstrate` class to 
`MySubstance` and the ELN component to `ReferenceEditQuantity`.
5. Make `MySubstrate` additionally inherit from 
`nomad.datamodel.metainfo.eln.ElnBaseSection`.
6. Reupload the schema and reprocess your existing substrate entry or make a new one.
7. Add the substance you created as a reference for the substrate material.
8. *In case of time: Add a SampleID subsection, reupload, reprocess and generate a 
SampleID.*