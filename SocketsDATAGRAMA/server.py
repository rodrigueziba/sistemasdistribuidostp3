import socket

def main():
    host = '127.0.0.1'
    port = 12345

    # Crear un socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Vincular el socket al host y puerto
    server_socket.bind((host, port))

    print("Esperando datos...")

    data, addr = server_socket.recvfrom(1024)  # Recibe el nombre del archivo
    file_name = data.decode('utf-8')

    with open(file_name, 'w') as file:
        while True:
            data, addr = server_socket.recvfrom(1024)
            if not data:
                break
            file.write(data.decode('utf-8'))

    print(f"Archivo '{file_name}' recibido con éxito")
    server_socket.close()

if __name__ == '__main__':
    main()
