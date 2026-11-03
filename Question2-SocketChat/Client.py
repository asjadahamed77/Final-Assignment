import socket
import threading

SERVER_IP = "127.0.0.1"
PORT = 5000


def send_messages(sock):
    try:
        while True:
            msg = input("Client: ")
            sock.sendall((msg + "\n").encode("utf-8"))
            if msg.strip().lower() == "exit":
                break
    except (EOFError, OSError):
        pass
    finally:
        try:
            sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((SERVER_IP, PORT))
        print("Connected to server", flush=True)
        threading.Thread(target=send_messages, args=(sock,), daemon=True).start()
        reader = sock.makefile("r", encoding="utf-8")
        for line in reader:
            message = line.rstrip("\n")
            if message.strip().lower() == "exit":
                break
            print(f"\rServer: {message}")
            print("Client: ", end="", flush=True)
        print("\nDisconnected from server")
    except ConnectionRefusedError:
        print("Could not connect: is the server running?")
    except OSError as e:
        print(f"Socket error: {e}")
    except KeyboardInterrupt:
        print("\nClient stopped")
    finally:
        sock.close()


if __name__ == "__main__":
    main()

