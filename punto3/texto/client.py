import socket

def send_update(server_address, message):
    # Crear un socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Enviar el mensaje al servidor
    client_socket.sendto(message.encode('utf-8'), server_address)

    # Cerrar la conexión
    client_socket.close()

def main():
    server_address = ('127.0.0.1', 12345)

    # Lista de actualizaciones de combustible
    updates = [
        "INFINIA:1.5",
        "SÚPER:1.3",
        "INFINIA DIESEL:1.2",
        "ULTRADIESEL:1.1",
        "DIESEL 500:1.0"
    ]

    for update in updates:
        send_update(server_address, update)

    # Enviar un mensaje de finalización
    send_update(server_address, "FIN")

if __name__ == '__main__':
    main()
