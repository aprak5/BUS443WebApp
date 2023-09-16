# BUS 443 (Web Development for Business) Final Project

## Description

As a part of the final project for the course, a web application was made as a small-scale enrollment management system. This application could be something a department course scheduler or admin uses to manage courses enrollment between students and/or teachers in the department. The application includes an admin management page along with the home, login, student info, course info, and enrollment info pages. All pages except the login page is protected, so valid user credentials are required to view the other pages. A brief overview of the application architecture can be found below.

![](https://github.com/aprak5/BUS443WebApp/blob/main/images/bus44projectarch.jpg?raw=true)

## Prerequisites

To run the web application, make sure the following prerequisites have been met:

- PostGreSQL installed (version >= 16) (pgadmin4 is highly recommended)
- Python installed (version >= 3.11.0) with path set in pyvenv.cfg
- Superuser finaluser exists and is owner of studentinfo, courseinfo, and enrollmentinfo tables (User: finaluser, Password: finaluser)
- Working directory is the repository (BUS443WebApp)
- Virtual environment is active (To activate: run `443django/Scripts/Activate`)
- User exists (To make the user: run  `python finalproject/manage.py createsuperuser`)
- All migrations have been made (To make migrations: run `python finalproject/manage.py migrate`)

## Run Commands

To run the web application:

- Run using the command `python finalproject/manage.py runserver`
- Access the app on a web browser by typing `http://127.0.0.1:8000/login`
- Log into the app using the credentials of the user made in the createsuperuser command
- To exit, run the command `Deactivate`
