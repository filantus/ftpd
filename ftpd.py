#!/usr/bin/env python
from os import environ
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    PORT = int(environ['FTP_PORT']) if 'FTP_PORT' in environ else 21
    MIN_PORT = 40000
    MAX_PORT = 65535
    ROOT = environ['FTP_ROOT'] if 'FTP_ROOT' in environ else '/var/ftp'

    if 'PASV_PORTS' in environ:
        ports = [int(p) for p in environ['PASV_PORTS'].split('-')]
        MIN_PORT, MAX_PORT = ports[0], ports[1]

    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user(environ['FTP_USER'],
                        environ['FTP_PASS'],
                        ROOT, perm='elradfmwM')

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    if 'PASV_ADDRESS' in environ:
        handler.masquerade_address = environ['PASV_ADDRESS']

    handler.passive_ports = range(MIN_PORT, MAX_PORT)

    # Instantiate FTP server class and listen on 0.0.0.0:21
    address = ('', PORT)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()