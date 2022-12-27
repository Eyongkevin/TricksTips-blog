!['logo'](docs/img/bannar2.png)

[MyTricksnTips](https://www.mytricksntips.com/) provides you with useful Tricks and Tips to help you up-to-date with the latest technologies. All Tricks and Tips are simple, easy-to-follow and practical.

## Tech Stacks

MyTricksnTips uses the following tech stacks;

- Django
- PostgreSQL
- Gunicorn
- Css
- JavaScript
- HTML5
- Makefile

## How To Run

While this blog is hosted on [railway app](https://railway.app), we have set up two ways to run it locally

**NB** Make sure to

- create a virtual environment
- install all dependencies
- set up your environment
  variables
- Migrate, either with `make dev-migrate` or `make prod-local-migrate` base on which environment you want to run on(Check below)

### Using Django wsgi (dev)

- This uses sqlite3 for the database.
- Consumes environment variables from the `.env` file.

```
$ make dev
```

### Using Gunicorn and Nginx (local prod)

**NB** This uses postgreSQL, so make sure to set it and put credentials in an environment file named `.env.prod`

- Locate your nginx. On mac, it is located at `/user/local/etc/nginx`. Then add the following settings to `http{..}`

```
    server {
        listen 80;
        server_name localhost;

        access_log /var/log/nginx/access.log;     # <- make sure to create the logs directory
        error_log /var/log/nginx/error.log;       # <- you will need this file for debugging

        location = /favicon.ico {
            access_log off;
            log_not_found off;
        }

        # location / {
        #   try_files $uri @proxy_to_app;
        # }
        location /static/ {
            alias /usr/local/var/www/mtt/staticfiles/;  # <- let nginx serves the static contents
        }

        location / {
            proxy_pass http://localhost:8000;         # <- let nginx pass traffic to the gunicorn server
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $host;
            proxy_redirect off;
        }
    }
```

make sure to create the directory `/var/log/nginx/` for nginx logs and `/usr/local/var/www/mtt/staticfiles` for collectstatic to dump all your static files.

- dump the static files with `make cs-g`
- Start nginx `sudo brew services start nginx` or `sudo nginx`
- Run the django project `make dev-g`

### How to contribute

[MyTricksnTips](https://www.mytricksntips.com/) is an [open source](https://opensource.com/resources/what-open-source) project. I am open to suggestions and willing to extend it to a different level. Anyone willing to contribute is highly welcomed.
To contribute, go ahead and:

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :blush:
