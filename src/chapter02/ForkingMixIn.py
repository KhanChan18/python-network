import os
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'

class ForkingClient():
    """
    A client to test forking server...
    """
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def run(self):
        """
        Client playing with the server
        """
        current_process_id = os.getpid()
        print "Client: PID %s Sending echo message to the server: '%s'" % (current_process_id, ECHO_MSG)
        send_data_length = self.sock.send(ECHO_MSG)
        print "Client: Send: %d characters, so far..." % send_data_length

        response = self.sock.recv(BUF_SIZE)
        print "Client: PID %s received: %s" % (current_process_id, response[5:])

    def shutdown(self):
        """
        Cleanup the client socket.
        """
        self.sock.close()

class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        """
        Send the echo back to the client.
        """
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getpid()
        response = "%s: %s" % (current_process_id, data)
        print "             Server: Server sending response [current_process_id: data] = [%s]" % response
        self.request.send(response)
        return

class ForkingServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    """
    Nothing to add here, just inherited
    """
    pass

def main():
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    print "                 Server: Server loop running PID: %s" % os.getpid()

    clientPool = [ForkingClient(ip, port) for i in range(10)]
    for client in clientPool:
        client.run()

    server.shutdown()
    for client in clientPool:
        client.shutdown()
    server.socket.close()

if __name__=="__main__":
    main()
