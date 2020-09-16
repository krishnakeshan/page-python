import sys

import api_server

host = sys.argv[1]
port = int(sys.argv[2])

apiServer = api_server.APIServer(host, port)
apiServer.startServer()