Welcome to May Blog
====================

##Why it named MayBlog?

Just because it is a blog system started in May, 2015. MayBlog is vivid.

:stuck_out_tongue: :stuck_out_tongue: :stuck_out_tongue:

##Features

MayBlog is a blog system with following features:

- Powered by django and bootstrap
- Deployed by docker
- Multiple deployment setting files
- Search engine optimized
- Blog features:
    - multi-user
    - multi-role
    - posts, pages, tags, and categories
    - markdown support
    - admin interface
    - RESTful API (under development)



##How to run it ?

###Run from source code

If you want to see more about the source code, checkout the [source code readme](blog)


###Run by docker(recommended)

Run MayBlog by docker is recommended, here are some instruction：

####First Run

1. Build your own MayBlog image
```bash
(sudo) docker-compose build

#Now you can take a cup of coffee and wait for a few minutes :)
```
2. Run MayBlog
```bash
(sudo) docker-compose up -d
```
3. Get into MayBlog container and migrate database
```bash
#Specify MayBlog container ID, eg:12345678
(sudo) docker ps

#Get into MayBlog container
(sudo) docker exec -it 12345678 bash

#Migrate datebase
python manage.py migrate
```

####After first run

- Start MayBlog

```bash
(sudo) docker-compose start
```

- Stop MayBlog

```bash
(sudo) docker-compose stop
```


###Initialize MayBlog

When the blog is run, checkout `http://host:port/init` to initialize the system

It will create the superuser, user groups(administrator, editor, writer, contributor, and reader), and assign permissions for each group.

##What's more

If you find a bug or want to add a new feature, just issue me.
Want to contribute? Please fork MayBlog and pull request to me.

I'm not good at frontend development, so I used a free bootstrap blog theme. If you can redesign the blog theme and admin interface, I'll appriciate your work very much!

