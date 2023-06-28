import socket
import threading
import logging

def handle_client(client_socket, address):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            logging.info("Повідомлення від клієнта {}: {}".format(address, message))

            response = process_message(message)

            client_socket.send(response.encode("utf-8"))

        except ConnectionResetError:
            break

    client_socket.close()
    logging.info("Клієнт {} відключився.".format(address))

def process_message(message):
    if message.lower() == "привіт":
        return "Привіт! Я серверний чат-бот."
    elif message.lower() == "надішли повідомлення":
        return "Це відповідь від сервера."
    else:
        return "Ви написали: " + message

def start_server():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    logging.info("Сервер запущений. Очікування підключення...")

    client_socket, address = server_socket.accept()
    logging.info("Підключився клієнт: {}".format(address))

    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()

    while True:
        message = input("Введіть повідомлення для клієнта: ")
        if not message:
            break

        client_socket.send(message.encode("utf-8"))

    server_socket.close()
    logging.info("Сервер завершив роботу.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_server()
