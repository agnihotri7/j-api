JIRA-API's
=============
REST API's to create/update/complete/list task assigned for a project(Similar to JIRA).

# Installation

## Clone Project

    git clone https://github.com/agnihotri7/j-api.git

## Virtual Envirnoment and requirements

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

## Create db for project.

    python manage.py syncdb

## Running Development Server

    python manage.py runserver
