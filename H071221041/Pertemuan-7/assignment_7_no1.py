import re

try:
    string_s=input('masukkan string s: ')
    print(len(string_s))
    if len(string_s)==45:
        cocok=re.search("[2468a-zA-Z]{40}[13579 ]{5}", string_s)
        if cocok:
            print('true')
        else:
            print('false')
    else:
        print('false')
except:
    print('false')