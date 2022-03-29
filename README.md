FastAPI // Docker // PostgreSQL 
============
[![GitHub Stars](https://img.shields.io/github/stars/jordanhoare/fastapi-api.svg)](https://github.com/jordanhoare/fastapi-api/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/jordanhoare/fastapi-api.svg)](https://github.com/jordanhoare/fastapi-api/issues) [![Current Version](https://img.shields.io/badge/version-0.5.0-green.svg)](https://github.com/jordanhoare/fastapi-api) 


An async RESTful API with Python, FastAPI, and Postgres. FastAPI and Postgres run inside Docker containers and pytests are configured in order to practice Test-Driven Development (TDD).

</br>

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

- Build the image and spin up the two containers:
    ```
    chmod +x project/entrypoint.sh
    docker-compose up -d --build
    ```
- Create the first migration (Aerich init):
    ```
    docker-compose exec web aerich init-db
    docker-compose exec web aerich upgrade
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
</details>

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


