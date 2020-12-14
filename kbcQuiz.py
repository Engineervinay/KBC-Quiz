class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def skiptheanswer():
    print("in this lifeline you will be provided the correct asnwer")


def fiftyfifty():
    print("in this lifeline you will be provided two options in which one is coreect and other is wrong")
    print("all you have to do is choose your answer from that options only ")

def audiencepoll():
    print("when you call this lifeline you will be displayed the percentage that how much")
    print("audience vote to any answer")


def googlehelp():
    print("in this lifeline you will be given 1 minute of time and you can take help of google to answwer your question")


print(color.BOLD + color.BLUE + "\n\n\n             WELCOME TO KAUN BANEGA CROREPATI BY VINAY PATIL")


def info():
    print(color.BOLD + "\n\nour team welcome you to the famous game by kaun banega crorepati\n")
    print(color.END + "basically this is the non graphical version of kbc just as a project")
    print("so following their are some instruction and tips to play the game")
    print("\n\nSO LET'S START\n\n\n")
    print(color.BLUE + "you will get 13 question in this game every question have its unique price")
    print("as you will pass every question the amount you won will be displayed just after that question" + color.END)
    print(color.BOLD + "you will get 4 lifelines in this game")
    print("you can use these lifelines anytime but one lifeline only once")
    print("\n if you use any lifeline more than one time then you are not able to")
    print("use any lifeline in that question and you have to answer that question without lifeline" + color.END)
    print(color.PURPLE + "\nyou will have following lifelines in this game")
    print(color.RED + "\n1. skip the question")
    print("2. 50-50")
    print("3. expert advice")
    print("4. audience poll" + color.END)
    print("\nif you want to know about any lifeline just enter its number")
    print(
        "\nif you want to exit just answer the question you may win but if you loose you will automatically get out of game")
    h = input()
    if h == '1':
        skiptheanswer()
    elif h == '2':
        fiftyfifty()
    elif h == '3':
        googlehelp()
    elif h == '4':
        audiencepoll()
    else:
        pass


f = open("ques.txt", "r")
a=0
b=6
q=0
lf=4
au=0
ex=0
ff=0
sk=0

win_amount = 0


def win_amt():
    global win_amount
    global answ
    global b
    global a
    if((a==0)and answ=="b"):
        win_amount+=5000
    elif ((a == 12 or a == 54 or a == 48 or a == 72) and answ == "b"):
        win_amount = win_amount*2
        print(color.PURPLE + "amount you won=" + color.END, win_amount)
    elif ((a == 6 or a == 24 or a == 30 or a == 66) and answ == "a"):
        win_amount = win_amount*2
        print(color.PURPLE + "amount you won=" + color.END, win_amount)
    elif ((a == 18 or a == 36) and answ == "c"):
        win_amount = win_amount*2
        print(color.PURPLE + "amount you won=" + color.END, win_amount)
    elif ((a == 42 or a == 60) and answ == "d"):
        win_amount = win_amount*2
        print(color.PURPLE + "amount you won=" + color.END, win_amount)
    else:
        print("total amount you won is ",win_amount)

    return win_amount



def check_answ():
    global a
    global answ
    if ((a==0 or a==12 or a==54 or a==48 or a==72) and answ=="b"):
        print(color.GREEN+"Congrats that was correct\n"+color.END)
        win_amt()
    elif((a==6 or a==24 or a==30 or a==66)and answ=="a"):
        print(color.GREEN+"Congrats that was correct\n"+color.END)
        win_amt()
    elif((a==18 or a==36)and answ=="c"):
        print(color.GREEN+"Congrats that was correct\n"+color.END)
        win_amt()
    elif((a==42 or a==60)and answ=="d"):
        print(color.GREEN+"Congrats that was correct\n"+color.END)
        win_amt()
    else:
        print("sorry that was wrong\n")
        win_amt()
        exit()


import time

def countdown(n):
    while(n>0):
        print(n)
        time.sleep(1)
        n=n-1
    print(color.PURPLE+"times up enter your answer now")


def audiencepoll():
    print("\n\n")
    if (a == 0 or a == 12 or a == 54 or a == 48 or a == 72):
        print(color.BLUE+"audience vote answer a.=23% \n b.=72% \n c.=7% \n d.=3%")
    elif (a == 6 or a == 24 or a == 30 or a == 66):
        print(color.BLUE+"audience vote answer a.=72% \n b.=23% \n c.=7% \n d.=3%")
    elif (a == 18 or a == 36):
        print(color.BLUE+"audience vote answer a.=23% \n b.=7% \n c.=72% \n d.=3%")
    elif (a == 42 or a == 60):
        print(color.BLUE+"audience vote answer a.=23% \n b.=3%% \n c.=7% \n d.=72%")




def fifty():
    if (a == 0 or a == 12 or a == 54 or a == 48 or a == 72):
        print(color.BOLD+"\ntrue answer is in a or b\n")
    elif (a == 6 or a == 24 or a == 30 or a == 66):
        print(color.BOLD+"true answer is in a or b\n")
    elif (a == 18 or a == 36):
        print(color.BOLD+"true answer is in c or d\n")
    elif (a == 42 or a == 60):
        print(color.BOLD+"true answer is in c or d\n")
