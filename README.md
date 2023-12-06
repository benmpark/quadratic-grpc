# Quadratic Equation gRPC Server & Client

## Overview
This repository contains the necessary files to run a server and client capable of communicating with each other to solve a [quadratic equation](https://en.wikipedia.org/wiki/Quadratic_equation). The code is written in Python (but either the server or the client could communicate with a version of the other coded correctly in a different language, of course). The client asks the user for the three real coefficients **a**, **b**, and **c** and then sends those to the server, which crunches the numbers and returns the correct solution (formatted depending on whether the answers are real or imaginary (or complex) a basic banking application with various (simulated) functions (i.e., you cannot use this program to actually add money to your real bank account!). The main menu, which lists the actions that the user can perform, is detailed below. This application was created as part of a final project for a Foundations of Program class at Merrimack College (CSC6003).

## Installation and Running the Programs
Aside from having [Python](https://www.python.org/downloads/) installed on your machine, you will need the `grpcio` and `grpcio-tools` packages installed, too. Next you should run (with Python) **quadratic_server.py**; a message confirming that the server has been started and is listening will be displayed. Then, *in a separate window*, run **quadratic_client.py**. You'll be prompted for the coefficients, after which there will be a message that the client is communicating with the server. If the communication succeeds, your solution(s) will be returned.

## Documentation
A folder with documentation for the server and client is included with the files in this repository, and PyDocs can be generating from the source code itself, too.

## License
MIT License

Copyright (c) 2023 Benjamin Park

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

