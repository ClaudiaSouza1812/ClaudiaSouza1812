import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object

server_socket.bind(('localhost', 5000)) # bind to the address and port

server_socket.listen(5) # listen for incoming connections
print('Server is listening on port 5000')

while True:
    client_socket, address = server_socket.accept() # accept a connection
    print(f'Connection from {address} has been established!')
    client_socket.send('Welcome to the server!'.encode('utf-8')) # send a message to the client
    client_socket.close() # close the connection


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object

client_socket.connect(('localhost', 5000)) # connect to the server

data = client_socket.recv(1024) # receive data from the server

print(data.decode('utf-8')) # print the data

client_socket.close() # close the connection

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object

server_socket.bind(('localhost', 5000)) # bind to the address and port

server_socket.listen(5) # listen for incoming connections
print('Server is listening on port 5000')

while True:
    client_socket, address = server_socket.accept() # accept a connection
    print(f'Connection from {address} has been established!')
    client_socket.send('Welcome to the server!'.encode('utf-8')) # send a message to the client
    client_socket.close() # close the connection


# example of osi model (open systems interconnection model):
# application layer - HTTP, FTP, SMTP, DNS - human-computer interaction where application can access network services
# presentation layer - encryption, compression, translation - ensures that data is in a usable format and is where data is encrypted and decrypted
# session layer - establishes, maintains, and terminates connections - maintains the connection between the two systems, responsible for controlling ports and sessions
# transport layer - TCP, UDP - transmits data using transmission control protocol or user datagram protocol, responsible for error checking and recovery, including TCP and UDP
# network layer - IP, ICMP, ARP - decides which physical path the data should take based on the network conditions, and is responsible for routing
# data link layer - Ethernet, Wi-Fi, PPP - ensures that data is sent and received correctly, and is responsible for error detection and correction, define the format of the data on the network
# physical layer - cables, hubs, repeaters - transmits raw bit streams over a physical medium, and is responsible for the physical connection between the devices


# example of tcp/ip model (transmission control protocol/internet protocol model):
# application layer - HTTP, FTP, SMTP, DNS - human-computer interaction where application can access network services
# transport
# network
# link
# physical

import socket

hostname = 'www.google.com'

ip_address = socket.gethostbyname(hostname)
print(f'The IP address of {hostname} is {ip_address}')


# DNS (domain name system) is a hierarchical and decentralized naming system for computers, services, or other resources connected to the internet or a private network.
# It associates various information with domain names assigned to each of the participating entities. Most prominently, it translates more readily memorized domain
# names to the numerical IP addresses needed for locating and identifying computer services and devices with the underlying network protocols.
# By providing a worldwide, distributed directory service, the Domain Name System has been an essential component of the functionality of the internet since 1985.

# example of a domain name: www.google.com
# example of an IP address:
import socket

ip_address = socket.gethostbyname('www.google.com')
print(f'IP address of www.google.com is {ip_address}')

# DNS hierarchy:
# root domain - the root domain is the highest level of the DNS hierarchy and is the first step in translating human-readable domain names into IP addresses
# top-level domain - the top-level domain is the highest level of the DNS hierarchy and is the last part of a domain name and is the part that is directly under the root domain
# second-level domain - the second-level domain is the second part of a domain name and is the part that is directly under the top-level domain
# subdomain - a subdomain is a domain that is part of a larger domain and is the part that is directly under the second-level domain
# hostname - a hostname is a label that is assigned to a device connected to a computer network and is used to identify the device on the network
# fully qualified domain name - a fully qualified domain name is a domain name that specifies the exact location of a device on the internet and is the combination of the hostname and the domain name

# example of hierarchy root domain: .
# example of hierarchy top-level domain: .com, .org, .net, .gov, .edu - the highest level of the DNS hierarchy and is the last part of a domain name and is the part that is directly under the root domain
# example of hierarchy second-level domain: google.com, yahoo.com, microsoft.com - the second part of a domain name and is the part that is directly under the top-level domain
# example of hierarchy subdomain: mail.google.com, news.google.com, maps.google.com - a domain that is part of a larger domain and is the part that is directly under the second-level domain
# example of hierarchy hostname: www.google.com, mail.google.com, news.google.com, maps.google.com - a label that is assigned to a device connected to a computer network and is used to identify the device on the network
# example of hierarchy fully qualified domain name: www.google.com, mail.google.com, news.google.com, maps.google.com - a domain name that specifies the exact location of a device on the internet and is the combination of the hostname and the domain name

import socket

host = '192.168.31.205'
port_list = [21, 22, 23, 80, 443, 8080]

for port in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    service_name = "unknown"
    try:
        s.connect((host, port))
        service_name = socket.getservbyport(port)
        print(f'Port {port} is open')
    except:
        print(f'Port {port} is closed')

    s.close()


# example of a simple web server using the http.server module:
import requests

response = requests.get('https://www.google.com')
print(response.text)


# example of a simple web server using the http.server module:
import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

http = socketserver.TCPServer(("", PORT), Handler)

print(f"Server is running on port {PORT}")
http.serve_forever()


# example of a simple web server using the http.server module:
import requests

resp = requests.get('https://localhost:8080/data.json')
print(resp.text)



