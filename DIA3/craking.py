import zipfile

def extract_file(zfile, password):
    try:
        zfile.extractall(pwd=passw.encode('uft-8'))
        return password
    except Exception as error:
        print(error)

def main():
    zfile = zipfile.ZipFile('CARTA COMPROMISO.zip')
    dictionary_file = open('dictionary.txt')
    
    for line in dictionary_file.readlines():
        password = line.strip('\n')
        guess = extract_file(zfile=zfile, password=password)
        
        if guess: 
            print(f'[+] password {password} \n')
            exit(0)
            
if __name__== '__main__':
    main()


