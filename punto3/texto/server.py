import socket

def main():
    host = '127.0.0.1'
    port = 12345

    # Crear un socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Vincular el socket al host y puerto
    server_socket.bind((host, port))

    print("Esperando actualizaciones de combustible...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode('utf-8')
        if message == 'FIN':
            break
        print(f"Actualización recibida desde {addr}: {message}")

    print("Actualizaciones de combustible completadas")
    server_socket.close()

if __name__ == '__main__':
    main()
