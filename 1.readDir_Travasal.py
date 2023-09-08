import os,hashlib

def listing(_path,_uni):
    fo = open("output" + _uni + ".txt" , "w")
    for cp,ds,fs in os.walk(_path):
        for file in fs:
            tempFile = open(os.path.join(cp,file),'rb')
            tempStr = tempFile.read()
            h = hashlib.sha512()
            h.update(tempStr)
            tempFile.close()
            result = h.hexdigest() + "," + cp + "/" + file + "\n"
            fo.write(result)
    fo.close()
"""
def listCompare(_fileOri,_fileNew):
    fo = open(_fileOri , "r")
    fn = open(_fileNew , "r")
    line = 0
    while True:
        lineO = fo.readline()
        lo = lineO.split(',')
        lineN = fn.readline()
        ln = lineN.split(',')
        if(lo[0] != ln[0]):
            print(lo[1])
        line += 1
        
        if (not lineO) or (not lineN):
            break
"""
def dirCompare(_checkList,_checkList2):
    fo = open(_checkList)
    fn = open(_checkList2)
    dirO = {}
    dirN = {}
    
    while True:
        lineO = fo.readline()
        #break
        if not lineO:
            break
        tempO = lineO.split(',')
        tempNameO = lineO.split('/test1')
        dirO[tempNameO[1]] =  tempO[0]
        
    while True:
        lineN = fn.readline()
        if not lineN:
            break
        tempN = lineN.split(',')
        tempNameN = lineN.split('/test2') 
        dirN[tempNameN[1]] =  tempN[0]
        
    fo.close()
    fn.close()
    
    print("-" * 80)
    
    for key in dirO:
        if key in dirN:
            if dirO[key] != dirN[key]:
                print(key.replace('\n','') + ":不同的雜湊\n |A|" + dirO[key] + "\n |B|" + dirN[key])
            #else:
                #print(dirO[key]+"|"+dirN[key])
        else:
            print(key.replace('\n','') + ":不存在於" + _checkList2 + "紀錄中")
    for key2 in dirN:
        if key2 not in dirO:
            print(key.replace('\n','') + ":不存在於" + _checkList + "紀錄中")

listing("/Users/user/Desktop/ShiaAnLin/test1",'1')
listing("/Users/user/Desktop/ShiaAnLin/test2",'2')#請確認路徑正確
dirCompare("output1.txt","output2.txt")
