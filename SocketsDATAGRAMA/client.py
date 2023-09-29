import socket

def main():
    host = '127.0.0.1'
    port = 12345

    # Crear un socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    file_name = 'archivo_a_enviar.txt'  # Cambia esto al nombre del archivo que deseas enviar

    # Enviar el nombre del archivo al servidor
    client_socket.sendto(file_name.encode('utf-8'), (host, port))

    with open(file_name, 'r') as file:
        data = file.read(1024)
        while data:
            client_socket.sendto(data.encode('utf-8'), (host, port))
            data = file.read(1024)

    print(f"Archivo '{file_name}' enviado con éxito")
    client_socket.close()

if __name__ == '__main__':
    main()
