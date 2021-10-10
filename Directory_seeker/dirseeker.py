import sys,requests,urllib3
from colorama import Fore,Back


def searchDirectory(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
    except urllib3.exceptions.LocationParseError:
        pass

def printDirectory():
    
    defaultWordlist='./common.txt'
    protocol='https://www.'
    url=sys.argv[1]
    completeURL=protocol+url
    try:
        if(sys.argv[2]):
            defaultWordlist=sys.argv[2]
    except IndexError:
        pass
    
    with open(defaultWordlist,'r')as wordlist:
        for dir in wordlist:
            
            result = searchDirectory(completeURL+"/"+dir.strip())
            if(result):
                print(Back.WHITE+Fore.BLACK+"[+]--Directory Found:"+Back.RESET+Fore.RESET+" {}".format(result.url))
            


def initial():
    if(len(sys.argv) not in range (2,3+1)):
        print(Back.WHITE+Fore.RED+"[+]-usage--> python <program> <url> <[OPTIONAL] directory wordlist"+Back.RESET+Fore.RESET)
    else:
        printDirectory()


if __name__ == '__main__':
    initial()