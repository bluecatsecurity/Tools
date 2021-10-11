import sys,requests,re
from colorama import Fore,Back


def linksExplorer(url):
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    res= requests.get(url)
    #link = re.search(r'href=[\'"]?(\'">]+)',res.text)
    return re.findall('(?:href=")(.*?)"',res.text)
   

def printExplorer():
   
    url = 'http://'+sys.argv[1] 
    links_Found = linksExplorer(url)
    unique_links=[]
     
    if(len(sys.argv) == 3 and sys.argv[2]=='full'):
        for link in links_Found:
            # Si encuentra un relative path lo convierte a absoulte path
            link = requests.compat.urljoin(url,link)

            # Si encuentro un hashtag, le quito lo que venga luego, porque lo que me interesa esa la url y el directorio
            # que sea único
            if('#' in link):
                link = link.split('#')[0]
            print(Back.WHITE+Fore.BLACK+"LINK ENCONTRADO:"+Back.RESET+Fore.RESET+" {}".format(link))
            links_Found = linksExplorer(link)

    elif(len(sys.argv)==2):

        for link in links_Found:
            # Si encuentra un relative path lo convierte a absoulte path
            link = requests.compat.urljoin(url,link)
            
            if('#' in link):
                link = link.split('#')[0]
            
            #   Con ésto me aseguro que traiga directorios del dominio y no 3rd parties y no traiga directorios repetidos
            if(url[12:] in link and link not in unique_links):
                unique_links.append(link)
                #print(Back.WHITE+Fore.BLACK+"LINK ENCONTRADO:"+Back.RESET+Fore.RESET+" {}".format(link))
                links_Found = linksExplorer(link)
                
                
                
    if(unique_links):
        for link in unique_links:
            print(Back.WHITE+Fore.BLACK+"LINK ENCONTRADO:"+Back.RESET+Fore.RESET+" {}".format(link))

def initial():
    if(len(sys.argv) not in range (2,3+1)):
        print("[+]Usage--> python <program> <url> <[OPTIONAL] full")
        exit(-1)

    printExplorer()

if __name__ == '__main__':
    initial()