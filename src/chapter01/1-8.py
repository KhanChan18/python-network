import sys
import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description="Socket Error Example")
    parser.add_argument("--host", action="store", dest="host", required=False)
    parser.add_argument("--port", action="store", dest="port", type=int, required=False)
    parser.add_argument("--file", action="store", dest="file", required=False)
    
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Error creating socket: {0}".format(e)
        sys.exit(1)
        
    try:
        s.connect((host, port))
    except socket.gaierror, e:
        print "Address-related error connecting to server: {0}".format(e)
        sys.exit(1)
    except socket.error, e:
        print "Connection error: {0}".format(e)
        sys.exit(1)
        
    try:
        s.sendall("GET {0} HTTP/1.0\r\n\r\n".format(filename))
    except socket.error, e:
        print "Error sending data: {0}".format(e)
        sys.exit(1)     
        
    while True:
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print "Error receiving data: {0}".format(e)
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf)
        
if __name__ == "__main__":
    main()