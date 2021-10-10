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
    if(len(sys.argv) not in range (2,3+1)):
        print("[+]-Usage:   python <program.py> <url> <[optional] dictionary file>")
        exit(-1)
    else:
        printSubdomain()
   

def printSubdomain():

    protocol = 'https://www.'
    url=sys.argv[1]
    defaultDictionary='./Subdomain.txt'
    
    try:
        if(sys.argv[2]):
            defaultDictionary=sys.argv[2]
    except IndexError:
        pass
        
    with open(defaultDictionary,'r') as wordlist:
        for sub in wordlist:
            # Strip quito espacios antes y despues. Como cada linea del archivo tiene al final un \n, se lo quito para poder
            # concatenar con url todo en la misma línea
            completeURL =  protocol+sub.strip()+'.'+url
            result=searchSubdomain(completeURL)
            if (result):
                print(Back.WHITE+Fore.BLACK+"[+]-Subdomain found:"+Fore.RESET+Back.RESET+" {}".format(result.url))

if __name__ == '__main__':
    initial()