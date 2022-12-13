# Moringa Graduates

![Project Image](app/static/app/images/readme-image.png)

### By: Samuel Martins

## Table of Content

- [Description](#description)
- [Installation Requirement](#usage)
- [Technology Used](#technologies)
- [Licence](#licence)
- [Authors Info](#author-info)

## Description

This is a django application that provides a platform for all Moringa School graduates to create a profile for themselves for post-graduate hiring purposes. [live site]()

# Note: 
This project is by no means complete. Therefore, don't be alarmed when you encounter bugs in any form. Development is ongoing

## Behaviour Driven Development

The user ( developer ) is able to;

- Sign in to the application to start using it

- Set up a profile about themselves 

- Fill in their experience and acheivements

- Search for other developers


The user ( recruiter ) is able to;

- Veiw the applicaition in all its glory

- Search for developers by technology, stack, or name

- Directly message a specific developer within the platform




## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

These are the things you need to install the software and how to install them

```
virtual enviroment:

$ pipenv shell

or

$ python3 -m venv virtual ( or your selected virtual enviroment name )
```

### 1. Local Repository

- Make sure you have a stable internet to have the ability to clone the repository.
- Type the following command in your terminal to clone this repository

```
git clone https://github.com/thesmartcoder7/moringa-graduates.git

```

If you are using SSH, use the following command

```
git clone git@github.com:thesmartcoder7/moringa-graduates.git
```

When you run the commands successfully, you should have a local version of this repository.

### 2. Online Repository

- Make sure you have a stable internet for forking this repository.
- According to the license, you can fork this project. You need to click on the forking icon and it will be added as one of your repositories

Feel free to fork the project and have fun with it. Happy coding!

### Installing

To get a development env running, you simply need the install all the packages reguired from either a requirements.txt file or a pipfile. First you need to activate your virtual environment

```
$pipenv shell

of

$ source virtualenvname/bin/activate
```

after that, install all the required depencencies

```
$ pipenv install //pretty much takes care of installing all depencies for you
```

Now that all your dependencies are installed, you need to create a local database for your project and run migrations, or use the database that django comes with by default. The Make file has instructions for this.

```
make migrate
```

After this, you can run the application using the commands that come in the make file. for this case, it is either of the following:

```
$ make

or

$ make run

or

$ python manage.py runserver

```

## Running the tests

If you want to run tests for the entire project, you need only run this command:

```
$ make test

or

$ python manage.py test
```

## Technologies

- HTML5
- SCSS
- JavaScript
- Django
- Postgresql

## Licence

Copyright (c) Samuel Martins - [MIT Licence](LICENSE)

## Author Info

- Twitter - [@thesmartcoder7](https://twitter.com/thesmartcoder7)
- Linkedin - [Samuel Martins](https://www.linkedin.com/in/samuel-martins-09839b115/)
- Website - [Samuel Martins](https://smart-code.dev)
- blog - [Samuel Martins](https://samuel-martins.medium.com/)