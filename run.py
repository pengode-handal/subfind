
import json
import requests
import time
import os 
from os import system as sistem
import argparse
from argparse import *
from requests import *
sistem("clear")
m='\033[31;1m'
h='\033[32;1m'
k='\033[33;1m'
p='\033[37;1m'
b='\033[34;1m'
n='\033[00;1m'
bg='\033[47;1m'

print("""\n\n
      {}    ╔═══╗  ╔╗ ╔═══╗         {}{}{}Gura chan{}{}
          ║╔═╗║  ║║ ╚╗╔╗║           
          ║╚══╦╗╔╣╚═╗║║║╠══╦╗╔╦══╦╦══╗
          ╚══╗║║║║╔╗║║║║║╔╗║╚╝║╔╗╠╣╔╗║
          ║╚═╝║╚╝║╚╝╠╝╚╝║╚╝║║║║╔╗║║║║║
          ╚═══╩══╩══╩═══╩══╩╩╩╩╝╚╩╩╝╚╝
{}{}==================Information=================
||Tools     : SubDomain Finder              ||
||Author    : Babwa/Guraa-chan              ||
||help      : CLI Python3 System            ||
==================Information=================\n\n """.format(b, n, b, bg, n, b, n, m))

def main():
  
  parser = ArgumentParser()
  parser.add_argument("-d", "--domain", help="domain (dont use http/https)")
  parser.add_argument("-s", "--save", help="input the filename")
  parser.add_argument("-v", "--version", action="version", version="SubDomain Scanner Tool V1.1.0")
  args = parser.parse_args()
  
  def ngk():
    print("[+] Ya udh kalo ga mau di simpen")
  
  pika = ("##########RESULT###########")
  nma = ("")
  
  def logger(pika):
    file = open(str(nma) + ".txt", "a")
    file.write(str(pika))
    file.write("\n")    
    file.close()
    
    
 
  
  nma = args.save
  logger(pika)
    
  data = args.domain
  api = "https://sonar.omnisint.io/subdomains/" + data
  mulai = time.time()
  pika = requests.get(api).json()
  logger(pika)
  print("##########{}RESULT{}{}###########".format(b, n, m))
  for i in pika:
    print(h + i)
  stop = time.time()
  be = int(stop - mulai)
  print("\n{}butuh waktu {} detik untuk selesai".format(k, be))
  sistem("rm -rf None.txt")
  
if __name__ == '__main__':
  main()
