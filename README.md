# **My First FastApi Example**

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