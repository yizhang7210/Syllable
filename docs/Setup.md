# Environment Setup

### Local

##### Server
1. It's recommended to have `nix` from [here](https://nixos.org/nix/download.html`).
1. You might as well install `nox` by doing `nix-env -i nox`.
1. Make sure you have docker. Download from [here](https://www.docker.com/get-started).
1. Under the `server` folder, get into your nix environment by doing `nix-shell syllable.nix`.
1. Now, do `python -m venv venv` to get into python's virtualenv (only needed for first time).
1. Activate the virtualenv by doing `. venv/bin/activate`.
1. Now let's bring up the database by doing `docker-compose up (-d)`.
1. Open a new terminal window and repeat steps 4, 5, 6 to get into the right virtualenv.
1. Finally run `./manage.py migrate` to bring DB schema up to date, then `./manage.py runserver`
to bring up the server at `localhost:8000`!
1. You might need SendGrid API token. If you do, ask the maintainer about it.

##### Frontend
1. I would get nvm first from [here](https://github.com/creationix/nvm).
1. Then it's easier to manage different versions of node/npm.
1. `nvm install v11.13.0` then `nvm use v11.13.0`.
1. Then of course, you need to do `npm install` inside `frontend` folder.
1. `npm run serve` should bring the site up locally at `localhost:8080`.


### Continuous Integration
Continuous integration happens on Circle CI. Checkout the `.circleci/config.yml` for details.

In short, every time `develop` branch advances, everything (both the server and
frontend) gets rebuilt and automatically deployed to the staging/dev environment,
accessible at `dev.getsyllable.ca`.  
Every time `master` branch advances, everything gets built and deployed to
production, accessible at `www.getsyllable.ca`.


Note that the following environment variables are required for Circle CI jobs.
- `AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY` for deploying to AWS.
- `SYLLABLE_ENV = DEPLOY` for CI specific configurations.


### Staging + Production

##### Server
The server side consists of `RDS` (PostgreSQL) for database, `Elastic Beanstalk` for
the application and `Elastic Load Balancer`.

For the application on Elastic Beanstalk. They require the following environment
variables to run:
- `DJANGO_SECRET_KEY` for django server.
- `DJANGO_SETTINGS_MODULE = syllable.settings`.
- `JWT_SECRET` used by jwt token.
- `RDS_DB_NAME`, `RDS_HOSTNAME`, `RDS_PASSWORD`, `RDS_PORT` & `RDS_USERNAME` for DB connection.
- `SENDGRID_API_KEY` for email integration with Sendgrid.
- `SYLLABLE_ENV` would be `DEV` for staging and `PROD` for production.


##### Frontend
The frontend is a static site served from `S3`, with a `CloudFront` CDN in front.
The DNS is managed by `Route53`, and SSL certs managed by AWS `Certificate Manager`.
