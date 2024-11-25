import socket
import os

# Client configurations
HOST = '0.0.0.0'  
PORT = 8089       

def send_file(filepath):
    filesize = os.path.getsize(filepath)
    filename = os.path.basename(filepath)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server {HOST}:{PORT}")
        
        # Send file information
        file_info = f"{filename},{filesize}"
        client_socket.sendall(file_info.encode())
        
        # Send file data
        with open(filepath, "rb") as f:
            sent = 0
            while (chunk := f.read(1024)):
                client_socket.sendall(chunk)
                sent += len(chunk)
                print(f"Sent {sent}/{filesize} bytes")
        
        print(f"File {filename} sent successfully!")

if __name__ == "__main__":
    filepath = input("Enter path of your file: ")
    if os.path.exists(filepath):
        send_file(filepath)
    else:
        print("File does not exist!")
