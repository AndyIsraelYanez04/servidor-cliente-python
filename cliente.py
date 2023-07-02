import socket

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 2020

def run_client():
    client_socket = socket.socket()
    client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
    print("Conectado al servidor: " + str((SERVER_ADDRESS, SERVER_PORT)))

    while True:
        data = input("Ingrese un mensaje para el servidor: ")
        if not data:
            break
        client_socket.send(data.encode())

        response = client_socket.recv(51200)
        if not response:
            print("El servidor no respondió")
            break
        response = response.decode()
        print("Respuesta del servidor:", response)

        # Recibir mensaje de bienvenida del servidor después de enviar el primer mensaje
        welcome_message = client_socket.recv(1024).decode()
        print("Mensaje de bienvenida del servidor:", welcome_message)

    client_socket.close()

run_client()
