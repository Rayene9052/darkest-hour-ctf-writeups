import socket

HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = 1337       # The port players will connect to using nc

def handle_client(conn):
    conn.sendall(b"Enter your coordinates:\n")
    
    conn.sendall(b"Enter x: ")
    x = conn.recv(1024).decode().strip()
    if not x.isnumeric():
        conn.sendall(b"Invalid input. Please enter a number.\n")
        conn.close()
        return
    x = float(x)
    conn.sendall(b"Enter y: ")
    y = conn.recv(1024).decode().strip()
    if not y.isnumeric():
        conn.sendall(b"Invalid input. Please enter a number.\n")
        conn.close()
        return
    y = float(y)

    conn.sendall(b"Enter your crush's coordinates:\n")
    
    while True:
        conn.sendall(b"Enter x: ")
        xx = conn.recv(1024).decode().strip()
        if not xx.isnumeric():
            conn.sendall(b"Invalid input. Please enter a number.\n")
            conn.close()
            return
        xx = float(xx)
        conn.sendall(b"Enter y: ")
        yy = conn.recv(1024).decode().strip()
        if not yy.isnumeric():
            conn.sendall(b"Invalid input. Please enter a number.\n")
            conn.close()
            return
        yy = float(yy)

        if xx != x or yy != y:
            break
        conn.sendall(b"You and your crush are definitely not at the same place rn. Try again.\n")

    def is_point_in_heart(x, y):
        value = ((x**2)/4 + (y**2)/4 - 1)**3 - (x**2 * y**3/9)
        return value <= 0

    your_state = is_point_in_heart(x, y)
    crush_state = is_point_in_heart(xx, yy)

    if your_state and crush_state:
        conn.sendall(b"\n")
        conn.sendall(b"\n")
        conn.sendall(b"True Love! You are both deeply in love!\n")
        love(conn)
    elif your_state or crush_state:
        conn.sendall(b"Unrequited love. One is in love, but the other is not interested.\n")
        exit()
    else:
        conn.sendall(b"No sparks at all.  Time to move on!\n")
        exit()

    conn.close()

def con(x):
    return *******************

def love(conn):

    conn.sendall(b"Now that we know there's potential, let's link your hearts together.\n")
    conn.sendall(b"Your crush left a secret message: I love you 3000\n")
    conn.sendall(b"I have a trick that can help you: MAKE A HEART ONE-DIMENSIONAL and use your mathematics.\n")
    conn.sendall(b"If that's not helping, I'll walk you through it.\n")
    conn.sendall(b"The code you need is the depth of your crush's hint.\n")

    conn.sendall(b"Keep Clicking Enter\n")
    conn.sendall(b"\n")
    i = 0
    while True:
        conn.sendall(b"Did you guess the code yet? send your attempt\n")
        conn.recv(1024).decode().strip()
        conn.sendall(f"Love Counter: {i}\n".encode())
        conn.sendall(f"Love Depth: {con(i)}\n".encode())
        
        i += 1

def start_server():
    with socket.create_server((HOST, PORT)) as server:
        print(f"Server started on port {PORT}. Waiting for connections...")
        while True:
            conn, addr = server.accept()
            print(f"Connection from {addr}")
            handle_client(conn)

if __name__ == "__main__":
    start_server()
