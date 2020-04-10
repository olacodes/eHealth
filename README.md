# eHealth


[![CircleCI](https://circleci.com/gh/olacodes/eHealth.svg?style=svg)](https://circleci.com/pipelines/github/olacodes/eHealth)

eHealth is a digital health application system that help the hospitals to collect the medical data of their users (patients), visualise and analyse the data to make critical suggestions and assumptions that lead to solution. [eHealth Application](https://ehealths.herokuapp.com/)

## Technolgies

* [Python 3.7](https://python.org) : Base development programming language
* [Bash Scripting](https://www.codecademy.com/learn/learn-the-command-line/modules/bash-scripting) : Create convinient script for easy development experience
* [PostgreSQL](https://www.postgresql.org/) : Application backing relational databases for both staging and production environments
* [Django Framework](https://www.djangoproject.com/) : Host development framework built on top of python
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [CircleCI]() : Continous Integration and Deployment
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the appication and services orchestration
* [Jinja Template Engine](https://jinja.palletsprojects.com/en/2.11.x/) : A template engine 
* [Bootstrap 4]: (https://getbootstrap.com/docs/4.0/getting-started/introduction/) : Styling framework for building responsive, mobile-first sites
* [Cripsy form](https://django-crispy-forms.readthedocs.io/en/latest/) : control the rendering behavior of Forms for the application 
* [Cloudinary](https://cloudinary.com/) : Host Application Images

## Usage
```
Go to `http://ehealths.herokuapp.com/` 
Register as a user or practitioner
Login to the app
Fill the medication infomation form
View the statistical data of all the medical records collected \(including yours\)
As a practitioner you can view others user medical information

```
## Site Map

<div>
    <img src="https://res.cloudinary.com/olacode/image/upload/ar_1:1,b_rgb:262c35,c_fill,g_auto,r_max,w_1000,x_0,y_0,z_0.1/v1583018450/eHealth/eHealth_ohptdx.jpg" width='400px' height='400px'>
    <br /><sub><b>Sit Map</b></sub>
</div>

## How To Contribute
Few things you need to setup to get started, set up a virtual environment majorly for isolating installs, create a `.env` file from the example file and finally install all requirements in the `requirements.txt` files within the virtual environment.

Fortunately for us, we already have a convenient script for this.

Note that you do not need to bother about activating virtual environments when installing or uninstalling packages using the `bin/install` and `bin/uninstall` scripts, unless you are running them directly yourself with `pip`.

```bash

# Clone the repository
$ git clone https://github.com/olacodes/ehealth.git

# Change directory into the cloned folder and run the setup script
$ cd eHealth
$ bin/setup

# Update .env file content as necessary. Not sure if values to set? ask the Leads

# Start the application containers and open it in browser
$ bin/start -d && bin/open

```

## Running Tests

Currently, there is a simple truthy test in `eHealth/web/tests` folder. While always writing docker commands to run test in api container might become boring, we have a convenient script we can use to run tests within our started api container

```bash

# Ensure the api container is running in its own shell or in background
$ bin/test
```

## Owner

<div>
    <img src="https://res.cloudinary.com/olacode/image/upload/v1583016760/personal/sodiq_1_xorws5.webp" width='400px' height='400px'>
    <br /><sub><b>Olatunde Sodiq</b></sub>
</div>
