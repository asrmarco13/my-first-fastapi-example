# **My First FastApi Example**

<p align="center">
  <a href="https://github.com/asrmarco13/my-first-fastapi-example/blob/master/LICENSE"><img alt="License: GPL3" src="https://img.shields.io/github/license/asrmarco13/my-first-fastapi-example"></a>
  <a href="https://github.com/asrmarco13/my-first-fastapi-example"><img alt="Latest commit" src="https://img.shields.io/github/last-commit/asrmarco13/my-first-fastapi-example/master"></a>
  <a href="https://github.com/asrmarco13/my-first-fastapi-example/issues"><img alt="Open Issues" src="https://img.shields.io/github/issues/asrmarco13/my-first-fastapi-example"></a>
  <a href="https://github.com/asrmarco13/my-first-fastapi-example/issues?q=is%3Aissue+is%3Aclosed"><img alt="Closed Issues" src="https://img.shields.io/github/issues-closed/asrmarco13/my-first-fastapi-example"></a>
  <a href="https://github.com/asrmarco13/my-first-fastapi-example/pulls"><img alt="Pull requests" src="https://img.shields.io/github/issues-pr/asrmarco13/my-first-fastapi-example"></a>
  <a href="https://github.com/asrmarco13/my-first-fastapi-example"><img alt="Stars" src="https://img.shields.io/github/stars/asrmarco13/my-first-fastapi-example?style=social"></a>
  <a href="https://github.com/asrmarco13/my-first-fastapi-example"><img alt="Watchers" src="https://img.shields.io/github/watchers/asrmarco13/my-first-fastapi-example?style=social"></a>
<p>

## **Summary**
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Execute project](#execute-project)
4. [Interactive api docs](#interactive-api-docs)
5. [Testing](#testing)

### **Introduction**

An example project based on [FastApi](https://fastapi.tiangolo.com/). Minimum Python version is 3.8

### **Prerequisites**

Create a random secret key that will be used to sign the JWT tokens. To generate a secure random secret key use the command:

```shell
openssl rand -hex 32
```

Copy the output to the variable **SECRET_KEY** in ***app/core/settings.py***

Install [PostgreSQL](https://www.postgresql.org/download/) or use the [docker image](https://hub.docker.com/_/postgres).

Create an instance DB and put the connection infos in ***.env*** file.

Install the tool [Pipenv](https://github.com/pypa/pipenv).

Go to ***app*** folder and run:

```shell
pipenv install --dev
```

### **Execute project**

Go to ***app*** folder and run:

```shell
python app.py
```

Open your browser at http://127.0.0.1:8080/hello

You will see the JSON response as:

```json
{"message": "Welcome to my FastApi example"}
```

### **Interactive api docs**

Now go to http://127.0.0.1:8000/docs.

You will see the automatic interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui)).

### **Testing**

Go to ***app/tests*** folder and run:

```shell
pytest
```