import socket
import sys

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "Old sock state: {0}".format(old_state)
    
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "New sock state: {0}".format(new_state)
    
    local_port = 8282
    
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(srv.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR))
    srv.bind(('', local_port))
    srv.listen(1)
    print "Listening on port: {0}".format(local_port)
    
    while True:
        try:
            connection, addr = srv.accept()
            print "Connected by {0}:{1}".format(addr[0], addr[1])
        except KeyboardInterrupt:
            break
        except socket.error, err:
            print "{0}".format(err)
            
if __name__=="__main__":
    ## Test failed and want to know the reason
    reuse_socket_addr()
    
    
    