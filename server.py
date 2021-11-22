# Import required modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234 # we can use any port between 0 to 65535
LISTENER_LIMIT = 5
active_clients = [] # List of all currently connected users

# Function to listen for upcoming messages from a client
def listen_for_messages(client, username):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':

            final_msg = username + '~' + message
            send_messages_to_all(final_msg)

        else:
            print(f"The message send from client {username} is empty")


# Function to send message to a single client
def send_message_to_client(client, message):

    client.sendall(message.encode())

# Function to send any new message to all the clients that
# are currently connected to this server
def send_messages_to_all(message):

    for user in active_clients:

        send_message_to_client(user[1], message)






if __name__ == '__main__':
    main()