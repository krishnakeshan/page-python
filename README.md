# page-python
Page server built with Python. Page is an application to let you transform your PC/Laptop into a home server.

# Getting Started

To get started, simply clone this repository onto your machine. In a terminal, navigate to the base directory and start the server as shown below:

`$: python3 main.py ip-address port`

where `ip-address` must be the address of the network interface your server should run on. Most commonly, for running the server on your local network, you can run `ipconfig` or `ifconfig` on your terminal to find the IP address corresponding to `en0` or something similar. `port` is the port number you want to run the server on. It can be any integer between 1024 - 65535 and that isn't already being used by another application. The application will exit if it cannot use the provided configuration so you should consider trying it with different configurations.

`ip-address` can also be a public IP address in which case it will be accessible outside of your LAN as well.

# Contributing

**page-python** is well, built in Python and it's the current server implementation of Page. You can contribute to this implementation or create a port in a different language for any reasons you find valid (performance, portability, etc.). The code is well-commented and well-structured so you should be able to understand it quite easily.
