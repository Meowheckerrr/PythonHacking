from base64 import encode
import hashlib
from hmac import digest

hash_text = input("please input the hash")

wordlist_list = input("input the worlist name")

try:
    file = open("wordlist_list","r")

except:
    print("error")
    quit()


for psWD in file:
    
    psWD = psWD.encode("utf-8")
    digest = hashlib.md5(psWD.strip()).hexditest()

