import base64
import locale
import sys

"""
def encoder(content):
    print('編碼類型：{:10}|{}'.format('default',content.encode()))
    print('編碼類型：{:10}|{}'.format('UTF-8',content.encode(encoding='utf8')))
    print('編碼類型：{:10}|{}'.format('UTF-16',content.encode(encoding='utf16')))
    print('編碼類型：{:10}|{}'.format('UTF-32',content.encode(encoding='utf32')))
    print('編碼類型：{:10}|{}'.format('cp950',content.encode(encoding='cp950')))
"""
"""
def encoder(content):
    

    enc = ['utf8','utf32','cp950']
    for _ in enc:
        print('編碼類型：{:10}|{}'.format(_,content.encode(encoding = _)))
"""

"""
def decoder(content):
    
    enc = ['base64','utf8','utf32','cp950']
    cypher = []
    for _ in enc:
        if(_ == 'base64'):
            cypher.append(base64.b64encode(content.encode()))
            print('編碼類型：{:10}|{}'.format(_,base64.b64encode(content.encode())))
            
        else:
            cypher.append(content.encode(encoding = _))
            print('編碼類型：{:10}|{}'.format(_,content.encode(encoding = _)))

    print("-"*60)
    index = 0
    for _ in enc:
        if(_ == 'base64'):
            cypher.append(base64.b64encode(content.encode()))
            print('編碼類型：{:10}|{}'.format(_,base64.b64decode(cypher[index]).decode()))
        
        else:
            print('解碼類型：{:10}|{}'.format(_,cypher[index].decode(encoding = _)))

        index +=1
"""
def bash64Decoder(url):
    content = base64.b64decode(url)
    print(content)
    with open('a.png','wb') as f:
        f.write(content)
    
    #content.decode('utf-8')
    #print(content)
    
#print(sys.getfilesystemencoding())
#print(locale.getpreferredencoding())
url = "Oz4rPj0+LDovPiwsKDAtOw=="
bash64Decoder(url)
