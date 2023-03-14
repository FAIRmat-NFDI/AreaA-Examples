# Part 5: Reading Files with the Tabular Parser and Adding Plots

In this tutorial we show you how to decorate your schema to allow the parsing of csv and xlsx spreadsheet files into Nomad.

## Prerequisites
1. A NOMAD account.
    - You can easily make one on 
    [nomad-lab.eu](https://nomad-lab.eu/fairdi/keycloak/auth/realms/fairdi_nomad_prod/login-actions/registration?client_id=nomad_public&tab_id=X58B5qImrj8) 
    if you don't already have one.
2. A text editor.
    - Default editor works (i.e. Notepad).
    - Dedicated YAML editor like [Notepad++](https://notepad-plus-plus.org/) or an IDE 
    like [VScode](https://code.visualstudio.com/) is recommended.
3. The yaml files contained in this folder.

## Exercise
1. Try to instantiate a new entry choosing "MyOverallProcess" custom schema from the `mixed_tabular_parser.schema.archive` file. After uploading this file you can instantiate the entry and then drag and drop into the `data_file` quantity the `process_data.xlsx` file and save.
2. Add a new `quantity` in the `column_tabular_parser.schema.archive` file and parse the column "test_quantity" from `process_data.xlsx` file.
3. Add a new plot in the Section annotation so that the new quantity is visualized.

Point 2 and 3 solutions are shown in `SOLUTION_column_tabular_parser.schema.archive.yaml`

## Further Documentation

[Annotations documentation](https://nomad-lab.eu/prod/v1/staging/docs/schema/elns.html#eln-annotation)

[Plot documentation](https://nomad-lab.eu/prod/v1/staging/gui/dev/plot)

[Editable Quantities documentation](https://nomad-lab.eu/prod/v1/staging/gui/dev/editquantity)

