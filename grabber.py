import requests
import sys
import os
from threading import Thread

banner = """
░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
                                                                   
            <<Made by Hades - Reverse IP/Domain>>
                      <<Version v.0>>
"""
print(banner)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}


result_reverse = 'result.txt'


def rev(ip):
    url = f"https://api.hackertarget.com/reverseiplookup/?q={ip}"
    r = requests.get(url, headers=headers).text

    with open(result_reverse, 'a+') as f:
            f.write(r)
            f.write("\n")
    f.close()

if __name__ == '__main__':
    try:
        program_name = sys.argv[0]
        input_ip = sys.argv[1]
        input_thread = int(sys.argv[2])
        ip_file = open(input_ip).read()
        for ip in ip_file.splitlines():
            thread = Thread(target=rev, args=(ip,))
            thread.start()
            thread.join()
    except IndexError:
        print(f"Usage : {program_name} <ip_list.txt> <thread>")
    except FileNotFoundError:
        print(f"file {input_ip} nothing. try again!")
