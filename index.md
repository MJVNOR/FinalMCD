## Trabajo Final Curso Herramientas de Productividad para Ciencia de Datos

### Introducción 
Esta es una pagina para explicar una problematica con un dataset de la [dirección general de epidemiología](https://www.gob.mx/salud/documentos/datos-abiertos-152127). Utilizando un Dockerfile y herramientas vistas en el curso se resolvera esta problematica.

### problematica
Se busca graficar la cantidad de personas con covid que estan entubadas y que tuvieron neumonia en edades de entre 20 y 40 y mas de 40 y comparando entre hombres y mujeres.

1.- Descargamos el repositorio.
```
git clone https://github.com/MJVNOR/FinalMCD.git
```
2.- Generamos la imagen del Dockerfile
```
docker build -t datoscovid .
```
3.- Generamos un contenedor
```
docker run -it --name ContenedorCovid datoscovid
```

[Image](./documentos/fig1.png)
