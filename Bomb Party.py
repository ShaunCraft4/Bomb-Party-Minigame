import requests
import random
from inputimeout import inputimeout, TimeoutOccurred
import time


words= requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt")
wordlist=words.text.splitlines()
WordList1=[x.upper() for x in wordlist]
WordList=[]
for i in WordList1:
    s=""
    for j in i:
        if j not in ".,<>/?;:\|*&^%$#@!-_+=[]{'}~":
            s+=j
    WordList.append(s)


def Random_letter(WordList):
    RW=random.choice(WordList)
    RI=random.randint(0,len(RW)-3)
    TOT=random.randint(2,3)
    if TOT==2:
        
        Letters=RW[RI]+RW[RI+1]
    else:
        Letters=RW[RI]+RW[RI+1]+RW[RI+2]
    return Letters

def Order(nHearts,timeint,WordList,lHearts,RL,c,index):
    for j in range(index,len(lHearts)):
            i=lHearts[j]
            ntimeint=timeint
            print()
            print()
            try:
                print("Its your turn",i,"!!!")
                print("Your letters are '",RL,"'")
                Catch=True
                while Catch==True:
                    start_time = time.perf_counter()
                    value = inputimeout(prompt="Enter the word: ", timeout=ntimeint)
                    end_time = time.perf_counter()
                    if value.upper() in WordList and RL in value.upper() and value.upper()!=RL:
                        print(random.choice(["Fantastic work","Amazing job","Excellent work","Outstanding work"])+"!!!")
                        Catch=False
                        while True:  
                            RL1=Random_letter(WordList)
                            c2=0
                            for i in RL:
                                if i in RL1:
                                    c2+=1
                            if c2==0:
                                RL=RL1
                                break    
                    else:
                        print("Oh "+random.choice(["No","Sadly","Regretfully","Painfully","Bitterly"])+" that word doesnt work well....Try again!!!")
                        elapsed_time = end_time - start_time
                        ntimeint-=elapsed_time
                    
            except TimeoutOccurred:
                print("Times up!, You couldnt guess a word... You lost a heart!")
                nHearts[i]-=1
                if nHearts[i]==0:
                    print(i,"has lost their lives!!!")
                    nHearts.pop(i)
                    index=lHearts.index(i)
                    if index==len(lHearts):
                        index=0
                    lHearts.remove(i)
                    if len(lHearts)==1:
                        c=1
                    else:
                        L=Order(nHearts,timeint,WordList,lHearts,RL,c,index)
                        if L==1:
                            c=1
                        break
                        
            if c==1:
                global O
                O=1
                break

def Bomb_Party(nHearts,timeint,WordList):
    while True:
        global O
        O=0
        c=0
        RL=Random_letter(WordList)
        lHearts=list(nHearts.keys())
        index=0
        Order(nHearts,timeint,WordList,lHearts,RL,c,index)
        print()
        print("Hearts left after this round:")
        for i in nHearts:
            print(i," : ",nHearts[i])
        time.sleep(5)
        print()
        if O==1:
            print(lHearts[0],"has won the Game!!!")
            break
                
         
print()     
print("Welcome to Bomb Party!!!")
print()
print('''Here are the rules:
      
On a player's turn they must type a word (3 letters or more) containing the given letters in the same order before the bomb explodes 🤯 (example: LU - BLUE).
If a player does not type a word in time, they lose a heart 💀. The last player remaining wins the game 🎉

''')
time.sleep(7)
print()
nHearts={}  
NOP=int(input("Enter number of players: "))
print()
for i in range(1,NOP+1):
    print("Player ",i,":")
    pn=input("Enter name: ")
    print()
    nHearts[pn]=3
timeint=int(input("Enter time limit foreach guess: "))
print()
print("Lets get the party Started!!!")
time.sleep(2)
Bomb_Party(nHearts,timeint,WordList)
