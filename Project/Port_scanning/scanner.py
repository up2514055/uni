import socket

target = input("Enter the target IP address: ")
start = int(input("Start Port: "))
end = int(input("End Port: "))

open_ports = []
closed_ports = []

for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)#this set this to 0.5 seconds to wait for a reply or we may get stuck on closed port

    if s.connect_ex((target, port)) == 0:
        print(f"Port {port} is Open")
        open_ports.append(port)
    else:
        print(f"Port {port} is closed")
        closed_ports.append(port)

    s.close()

    
print("Summary")

print(f"Num of open ports were {len(open_ports)}")
print(f"Open ports: {open_ports}")
print("****************************")
print(f"Num of closed ports were {len(closed_ports)}")
print(f"Closed ports:{(closed_ports)}")
    

   
