# Auth Microservice

This service is intended to serve as auth microservice.

Generate your own SECRET KEY with this command, and modify `.env` file

```bash
openssl rand -hex 32
```

## Requirements

Install docker.

## Steps

1. 

```bash
docker-compose build
```

2.

```bash
docker-compose up
```

## Áreas de mejora:

1. Que en el Settings haya un campo `DEFAULT_TOKEN_CLAIMS` que sea una lista, la cual modifique lo que devuelve el JWT. Se deben de hacer modelos de pydantic que verifiquen que los token efectivamente devuelvan esa información

2. Conexión con la base de datos.

3. Que se genere un log de las conexiones usando Background Tasks.