def skipques():
    if (a == 0 or a == 12 or a == 54 or a == 48 or a == 72):
        print(color.BOLD+"\ntrue answer is b\n")
    elif (a == 6 or a == 24 or a == 30 or a == 66):
        print(color.BOLD+"true answer is a\n")
    elif (a == 18 or a == 36):
        print(color.BOLD+"true answer is c\n")
    elif (a == 42 or a == 60):
        print(color.BOLD+"true answer is d\n")


def expert():
    global a
    if(a == 0 or a == 12 or a == 54 or a == 48 or a == 72):
        print("according to our expert answer is b")
    elif(a == 6 or a == 24 or a == 30 or a == 66):
        print("according to our expert answer is a")
    elif(a == 18 or a == 36):
        print("according to our expert answer is c")
    elif(a == 42 or a == 60):
        print("according to our expert answer is d")


def lifeline():
    print(color.DARKCYAN+"")
    print(color.BOLD+"select the lifeline you want to use")
    print(color.BOLD+"\ndon't use the lifeline you already used\n")
    print(color.BOLD+"\nselct the number of lifeline you want to use\n")
    print(color.DARKCYAN+"            1. audience poll\n")
    print(color.DARKCYAN+"            2. fifty fifty\n")
    print(color.DARKCYAN+"            3. skip the answer\n")
    print(color.DARKCYAN+"            4. expert advice\n")

    l=int(input(color.END+"\nenter the number of that lifeline you want to use"))
    if(l==1):
        global au
        if(au==0):
            au-=1
            audiencepoll()
        else:
            print(color.BOLD+"you already used this lifeline and not allowed to use again")
            print(color.BOLD+"\nnow you are not allowed to take lifeline for this question")
            print(color.BOLD+"you have to answer this question without lifeline")

        return au

    elif(l==2):
        global ff
        if(ff==0):
            ff-=1
            fifty()
        else:
            print(color.BOLD+"\nyou already used this lifeline and not allowed to use again\n")
            print(color.BOLD + "\nnow you are not allowed to take lifeline for this question")
            print(color.BOLD + "you have to answer this question without lifeline")
        return ff
    elif(l==3):
        global sk
        if(sk==0):
            sk-=1
            skipques()
        else:
            print(color.BOLD+"you have already used this lifeline and not allowed to use it again")
        return sk
    elif(l==4):
        global ex
        if(ex==0):
            ex-=1
            expert()
        else:
            print(color.BOLD+"you already used this lifeline and not allowed to use it again")
        return ex


info()
while(q!=13):
    for i in range(a,b):
        print(f.readline())
    answ = input("enter your answer: ")

    #code starting for lifeline

    if(answ=="l"):
        print(color.BLUE+"\nare you sure you want to take lifeline enter l to confirm and if not enter your answer\n\n")
        answ=input()
        if(answ=="l"):
            lf-=1
            print(color.BOLD+"                                  lifeline left after this question=", lf)

            #lifelines left at present time start

            print("                             you have left these life line for this question\n")
            print(" "*15+color.RED+"# # # # # # # # # # # #\n")
            if(au==0):
                print(color.RED+"               #   audience poll     #\n")
            if(sk==0):
                print(color.RED+"               #   skip the answer   #\n")
            if(ff==0):
                print(color.RED+"               #   fifty fifty       #\n")
            if(ex==0):
                print(color.RED+"               #   expert advice     #\n")
            print(" "*15+color.RED+"# # # # # # # # # # # #\n")

            #lifeline left at present time ends

            if (lf > -1 and lf <= 4):
                lifeline()
                answ = input(color.END+"okk now enter your answer")

                if ((a == 0 or a == 12 or a == 54 or a == 48 or a == 72) and answ == "b"):
                    print(color.GREEN+"Congrats that was correct\n"+color.END)
                    win_amt()
                elif ((a == 6 or a == 24 or a == 30 or a == 66) and answ == "a"):
                    print(color.GREEN+"Congrats that was correct\n"+color.END)
                    win_amt()
                elif ((a == 18 or a == 36) and answ == "c"):
                    print(color.GREEN+"Congrats that was correct\n"+color.END)
                    win_amt()
                elif ((a == 42 or a == 60) and answ == "d"):
                    print(color.GREEN+"Congrats that was correct\n"+color.END)
                    win_amt()
                else:
                    print(color.RED+"sorry that was wrong")
                    exit()
                    win_amt()
            else:
                print(color.RED+"sorry you have no lifeline left")
                answ = input("okk now enter your answer")
                if ((a == 0 or a == 12 or a == 54 or a == 48 or a == 72) and answ == "b"):
                    print("Congrats that was correct")
                elif ((a == 6 or a == 24 or a == 30 or a == 66) and answ == "a"):
                    print("Congrats that was correct")
                elif ((a == 18 or a == 36) and answ == "c"):
                    print("Congrats that was correct")
                elif ((a == 42 or a == 60) and answ == "d"):
                    print("Congrats that was correct")
                else:
                    print("sorry that was wrong")
                    exit()
        else:
            check_answ()
    else:
        check_answ()

    #code ends for lifeline

    a=b
    b=b+6
    q=q+1
f.close()


