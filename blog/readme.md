Welcome to May Blog
====================

##Why name it MayBlog?

Just because it is a blog system and started in May, 2015, and MayBlog is vivid.
 :P

##Features

MayBlog is a django based blog system with following features:

- multiuser
- multirole (under development)
- posts, pages, tags, and categories
- markdown support
- admin interface
- RESTful API (under development)
- multiple setting files, easily switch environment: dev, prod, custom, etc

To Do:

- allow register flag
- roles
- access limitation by roles
- RESTful API

##How to run it ?

###Install requirements

```
(sudo) pip install -r requirements.txt 
```

###Create/update datebase

For the first time, before you start the application, you need to initialize the datebase which is configured in the `settings file` and designed in `main.models.py`

```bash
python manage.py migrate
```

If the models are changed after the datebase is created, you need to run the following commands:

```bash
python manage.py makemigrations #create migration script
python manage.py migrate #migrate datebase
```

###Run MayBlog

After the datebase is established, you can run the blog with command:

```bash
python manage.py runserver 0.0.0.0:8000
```

Then you can visit the blog with url: http://127.0.0.1:8000

###Admin MayBlog

You can create a superuser to administer MayBlog in its admin interface:

```bash
python manage.py createsuperuser
```

Then, you can administer MayBlog with following admin interface:

- MayBlog admin: http://127.0.0.1:8000:admin/
- Django's default admin: http://127.0.0.1:8000:admin2/

- Login page: http://127.0.0.1:5000/accounts/login/
- Register page: http://127.0.0.1:5000/accounts/register/ (if `REGISTER_IS_ALLOWED` is set to True in settings)

###MayBlog settings

By default, MayBlog uses dev settings(`blog.settings.dev`) in `blog/settings/dev.py` in development environment. 

`blog.settings.prod` is used in product environment and `blog.settings.stage` is in test environment. You can overwrite these settings or create your custom settings and switch to it.

####How to switch to your aim settings

Just set your settings in bash with `export` command. For example, if you want to run MayBlog in product environment, you can switch to prod settings like this:

```
export DJANGO_SETTINGS_MODULE="blog.settings.prod"
```

###What's more

If you find a bug or want to add a new feature, just issue me.
Want to contribute? Please fork MayBlog and pull request to me.

I'm not good at frontend development, so I used a free bootstrap blog theme. If you can redesign the blog theme and admin interface, I'll appriciate your work very much!

