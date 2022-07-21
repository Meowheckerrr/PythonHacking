

hexFilter="".join([(len(repr(chr(i)))==3) and chr(i) or '.' for i in range(256)])
# list comprehension  if chr(i) string length =3 true get ch(i) false replace with '.' declare i in 0~255

def haxdump(src,length =16,show =True): 
    if isinstance(src, bytes):
        src=src.decode()
        results =list()
        for i in range(0, len(src), length):
            word = str(src[i:i+length])

            printable=word.translate(hexFilter)
            hexa=''.join(f'{ord(c):02X}' for c in word)
            hexwidth =length*3
            results.append(f'{i:04x}{hexa:<{hexwidth}} {printable}')


            if show:
                for line in results:
                    print(line)
            else:
                return results
            
            def receiveForm(connection):
                buffer=b''
                connection.settimeout()
            


        
