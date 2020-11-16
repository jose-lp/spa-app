# Proyecto2: spa-app
---
Este repositorio contene la implementación de una aplicación web de citas para un spa. 

## Dependencias
Debe ejecutar el siguiente comando para instalar las dependencias:

```
    apt-get update && apt-get install -y \
        python3
        python3-pip \
        sqlite3
```
Dependencias de python:

```
    pip3 install Django django-bootstrap3
```

## Instrucciones de uso

### Desde la máquina host:
1) Para levantar la página ejecute `make`

2) Para acceder a la página coloque en el navegador 127.0.0.1:8000/home 
### Desde un contenedor Docker:
1) Para construir la imagen del dockerfile ejecute `make docker_build`.

2) Para crear un contenedor con la aplicación ejecute make `docker_run`. 

3) Para acceder a la página coloque en el navegador localhost:8000/home

## Contribuyentes
- [hdezmariela](https://gitlab.com/hdezmariela)  Mariela Henández Chacón
- [joselp](https://gitlab.com/joselp) José López Picado


## Repositorio oficial

Puede consultar el repositorio del proyecto desde [aquí]().

## Licencia
- MIT
