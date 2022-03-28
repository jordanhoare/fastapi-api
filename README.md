FastAPI // Docker // PostgreSQL 
============
[![GitHub Stars](https://img.shields.io/github/stars/jordanhoare/fastapi-api.svg)](https://github.com/jordanhoare/fastapi-api/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/jordanhoare/fastapi-api.svg)](https://github.com/jordanhoare/fastapi-api/issues) [![Current Version](https://img.shields.io/badge/version-0.5.0-green.svg)](https://github.com/jordanhoare/fastapi-api) 


## Requirements 
- [Git](https://git-scm.com/) for command-line interface 
- [Pyenv](https://github.com/pyenv/pyenv) for Python version management tool
- [Poetry](https://python-poetry.org/docs/) for dependency management and packaging
- [Docker](https://docs.docker.com/get-docker/) for developing, shipping, and running applications


</br>


## Manual Build on Your Local Machine

1. Clone the GitHub repository to an empty folder on your local machine:

    ```
    gh repo clone jordanhoare/fastapi-api
    ```

1. Build the image and spin up the two containers:

    ```
    chmod +x project/entrypoint.sh
    docker-compose up -d --build
    docker-compose exec web-db psql -U postgres
    ```

1. Create the first migration:

    ```
    docker-compose exec web aerich init-db
    ```

1. To access the database via psql:

    ```
    
    docker-compose logs web
    
    \c web_dev
    \dt
    ```


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


