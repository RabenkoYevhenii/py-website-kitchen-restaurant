# py-website-kitchen-restaurant 
## Features
* It is a web-site for restaurants with ukrainian kitchens.
Using this web-site, it is easy to represent your restaurant`s menu to guests.

* In this project is implemented registration system.

* With this project you can interact with such models as: Dish types, Dishes, Cooks.

* There are three pages with build in search, pagination and such operation as create, update, delete on every model.

* There is detailed information about every dish type, dishes and cooks on appropriate detail page.

* You can use navigation toolbar to switch pages, or on the main page there are clickable names: Types of dishes, Dishes, Cooks.
Each of these names will take you to the appropriate page.

## How it works
Django project for restaurant kitchen management

![diagram.png](images%2Fdiagram.png)


## Check it out!

[Kitchen restaurant project deployed to Render](https://kitchen-restaurant-customized.onrender.com/)

## Installing
#### Python3 must be already installed

_Set up the environment_

```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
```
_Set up requirements_
```
pip install -r requirements.txt
```
_Set up database_

_Use following command to load data from database_ 

`python manage.py loaddata kitchen_restaurant_data.json`

_Use following command to run server_

`python manage.py runserver`

### Log in
You can use below credentials to log in with available CRUD operation:

username: `admin`

password: `1qazcde3`

Or you can create your own superuser using following command:

`python manage.py createsuperuser`

Or log in without available CRUD operation as usual user with these credentials:

username: `test`

password: `test12345`

## Demo

![home_page.png](images%2Fhome_page.png)


![dish_types.png](images%2Fdish_types.png)


![dish_list.png](images%2Fdish_list.png)


![cook_page.png](images%2Fcook_page.png)
