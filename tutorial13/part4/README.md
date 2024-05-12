> [!WARNING]
> This is work in progress and some of the commands below might not work before the day
> of the tutorial (15th of May, 2024).

# Part 4: Deploying a NOMAD Oasis with Plugins

## Prerequisites
- A GitHub account, can be created for free on [github.com](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)
- Docker installed on your computer, installation instructions can be found on
[docs.docker.com/desktop/](https://docs.docker.com/desktop/)

## 1. Create a Git(Hub) repository
There is a GitHub template repository that can be used for this at [github.com/FAIRmat-NFDI/nomad-distribution-template](https://github.com/FAIRmat-NFDI/nomad-distribution-template).

To use the template you should choose the "Create an new repository" option after pressing
the green "Use this template" button in the upper right corner.
Please note that you have to be logged into to GitHub to see this option.

## 2. Add the plugin
TBA

## 3. Run the OASIS
1. Make sure you have [docker](https://docs.docker.com/engine/install/) installed.
Docker nowadays comes with `docker compose` built in. Prior, you needed to
install the stand-alone [docker-compose](https://docs.docker.com/compose/install/).
2. Get the `nomad-oasis.zip` archive from your distribution repository using for example curl
```sh
curl -L -o nomad-oasis.zip "https://github.com/GITHUB_REPOSITORY/raw/main/nomad-oasis.zip"
```
3. Unzip the `nomad-oasis.zip` file and enter the extracted directory
```sh
unzip nomad-oasis.zip
cd nomad-oasis
```
4. _On Linux only,_ recursively change the owner of the `.volumes` directory to the nomad user (1000) 
```sh
sudo chown -R 1000 .volumes
```
5. Pull the images specified in the `docker-compose.yaml` (retrieved from the `nomad-oasis.zip`).
Note that the image needs to be public or you need to provide a PAT (see "Important" note above).
```sh
docker compose pull
```
6. And run it with docker compose in detached (--detach or -d) mode 
```sh
docker compose up -d
```
7. Optionally you can now test that NOMAD is running with
```
curl localhost/nomad-oasis/alive
```
8. Finally, open [http://localhost/nomad-oasis](http://localhost/nomad-oasis) in your browser to start using your new NOMAD Oasis.
