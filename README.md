# Build Instructions

![Build Status](https://microsoftdigitallearning.visualstudio.com/Courseware/_apis/build/status/MicrosoftLearning.Docker-Build?branchName=master)

## Requirements

- Latest version of [pandoc](http://pandoc.org/)
- [Git](https://git-scm.com/) command-line interface 
- [Node.js](https://nodejs.org/) version 8 or greater

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

1. Run ``npm install`` to install all required dependencies:

    ```
    npm install
    ```

1. Run ``node package.js`` to run the packaging script specifying version number and a course identifier:

    ```
    node package.js --version 1.0.0 --course INF99X
    ```

## Docker Image

If you do not have Node, Pandoc Git installed on your local machine, we have a Docker Hub image with the required versions of each tool located at: [microsoftlearning/markdown-build](https://hub.docker.com/r/microsoftlearning/markdown-build)