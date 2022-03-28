FastAPI // Docker // PostgreSQL 
============
[![GitHub Stars](https://img.shields.io/github/stars/jordanhoare/fastapi-api.svg)](https://github.com/jordanhoare/fastapi-api/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/jordanhoare/fastapi-api.svg)](https://github.com/jordanhoare/fastapi-api/issues) [![Current Version](https://img.shields.io/badge/version-0.5.0-green.svg)](https://github.com/jordanhoare/fastapi-api) 


## Requirements 
- Python (^3.8.2)
- [Git](https://git-scm.com/) command-line interface 
- Poetry (https://python-poetry.org/docs/)

</br>

## Manual Build on Your Local Machine

1. Clone the GitHub repository to an empty folder on your local machine:

    ```
    git clone https://github.com/MicrosoftLearning/Docker-Build.git .
    ```

1. Clone another GitHub repository of the course you would like to build your local machine:

    ```
    git remote add course https://github.com/MicrosoftLearning/INF99X-Sample-Course.git
    git fetch course
    git merge course/master --allow-unrelated-histories
    ```

    > In this example, we are using the sample course [INF99X: Sample Course](https://github.com/MicrosoftLearning/INF99X-Sample-Course)


</br>

## Build Docker

```
docker-compose up -d --build

docker-compose exec web aerich init-db

docker-compose exec web-db psql -U postgres

\c web_dev
\dt
\q
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


