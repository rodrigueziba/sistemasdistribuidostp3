import socket

def main():
    host = '127.0.0.1'
    port = 12345

    # Crear un socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincular el socket al host y puerto
    server_socket.bind((host, port))

    # Escuchar conexiones entrantes
    server_socket.listen(1)
    print("Esperando conexiones...")

    conn, addr = server_socket.accept()
    print(f"Conexión entrante desde {addr}")

    with open('archivo_enviado.txt', 'rb') as file:
        data = file.read(1024)
        while data:
            conn.send(data)
            data = file.read(1024)

    print("Archivo enviado con éxito")
    conn.close()

if __name__ == '__main__':
    main()
