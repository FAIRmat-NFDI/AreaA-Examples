# Part 4: Writing a Custom Schema

In this tutorial we will show you how to create your very own data schema which generates
a custom Electronic Lab Notebook (ELN).

## Prerequisites
1. A NOMAD account.
    - You can easily make one on 
    [nomad-lab.eu](https://nomad-lab.eu/fairdi/keycloak/auth/realms/fairdi_nomad_prod/login-actions/registration?client_id=nomad_public&tab_id=X58B5qImrj8) 
    if you don't already have one.
2. A text editor.
    - Default editor works (i.e. Notepad).
    - Dedicated YAML editor like [Notepad++](https://notepad-plus-plus.org/) or an IDE 
    like [VScode](https://code.visualstudio.com/) is recommended.

## Exercise

1. Extend the YAML file (`my_schema.schema.archive.yaml`) we wrote during the tutorial 
with a string quantity `name`.
2. Login on the nomad beta server
([nomad-lab.eu/prod/v1/staging](https://nomad-lab.eu/prod/v1/staging/gui/about/information)) 
and open your upload from part 3 under the "Publish/uploads" menu.
3. Upload the modified YAML file and make sure it is processed successfully.
4. Create an instance of `MySubstrate` using the "Create Entry" button and check that the 
new `name` quantity is there.
5. *In case of time: Add more quantities using the edit quantities found on 
[nomad-lab.eu/prod/v1/staging/gui/dev/editquantity](https://nomad-lab.eu/prod/v1/staging/gui/dev/editquantity)*
