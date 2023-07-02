import socket
SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 2020

def handle_client_connection(client_socket):
    while True:
        data = client_socket.recv(2048)
        if not data:
            print("Fin de la transmisión desde el cliente")
            break
        data = data.decode()
        print("Información recibida desde el cliente: " + data)
        response = "El servidor ha recibido tu mensaje: " + data
        client_socket.send(response.encode())

        # Envía el mensaje de bienvenida al cliente después de recibir el primer mensaje
        welcome_message = "¡Bienvenido al servidor!"
        client_socket.send(welcome_message.encode())

    client_socket.close()

def run_server():
    server_socket = socket.socket()
    server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
    server_socket.listen(13)
    print("Escuchando al servidor: " + str((SERVER_ADDRESS, SERVER_PORT)))

    while True:
        client_socket, addr = server_socket.accept()
        print("Cliente conectado:", addr)

        handle_client_connection(client_socket)
run_server()
