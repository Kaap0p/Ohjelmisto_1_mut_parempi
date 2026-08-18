import socket
import subprocess
from re import Scanner
import socket
from re import Scanner

Welcome = """
       __        __   _                          _ 
       \ \      / /__| | ___ ___  _ __ ___   ___| |
        \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
         \ V  V /  __/ | (_| (_) | | | | | |  __/_|
          \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)
       """
print(Welcome)
function = input("What would you like to do?")
if function.lower() == "scan":
    Port_names = {
        21 : "FTP",
        80 : "HTTP",
        443 : "HTTPS",
        22 : "SSH",
        3389 : "RDP",
        23 : "TELNET"
    }
    for port in Port_names:
        S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        S.settimeout(0.5)

        status = S.connect_ex(("127.0.01", port))

        if status == 0:
            print(f'Port {port} is open')
        else:
            print(f'Port {port} is not open')

function = input("What would you like to do?")
if function == "scan":
    Port_names = {
        21 : "FTP",
        80 : "HTTP",
        443 : "HTTPS",
        22 : "SSH",
        3389 : "RDP",
        23 : "TELNET"
    }
    for port in Port_names:
        S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        S.settimeout(0.5)

        status = S.connect_ex(("127.0.01", port))

        if status == 0:
            print(f'Port {port} is open')
        else:
            print(f'Port {port} is not open')

        S.close()

elif function == "SSH":
    print("\nStarting local SSH-like command executor. ")
    print("Type Exit to quit.")
    print("Extra commands:Banner <ip> <port>\n")


    while True:
        CMD = input("> ")

        if CMD.lower() == "exit":
            print("\nExiting SSH-like command executor.")
            break

        elif CMD.startswith("banner"):
            try:
                _, ip, port = CMD.split(" ")
                S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                S. settimeout(2)

                print(f"connecting to {ip}:{port}  ...")
                s.connect((ip, int(port)))

                banner = S.recv(1024).decode(errors="ignore")
                print("Banner:\n" + banner)

                s.close()
            except exception as e:
                print(f"Error connecting to {ip}:{port}: {e}")
            continue

        output = subprocess.getoutput(CMD)
        print(output)

else:
    print("Unknown command. Pls type 'SSH' or 'Scan'.")
