import sys,requests,urllib3
from colorama import Fore,Back

def searchSubdomain(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
    except urllib3.exceptions.LocationParseError:
        pass

def initial():
    if(len(sys.argv) !=2):
        print("[+]-Usage:   python <program.py> <url>")
        exit(-1)
    else:
        printSubdomain()
   

def printSubdomain():

    protocol = 'https://www.'
    url=sys.argv[1]
    with open('/home/mute/Development/Python/Practice/Subdomain.txt','r') as wordlist:
        for sub in wordlist:
            # Strip quito espacios antes y despues. Como cada linea del archivo tiene al final un \n, se lo quito para poder
            # concatenar con url todo en la misma línea
            completeURL =  protocol+sub.strip()+'.'+url
            result=searchSubdomain(completeURL)
            if (result):
                print(Back.WHITE+Fore.BLACK+"[+]-Subdomain found: "+Fore.RESET+Back.RESET+"{}".format(result.url))

if __name__ == '__main__':
    initial()