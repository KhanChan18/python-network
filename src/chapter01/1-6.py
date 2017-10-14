import socket

def convert_integer():
    data = 1234
    print "Original: {0} => Long host byte order: {1}, Network byte order: {2}".format(
                                                                            data,
                                                                            socket.ntohl(data),
                                                                            socket.htonl(data)
                                                                            )
    
    print "Original: {0} => Long host byte order: {1}, Network byte order: {2}".format(
                                                                            data,
                                                                            socket.ntohs(data),
                                                                            socket.htons(data)
                                                                            )
if __name__ == "__main__":
    convert_integer()