import socket

def get_remote_machine_info():
    remote_host = "www.python.org"
    try:
        print "IP address: {0}".format(socket.gethostbyname(remote_host))
    except socket.error, err_msg:
        print "{0}: {1}".format(remote_host, err_msg)

if __name__=="__main__":
    get_remote_machine_info()
