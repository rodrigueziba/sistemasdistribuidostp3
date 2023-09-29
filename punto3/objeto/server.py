import socket
import pickle

class Sucursal:
    def __init__(self, nombre, ubicacion, multiplicador):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.multiplicador = multiplicador

def main():
    host = '127.0.0.1'
    port = 12345

    # Crear un socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Vincular el socket al host y puerto
    server_socket.bind((host, port))

    sucursales = {}  # Diccionario para almacenar información de sucursales

    print("Esperando actualizaciones de combustible...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        update = pickle.loads(data)
        if update.nombre == 'FIN':
            break

        # Verificar si la sucursal existe en el diccionario
        if update.nombre in sucursales:
            sucursal = sucursales[update.nombre]
            sucursal.multiplicador = update.multiplicador
        else:
            sucursal = Sucursal(update.nombre, update.ubicacion, update.multiplicador)
            sucursales[update.nombre] = sucursal

        print(f"Actualización recibida desde {addr}: {sucursal.nombre} - Multiplicador: {sucursal.multiplicador}")

    print("Actualizaciones de combustible completadas")
    server_socket.close()

if __name__ == '__main__':
    main()
