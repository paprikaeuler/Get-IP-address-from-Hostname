import socket
 
hostname = input("Та дурын домэйн нэр оруулна уу.! :\n")
 
# Хостын нэрнээс IP хаягыг гаргаж авах.

print(f'{hostname} -ын IP хаяг бол {socket.gethostbyname(hostname)}')