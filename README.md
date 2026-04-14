# Criptografia_LAB_2
Este repositorio contiene la documentación, evidencias y scripts desarrollados durante el laboratorio de ciberseguridad enfocado en la ejecución y análisis de ataques de fuerza bruta sobre aplicaciones web. El entorno de pruebas se desplegó utilizando Damn Vulnerable Web App (DVWA) en un entorno aislado con Docker.

## Objetivo del Proyecto
Analizar un ataque de fuerza bruta contra un formulario de autenticación web (método GET). El proyecto abarca la intercepción de peticiones HTTP hasta la automatización del ataque y el análisis del tráfico de red para identificar firmas de herramientas ofensivas.

## Herramientas  Utilizadas
* Entorno Vulnerable: Docker, DVWA (Damn Vulnerable Web App).
* Generación de Diccionarios: Crunch, Cupp.
* Intercepción y Análisis: Burp Suite (Community Edition), cURL.
* Automatización Ofensiva: THC-Hydra, Python 3 (`requests`).
* Análisis de Tráfico: Wireshark.

## Fases del Laboratorio
1. Despliegue del Entorno: Configuración de DVWA en un contenedor Docker con redirección de puertos (8081:80) para evitar conflictos de red.
2. Reconocimiento e Intercepción: Captura de peticiones HTTP, análisis de cookies de sesión (`PHPSESSID`) y variables del nivel de seguridad mediante Burp Suite y herramientas de desarrollador (Inspect Element).
3. Explotación Automatizada: Uso de **Burp Suite Intruder** (Cluster Bomb) para probar combinaciones.
   * Ejecución de **cURL** interactivo para validar accesos por terminal.
   * Despliegue masivo con **Hydra** filtrando falsos positivos mediante validación de respuestas (`S=Welcome`).
   * Desarrollo de un **Script en Python**, utilizado para evadir limitaciones de software de terceros.
4. Análisis de Red: Captura de tráfico en la interfaz de loopback (lo) con Wireshark para diferenciar firmas, `User-Agents` y comportamientos anómalos (volumen y concurrencia) entre el tráfico real y el automatizado.
5. Mitigación: Propuesta de remediaciones a nivel de servidor y aplicación (Rate Limiting, CAPTCHAs, MFA, Account Lockout).

## Uso del Script en Python
En el repositorio se incluye un script personalizado `brute.py` que demuestra cómo interactuar programáticamente con el formulario vulnerable.

Para ejecutarlo:
1. Tener los archivos `usuarios.txt` y `contrasenas.txt` en el mismo directorio.
2. Actualizar la variable `PHPSESSID` dentro del script, esto se logra con la cookie de sesión activa.
3. Ejecuta el script en la terminal:
   python3 brute.py



   
