# Adventure Lookup

Open repository for the website https://adventurelookup.com/

## Quickstart

### Dependencies
If you just want to run the website on your machine.
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "Install Git")
* [Docker](https://docs.docker.com/engine/installation/ "Install Docker")
* [Docker-Compose](https://docs.docker.com/compose/install/)

### Dev Dependencies
If you want to develop you'll probably want one or more of the following:
* [NodeJS](https://nodejs.org/en/download/ "Install Node")
* [Python 3.4+](https://www.python.org/downloads/ "Install Python")

### Steps
(For Linux/OSX, if someone knows the Windows equivalents I'm happy to add them)

1. Clone the repository & cd into it

  `git clone https://github.com/petertrotman/adventurelookup`
  `cd adventurelookup`

2. Build the docker files (may take some time but there's lots of whizzing text!)

  `docker-compose build`

3. Create the admin superuser (you will be prompted for a username and password)

  `docker-compose run --rm api python manage.py createsuperuser`

  (`--rm` ensures the container is removed after its done what it needs to do)

4. Carry out the database migrations

  `docker-compose run --rm -u root api python manage.py makemigrations`

  `docker-compose run --rm -u root api python manage.py migrate`

  (we need to run as root in the container with `-u root` because the default user doesn't have write access to the code files)

5. Run the server!

  `docker-compose up`

6. (Optional) Run the production server!

  `docker-compose -f docker-compose.prod.yml up`

7. Navigate to the homepage in your favorite browser at `http://localhost`

8. Add some signup e-mails on the homepage

9. Watch Matt's about video on the /about page

10. Navigate to `/api/admin`, and enter your superuser credentials to check out your added sign-up emails.

11. Stop the server

  (in the server terminal) `ctrl+c`

  --or--

  `docker-compose stop`

12. (Only if you want to get rid of it all) Remove the Docker images

  `docker-compose rm -v`

## Technology Stack
In no particular order:
* [Docker](https://www.docker.com/): An excellent way to package complex web apps together in a nice development environment so that anyone can run the same code.
* [Django](https://www.djangoproject.com/): Very mature and well-respected web framework in Python.
* [DjangoRestFramework](http://www.django-rest-framework.org/): A Django framework for creating fully-fledged APIs quickly.
* [Nginx](https://www.nginx.com/): A high performance web server.
* [Postgres](https://www.postgresql.org/): Enterprise-grade database which tonnes of awesome features.
* [React](https://facebook.github.io/react/): Facebook's ultra trendy component rendering library (which is actually very cool).
  Along with:
  * [[React-Router](https://github.com/reactjs/react-router): The official routing solution for react.
  * [Redux](https://github.com/reactjs/redux): An atomic state management library.

## Next Steps
Please feel free to get started! I will be posting some open issues up over the next few days, but it should be obvious what can be done right away. If you want to dive right in, the next big projects to tackle are:
* The Adventures model definitions and API
* Better styling (I'm no designer...)
* The Adventures front end search and input
* TESTS! We're using Jest for tests for the frontend and the Django test framework for the backend.
* Documentation - it's minimal right now, the first things that need to be filled in are the READMEs in the client and server folders to help people to get started quicker.
* Data - we will need a decent set of data for development, so a table of adventures would be really useful.

I'll be active on the [Discord channel](https://discordapp.com/channels/181982909752803330/181982909752803330) so please come by and ask any questions there.

Hope to see a few of you join me on this endeavour :-)

-- Peter
