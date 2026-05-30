## Explicación de los Archivos Implementados

### app.py

Archivo principal del microservicio desarrollado con Flask.

Funciones implementadas:

- Creación de la aplicación Flask.
- Endpoint `/` para verificar el funcionamiento de la API.
- Endpoint `GET /tareas` para obtener las tareas registradas.
- Endpoint `POST /tareas` para agregar nuevas tareas.
- Ejecución del servidor en el puerto 5000.

---

### requirements.txt

Archivo que contiene todas las dependencias necesarias para ejecutar el proyecto.

Dependencias utilizadas:

- Flask: Framework para construir la API.
- PyTest: Ejecución de pruebas unitarias.
- PyTest-Cov: Generación de cobertura de pruebas.
- Bandit: Análisis estático de seguridad (SAST).
- Pip-Audit: Análisis de vulnerabilidades en dependencias (SCA).

---

### test_app.py

Archivo que contiene las pruebas unitarias del proyecto.

Pruebas realizadas:

- Verificación del endpoint principal.
- Validación del código de respuesta HTTP.
- Apoyo al cálculo de cobertura de código.

---

### Dockerfile

Archivo encargado de construir la imagen Docker de la aplicación.

Configuración implementada:

- Utilización de Python 3.12 como imagen base.
- Definición del directorio de trabajo.
- Copia de dependencias y código fuente.
- Instalación automática de librerías.
- Exposición del puerto 5000.
- Configuración del comando de inicio de la aplicación.

---

### docker-compose.yml

Archivo utilizado para desplegar el entorno completo de forma local.

Configuraciones implementadas:

- Construcción automática del contenedor.
- Exposición del puerto 5000.
- Variables de entorno.
- Volumen persistente.
- Red personalizada.
- Healthcheck para verificar disponibilidad del servicio.
- Estrategia de reinicio automático.

---

### ci-cd.yml

Pipeline CI/CD implementado mediante GitHub Actions.

Etapas ejecutadas:

1. Descarga del código desde GitHub.
2. Instalación de dependencias.
3. Ejecución de pruebas unitarias.
4. Generación de cobertura de pruebas.
5. Análisis SAST mediante Bandit.
6. Análisis SCA mediante Pip-Audit.
7. Construcción de la imagen Docker.

---

### dependabot.yml

Configuración de Dependabot para la actualización automática de dependencias.

Funciones:

- Monitoreo de librerías Python.
- Monitoreo de GitHub Actions.
- Generación automática de Pull Requests cuando existen nuevas versiones disponibles.

---

### GitHub Actions

Se implementó automatización continua para validar el proyecto en cada cambio enviado al repositorio.

Beneficios:

 -Detección temprana de errores.
 -Verificación automática de calidad.
 -Construcción continua de la aplicación.
 -Validación de seguridad y dependencias.

## Reflexión Final

Durante el desarrollo de este proyecto surgieron diversos desafíos técnicos relacionados con la configuración de Docker, Docker Compose, GitHub Actions, análisis de seguridad y automatización del pipeline CI/CD.

Para resolver algunos problemas de configuración y comprender mejor determinadas herramientas, se utilizaron recursos de apoyo y asistencia basada en inteligencia artificial como complemento al aprendizaje, permitiendo investigar errores, validar configuraciones y fortalecer la comprensión de los conceptos aplicados.

A pesar de las dificultades encontradas, se logró implementar satisfactoriamente un entorno automatizado que incorpora pruebas, análisis de seguridad, contenedorización y despliegue reproducible mediante Docker Compose, cumpliendo los objetivos propuestos para la evaluación.

