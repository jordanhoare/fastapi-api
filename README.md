[![GitHub Stars](https://img.shields.io/github/stars/jordanhoare/fastapi-api.svg)](https://github.com/jordanhoare/fastapi-api/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/jordanhoare/fastapi-api.svg)](https://github.com/jordanhoare/fastapi-api/issues) [![Current Version](https://img.shields.io/badge/version-0.5.0-green.svg)](https://github.com/jordanhoare/fastapi-api) 

</br>

An async RESTful API with Python, FastAPI, and Postgres. FastAPI and Postgres run inside Docker containers and pytests are configured in order to practice Test-Driven Development (TDD).

</br>


## Dev Objectives
- [x] Develop an asynchronous RESTful API with Python and FastAPI
- [x] Practice Test-Driven Development
- [x] Test a FastAPI app with pytest
- [x] Interact with a Postgres database asynchronously
- [x] Containerize FastAPI and Postgres inside a Docker container
- [ ] Run unit and integration tests with code coverage
- [ ] Improve code quality with linter
- [ ] Configure GitHub Actions for continuous integration and deployment
- [ ] Speed up a Docker-based CI build with Docker Cache
- [ ] Deploy FastAPI, Uvicorn, and Postgres to Heroku with Docker
- [ ] Run tests in parallel
- [ ] Run a background process outside the request/response flow

</br>



## Installation & Usage

<details>
  <summary>Requirements</summary>

</br>

- [Git](https://git-scm.com/) for command-line interface 
- [Pyenv](https://github.com/pyenv/pyenv) for Python version management tool
- [Poetry](https://python-poetry.org/docs/) for dependency management and packaging
- [Docker](https://docs.docker.com/get-docker/) for developing, shipping, and running applications
</details>

</br>

<details>
  <summary>Reproduction on a local machine</summary>

</br>

- Clone the GitHub repository to an empty folder on your local machine:
    ```
    gh repo clone jordanhoare/fastapi-api
    ```
- Initialise poetry:
    ```
    poetry build
    ```
- Build a docker image and run the container in detached mode:
    ```
    docker-compose build
    docker-compose up -d
    docker-compose logs web
    ```
- Check the logs of the web service:
    ```
    docker-compose logs web
    ```
</details>

</br>

<details>
  <summary>Useful docker commands</summary>

</br>

- Bring down the containers and volumes
    ```
    docker-compose down -v
    ```
- Build the image and spin up the two containers:
    ```
    docker-compose up -d --build
    ```
- Apply migration:
    ```
    docker-compose exec web aerich upgrade
    ```
- Access data tables via psql:
    ```
    docker-compose exec web-db psql -U postgres
    \c web_dev
    \dt
    ```
- With the containers up and running, run the tests:
    ```
    docker-compose exec web python -m pytest
    ```
- Generate schema via Tortoise:
    ```
    docker-compose exec web python app/db.py
    ```
- Create the first migration (Aerich init):
    ```
    docker-compose exec web aerich init-db
    ```
- Define entrypoint:
    ```
    chmod +x project/entrypoint.sh
    ```
</details>

</br>

<details>
  <summary>CRUD / API Interaction</summary>

</br>

- Test routes with HTTPie::
    ```
    http --json POST http://localhost:8004/summaries/ http://testurl.io
    ```
</details>

</br>

</br>

</br>

</br>

</br>

<p align="center">
    <a href="https://www.linkedin.com/in/jordan-hoare/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
    </a>&nbsp;&nbsp;
    <a href="https://www.kaggle.com/jordanhoare">
        <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" />
    </a>&nbsp;&nbsp;
    <a href="mailto:jordanhoare0@gmail.com">
        <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
    </a>&nbsp;&nbsp;
</p>


