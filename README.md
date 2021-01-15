# Prueba Técnica Destácame
Desarrollo de prueba técnica para postulación en Destacame.

Modelo de datos usado: ver archivo del repositorio **/db.uml** o **/db.png**

#### Vista previa: http://138.68.25.182:8080/

## Clonar repositorio git
### Primer paso:
```
$ git clone https://github.com/imoctopo/prueba-tecnica-destacame.git
```
## Instalar con Docker Compose 
Se asume que está instalado Docker y Docker Compose. \
Ejectuar los siguientes comandos dentro del repositorio clonado.

### Primer paso: construir imágenes
```
$ docker-compose build
```
### Segundo paso: ejecutar docker-compose
```
$ docker-compose up -d
```
**Url Frontend:** http://localhost:8080 \
**Url Backend:** http://localhost:8000

## Instalar backend de forma manual
Se asume que está instalada la versión *3.9.1* de **Python**. \
Ejecutar los siguientes comandos dentro de **/backend**

### Primer paso: crear ambiente virtual venv
```
$ python -m venv ./venv
```
### Segundo paso: activar ambiente virtual

_En Windows_
```
$ source venv/Scripts/activate
```
_En Linux_
```
$ source venv/bin/activate
```

### Tercer paso: instalar requerimientos
```
(venv) $ pip install -r requirements.txt
```

### Cuarto paso: realizar migraciones
```
(venv) $ python manage.py migrate
```

### Quinto paso: ejecutar servidor de desarrollo
```
(venv) $ python manage.py runserver
```

## Instalar frontend de forma manual
Se asume que está instalada la versión *1.22.5* de **Yarn**. \
Ejecutar los siguientes comandos dentro de **/frontend**

### Primer paso: instalar dependencias
```
$ yarn install
```

### Segundo paso: ejecutar servidor de desarrollo
```
$ yarn serve
```

**Url Frontend:** http://localhost:8080 \
**Url Backend:** http://localhost:8000