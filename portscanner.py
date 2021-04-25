import socket
import sys
import time

target = sys.argv[1]

lista = [80, 8080, 8083, 8380, 443, 20, 21, 22, 3306]

print("""


██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                  
by Mardok Security - Developer & Information Security Student

Twitter: @MardokSecurity
YouTube: Mardok Security
GitHub: @MardokSecurity

""")

print("Scanning target...")
time.sleep(3)
print("Target IP: " + socket.gethostbyname(target))
print("Target: " + socket.getfqdn(target))
print("\n")
print("Listando ports...")
time.sleep(3)

for door in lista:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection = sock.connect_ex((target, door))
    if (connection == 0):
        print(door, "OPEN")
