import socket

def find_service_name():
    protocolname = "tcp"
    for port in [80, 25]:
        print "Port: {0} => service name: {1}".format(
                                    port,
                                    socket.getservbyport(port, protocolname)
                                    )
        print "Port: {0}  => service name: {1}".format(
                                    53,
                                    socket.getservbyport(53, 'udp')
                )

if __name__ == "__main__":
    find_service_name()
