same = 0
notbbe = 0
def loadinput(inp):
    f=open(inp, 'r')
    li=[]
    text = f.read()
    li = text.split()
    return li

def makelib(inp):
    li = loadinput(inp)
    d = {}
  
    for w in li:
        w = w.replace('?', '')
        w = w.replace('.', '')
        w = w.replace(',', '')
        w = w.replace('!', '')
        w = w.replace(')', '')
        w = w.replace('(', '')
        w = w.replace('[', '')
        w = w.replace(']', '')
        w = w.replace(':', '')
        w = w.lower()
        
        if w in d:
            d[w] = d[w] + 1;
        else:
            d[w]= 1
    return d

def inbbe(bbe, w):
    for v in bbe:
        if v==w:
            return 1
    return 0


def difference(bbe, d):
    li=[]
    i=0
    n=0
    global same
    global notbbe
    for w in d:
        y = inbbe(bbe, w)
        if y!=1:
            li.append(w)
            n+=1
        if y==1:
            i+=1
                        
    same = i
    notbbe = n
    return li
        

def main():
    global same
    
    f=open('out.txt', 'w')
    bbe=makelib('bbe.txt')
    d=makelib('input.txt')
    wrong=loadinput('badwords.txt')

    for x in d:
        for bword in wrong:
            if x==bword:
                print ('Wrong word on input: ')
                s='Word: ' + str(x) + ' --> ' + str(d[x]) +'\n'
                print s
    
    dif= difference(bbe.keys(), d.keys())

    i=1
    for k in d.values():
       if k > i:
           i = k

    f.write('Difference to BE:\n')
    for v in dif:
        f.write(v)
        f.write('\t')
    f.write('\n')
    f.write('Counted difference word:\t')
    f.write(str(notbbe))
    f.write('\n')
    f.write('BE words:\t')
    f.write(str(same))
 
    f.write('\n')
    f.write('All counted word:\t')
    f.write(str(same + notbbe))
    f.write('\n')
    
    
    while i > 0:
        for k in sorted(d.keys()):
            if d[k] == i:
                s='Word: ' + str(k) + ' --> ' + str(d[k]) +'\n'
                f.write(s)
        i-=1
        
        
if __name__=="__main__":
    main()
       
