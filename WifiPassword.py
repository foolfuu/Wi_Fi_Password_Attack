import os
def main():
    os.system('cls')
    while True:
        pa = input('Enter password: ')
        if pa == "erfunfoolfuu":
            os.system('cls')
            input('Welcome')
            break
        else:
            os.system('cls')
            print("no connect!")

    while True:
        os.system('cls')
        os.system('netsh wlan show profiles')
        print('\n\n\n')
        syst = input('Enter Wi_Fi: ')
        #
        d = syst[0]
        cv = d
        d = d.upper()
        for i in syst:
            if i == cv:pass
            else: d += i

        syst = d
        
        #
        os.system('cls')
        os.system('netsh wlan show profile ' + syst + ' key=clear')
        for i in range(2): input('')
        while True:
            os.system('cls')
            print('''

1: remove
2: exit
''')
            fg = input('Enter: ')
            if fg == '1':break
            elif fg == '2':return
            else:
                print('Error')
                input('')
    


main()
