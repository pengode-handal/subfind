
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
  parser.add_argument('-l', '--list', metavar='List File Name', help='SUBDOMAIN FINDER MASS SCAN')
  parser.add_argument("-s", "--save", help="input the filename")
  parser.add_argument("-v", "--version", action="version", version="SubDomain Scanner Tool V1.1.0")
  args = parser.parse_args()
  
  def ngk():
    print("[+] Ya udh kalo ga mau di simpen")
  
  pika = ("")
  nma = ("")
  
  def logger(pika):
    file = open(str(nma) + ".txt", "a")
    file.write(str(pika))
    file.write("\n")    
    file.close()
    
    
 
  if args.domain:
    nma = args.save
    logger(pika)
    
    data = args.domain
    api = "https://sonar.omnisint.io/subdomains/" + data
    mulai = time.time()
    pika = requests.get(api).json()
    print("##########{}RESULT{}{}###########".format(b, n, m))
    for i in pika:
      print(h + i)
      logger(i)
    stop = time.time()
    be = int(stop - mulai)
    print("\n{}butuh waktu {} detik untuk selesai".format(k, be))
    sistem("rm -rf None.txt")
  
  if args.list:
      nma = args.save
      logger(pika)
      
      def getUrl(url):
          urls = []
          with open(url, "r") as ufile:
              allurl = ufile.readlines()
              for i in range(len(allurl)):
                  urls.append(allurl[i].strip('\n'))
              return urls 
      file = getUrl(args.list)
      print("##########{}RESULT{}{}###########".format(b, n, m))
      for lists in file:
        api = "https://sonar.omnisint.io/subdomains/" + lists
        mulai = time.time()
        pika = requests.get(api).json()
        for i in pika:
          print(b +"["+lists+"]:\n\n"+h+ i)
          logger(i)
        stop = time.time()
        be = int(stop - mulai)
      print("\n{}butuh waktu {} detik untuk selesai".format(k, be))
      sistem("rm -rf None.txt")
if __name__ == '__main__':
  main()
