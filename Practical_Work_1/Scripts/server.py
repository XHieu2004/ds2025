import socket

# Server configurations
HOST = '0.0.0.0' 
PORT = 8089   

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server is listening on {HOST}:{PORT}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            
            # Get file information
            file_info = conn.recv(1024).decode()
            filename, filesize = file_info.split(',')
            filesize = int(filesize)
            print(f"Receiving file: {filename} ({filesize} bytes)")
            
            # Get file data
            with open(f"received_{filename}", "wb") as f:
                received = 0
                while received < filesize:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
                    received += len(data)
                    print(f"Received {received}/{filesize} bytes")
            
            print(f"File {filename} received successfully!")

if __name__ == "__main__":
    start_server()
