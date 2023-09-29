import socket

def main():
    host = '127.0.0.1'
    port = 12345

    # Crear un socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servidor
    client_socket.connect((host, port))

    with open('archivo_recibido.txt', 'wb') as file:
        data = client_socket.recv(1024)
        while data:
            file.write(data)
            data = client_socket.recv(1024)

    print("Archivo recibido con éxito")
    client_socket.close()

if __name__ == '__main__':
    main()
