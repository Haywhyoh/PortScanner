import socket

ip = (input('Enter ip address:'))
port_1 = int(input('Enter lowest port number: '))
port_2 = int(input('Enter the highest port number: '))

m_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for port in range(port_1,port_2):
    location = (ip, port)
    result_of_check = m_soc.connect_ex(location)

    if result_of_check == 0:
        print(port, 'Port is open')
    else:
        print(port, 'port is close')
   
    m_soc.close()