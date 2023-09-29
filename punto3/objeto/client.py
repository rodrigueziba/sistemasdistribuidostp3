import socket
import pickle

class Sucursal:
    def __init__(self, nombre, ubicacion, multiplicador):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.multiplicador = multiplicador

def send_update(server_address, update):
    # Crear un socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Serializar y enviar el objeto
    update_data = pickle.dumps(update)
    client_socket.sendto(update_data, server_address)

    # Cerrar la conexión
    client_socket.close()

def main():
    server_address = ('127.0.0.1', 12345)

    # Agregar sucursales y actualizar valores de combustible
    sucursal1 = Sucursal("Sucursal A", "Ubicación A", 1.5)
    sucursal2 = Sucursal("Sucursal B", "Ubicación B", 1.3)

    send_update(server_address, sucursal1)
    send_update(server_address, sucursal2)

    # Enviar un objeto de finalización
    send_update(server_address, Sucursal("FIN", "", 0))

if __name__ == '__main__':
    main()
