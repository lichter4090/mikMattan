import socket
import select
import json


with open("server_info.txt", "r") as server_info:
    LISTENING_PORT = int(server_info.read().split("\n")[1])

connected_clients = list()
connected_mattans = dict()

NUM_OF_FIELDS_IN_MSG = 7


def open_listening_socket(listening_port):
    """
    function for opening a listening socket that will listen in the listening port that is the argument
    :param listening_port: the port to listen to
    :type listening_port: int
    :return: listening socket that is listening in the port given
    :rtype: socket obj
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # open socket

    sock.setblocking(False)  # this makes the socket that all the methods on the socket (.recv(), .accept()...) will not wait until
    #  until it works, it will just check one time and move on (important for handling many clients)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # making the socket that it could reuse the local address in case the socket is closed and then reopened immediately

    sock.bind(('', listening_port))  # bind listening port
    sock.listen(10)  # set listening for many users

    return sock


def get_client_info(listening_socket):
    """
    function for returning info about the client that connected
    to the server (socket object, client address).
    :param listening_socket: listening socket of the server
    :type listening_socket: socket obj
    :return: info about client
    :rtype: tuple
    """
    return listening_socket.accept()


def try_get_data_from_client(client_soc):
    """
    function for trying to get data sent from client
    :param client_soc: the conversation socket of the client
    :type client_soc: socket obj
    :return: list containing the headers and data sent from user ([Header, Data(optional)])
    :rtype: list
    """
    try:
        client_msg = client_soc.recv(1024).decode()  # try to get client's msg

        return json.loads(client_msg)

    except Exception:  # in case client shutdown
        return list()  # return empty list


def handle_new_client(client_sock):
    """
    function for handling a new client that is just connected to the server
    :param client_sock: the socket of the client
    :type client_sock: socket obj
    :return: None
    :rtype: None
    """
    connected_clients.append(client_sock)  # add the client to the list of the connected clients
    client_sock.setblocking(False)

    print("New client:", client_sock.getpeername())


def handle_leaving_client(client_sock):
    """
    function for handling a client that is disconnecting the server
    :param client_sock: the socket that is disconnecting
    :type client_sock: socket obj
    :return: None
    :rtype: None
    """
    print(client_sock.getpeername(), "Disconnected from server")
    del connected_mattans[client_sock]
    client_sock.close()
    connected_clients.remove(client_sock)


def update_character_data(client_socket, character_data):
    """
    Update character data for a connected client.
    :param client_socket: The client's socket.
    :param character_data: The character data to update.
    """
    connected_mattans[client_socket] = character_data


def get_all_mattans():
    """
    Get character data for all connected clients.
    :return: A list of character data.
    """
    return [mattan for mattan in connected_mattans.values()]


def one_iteration_of_program(sock, data):
    update_character_data(sock, data)


def main():
    listening_sock = open_listening_socket(LISTENING_PORT)
    
    while True:
        readable_sockets = select.select([listening_sock] + connected_clients, [], [])[0]
        
        for sock in readable_sockets:
            if sock is listening_sock:
                client_socket, address = listening_sock.accept()
                handle_new_client(client_socket)
            else:
                data = try_get_data_from_client(sock)

                if len(data) == NUM_OF_FIELDS_IN_MSG:
                    one_iteration_of_program(sock, data)
                else:
                    handle_leaving_client(sock)
        
        for client_socket in connected_clients:
            all_mattans_except_yours = list()

            for key, value in connected_mattans.items():
                if key != client_socket:
                    all_mattans_except_yours.append(value)

            data_to_send = json.dumps(all_mattans_except_yours)
            client_socket.sendall(data_to_send.encode())


if __name__ == "__main__":
    main()
