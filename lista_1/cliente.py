import socket

def start_client():
    host = "127.0.0.1"
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    for _ in range(2): 
        question = client_socket.recv(1024).decode()
        print("\n" + question)

        answer = input("Digite o número da resposta: ")
        client_socket.send(answer.encode())

    result = client_socket.recv(2048).decode()
    print("\n" + result)

    client_socket.close()

if __name__ == "__main__":
    start_client()
