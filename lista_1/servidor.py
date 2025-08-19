import socket

questions = [
    {
        "q": "O que é um webservice?",
        "options": ["Um protocolo de segurança para proteger dados online", "Um servidor físico usado para armazenar dados na nuvem", "Um aplicativo que funciona apenas em dispositivos móveis", "Um software que permite a comunicação entre diferentes sistemas através da internet"],
        "answer": "Um software que permite a comunicação entre diferentes sistemas através da internet"
    },
    {
        "q": "Qual dos seguintes protocolos é comumente usado em webservices?",
        "options": ["SOAP", "SSH", "SMTP", "FTP"],
        "answer": "SOAP"
    }
]

def start_server():
    host = "127.0.0.1"
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Servidor aguardando conexão em {host}:{port}...")
    conn, addr = server_socket.accept()
    print(f"Cliente conectado: {addr}")

    results = []
    score = 0

    for q in questions:
        question_text = q["q"] + "\n"
        for i, opt in enumerate(q["options"], start=1):
            question_text += f"{i}) {opt}\n"


        conn.send(question_text.encode())

        answer = conn.recv(1024).decode().strip()
        print(f"Cliente respondeu: {answer}")

        try:
            chosen = q["options"][int(answer)-1]
        except:
            chosen = None

        if chosen == q["answer"]:
            results.append("Acertou")
            score += 1
        else:
            results.append("Errou  (Correta: " + q["answer"] + ")")

    summary = f"\nResultado final: {score}/{len(questions)} acertos\n"
    for i, r in enumerate(results, start=1):
        summary += f"Questão {i}: {r}\n"

    conn.send(summary.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
