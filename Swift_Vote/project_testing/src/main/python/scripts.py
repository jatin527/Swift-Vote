import sys
import web3

def function1(out):
    w3 = web3.Web3(web3.HTTPProvider("http://127.0.0.1:8545"))
    print(w3.isConnected())
    out.write(w3.isConnected())

def function2(out):
    print("yo")
    out.write("Hello")