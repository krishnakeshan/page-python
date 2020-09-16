import socket
import sys
import os
import json
from pathlib import Path

from file_explorer import FileExplorer


class APIServer:
    # init API server
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.fileExplorer = FileExplorer()

    # method to start the server and listen for incoming requests
    def startServer(self):
        addr = (self.host, self.port)

        # create socket server and listen for connections
        print(f"server listening on {self.host}:{self.port}")
        self.servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servSock.bind(addr)
        self.servSock.listen(1)
        while True:
            # accept incoming connection
            remoteSock, _ = self.servSock.accept()
            sockIn = remoteSock.makefile(mode="r")
            sockOut = remoteSock.makefile(mode="w")

            # receive message
            reqString = sockIn.readline()[:-1]
            request = json.loads(reqString)

            # handle request
            self.handleRequest(request, remoteSock)

            # close files
            sockIn.close()
            sockOut.close()

        # close server socket after breaking from loop
        self.servSock.close()

    # method to handle requests
    def handleRequest(self, request, remoteSock):
        # create io files
        sockOut = remoteSock.makefile("w")

        # GENERAL
        if request["message"] == "ping":
            response = {"success": True}
            sockOut.write(json.dumps(response))

        elif request["message"] == "getHostInfo":
            response = {"success": True, "name": "Krishna-Mac"}
            sockOut.write(json.dumps(response))

        # FILES
        # current directory name
        elif request["message"] == "getCurrentDirectory":
            response = {
                "success":
                True,
                "cwd":
                self.fileExplorer.getFileRep(
                    self.fileExplorer.currentDirectory),
            }
            sockOut.write(json.dumps(response))

        # current directory contents
        elif request["message"] == "getCurrentDirectoryContents":
            contents = []
            for file in self.fileExplorer.cwdContents():
                contents.append(self.fileExplorer.getFileRep(file))
            response = {"success": True, "contents": contents}
            sockOut.write(json.dumps(response))

        # change current directory
        elif request["message"] == "changeCurrentDirectory":
            # change directory
            destination = request["destinationDirectory"]
            result = self.fileExplorer.down(destination)

            # write response
            response = {
                "success":
                result,
                "cwd":
                self.fileExplorer.getFileRep(
                    self.fileExplorer.currentDirectory),
            }
            sockOut.write(json.dumps(response))

        # go up file hierarchy
        elif request["message"] == "goUp":
            if self.fileExplorer.currentDirectory != Path.home():
                self.fileExplorer.up()

            # write response
            response = {
                "success":
                True,
                "cwd":
                self.fileExplorer.getFileRep(
                    self.fileExplorer.currentDirectory),
            }
            sockOut.write(json.dumps(response))

        # download file
        elif request["message"] == "downloadFile":
            # get arguments
            fileName = request["fileName"]

        # MESSAGING
        elif request["message"] == "sendMessage":
            # sync this message to database
            print(request["payload"])

            # show message
            print(request["payload"])

            # send response
            response = {
                "success": True,
            }
            sockOut.write(json.dumps(response))

        # invalid request
        else:
            response = {"success": False, "message": "Invalid request"}
            sockOut.write(json.dumps(response))

        # close files and socket
        sockOut.close()
        remoteSock.close()
