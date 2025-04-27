# Applied-Network-Protocol-Analysis
 using HTTP/Python to solve a challenge
 # Applied Network Protocol Analysis
How It Works
1. The script sends a POST request to the server at `127.0.0.1:8888` with a payload containing the `magicNumber`.
2. The server responds with feedback indicating whether the PIN is correct or not.
3. The script iterates through all possible 3-digit PINs (000-999) until the correct one is found.

Problems Encountered
Incorrect port and host configuration, which resulted in failure to connect to the server.
Server errors caused by Windows protection, requiring adjustments to the system settings.
Errors in the initial code that prevented the password from being revealed, and all trying Pin are wrong.
The request timing was too fast, causing the server to respond with 'Too fast' message.
The most challenge encountered was resolving server-related issues due to Windows protection measures.
