import socket
import threading

HOST = "0.0.0.0"
PORT = 5000


def send_messages(conn):
    try:
        while True:
            msg = input("Server: ")
            conn.sendall((msg + "\n").encode("utf-8"))
            if msg.strip().lower() == "exit":
                break
    except (EOFError, OSError):
        pass
    finally:
        try:
            conn.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Server started on port {PORT}", flush=True)
        conn, addr = server.accept()
        print("Client connected", flush=True)
        threading.Thread(target=send_messages, args=(conn,), daemon=True).start()
        reader = conn.makefile("r", encoding="utf-8")
        for line in reader:
            message = line.rstrip("\n")
            if message.strip().lower() == "exit":
                break
            print(f"\rClient: {message}")
            print("Server: ", end="", flush=True)
        print("\nClient disconnected")
        conn.close()
    except OSError as e:
        print(f"Socket error: {e}")
    except KeyboardInterrupt:
        print("\nServer stopped")
    finally:
        server.close()


if __name__ == "__main__":
    main()

