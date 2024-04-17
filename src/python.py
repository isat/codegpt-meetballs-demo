import time
import random

player1=0
player3=0
player4=0
player5=0
player6=0
player7=0
odd="none"
even="none"
what12="none"
what18="none"
color2="none"
war=2
really=0
over=0

while 1:
    money=1000
    rmoney=10000
    print("what game do you want to play")
    print("for blackjack press 1")
    print("for roulette  press 2")
    if(war!=really):
        print("for Global thermal nuclear war press 3") 
    game=input("")
    if(game=="3"):
        time.sleep(1)
        print("Sorry that scenario is already running")
        time.sleep(1)
        print("how about a nice game of roulette or blackjack?")
        time.sleep(1)
        print("")
        time.sleep(1)
        really=really+1
        continue
    if(game=="lucas"):
        money=10000
        game="1"
        break
    if(game=="crissy"):
        rmoney=100000
        game="2"
        break
    if(game=="1") or (game=="2") or (game=="3"):
        break

def zeros():
    global hit,stop,cards5,ace,dealer9,cards10,stop1,cards11,pblackjack,dblackjack
    hit=0
    stop=0
    cards5=0
    ace=0
    dealer9=0
    cards10=0
    stop1=0
    cards11=0
    pblackjack=0
    dblackjack=0
def card1():
    random.seed()
    n1= random.randint(0,13)
    global cards1
    cards1=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
    (cards1[n1])
    cards1 = cards1[n1]
  
def card2():
    random.seed()
    n2= random.randint(0,13)
    global cards2
    cards2=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
    (cards2[n2])
    cards2 = cards2[n2]  

def card3():
    random.seed()
    n3= random.randint(0,13)
    global cards3
    cards3=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
    (cards3[n3])
    cards3 = cards3[n3] 

def dealer():
    random.seed()
    d1= random.randint(0,13)
    global dealer1
    dealer1=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
    (dealer1[d1])
    dealer1= dealer1[d1]  

def dealer10():
    random.seed()
    d2= random.randint(0,13)
    global dealer2 
    dealer2=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
    (dealer2[d2])
    dealer2= dealer2[d2]

def dealer11():
    random.seed()
    d3= random.randint(0,13)
    global dealer3 
    dealer3=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
    (dealer3[d3])
    dealer3= dealer3[d3]

while 1:
    if(over==1):
        break
    zeros()
    print(f"you have {money}$ to bet ")
    bet=int(input("how much do you want to bet:"))
    if(bet>money):
        print("you dont have enough money to make that bet")
        time.sleep(0.5)
        continue
    money=money-bet
    dealer() 
    time.sleep(0.5) 
    print(f"dealers first card is {dealer1}") 
    dealer10()
    if(dealer2==11):
        dealer4=dealer1+dealer2
        if(dealer4>21):
            dealer2=1
    dealer4=dealer1+dealer2
    if(dealer4==21):
        print("dealer blackjack")
        dblackjack=1
        money=money-bet
        pass

    while 200:
        if(dblackjack==1):
            break
        card1()
        time.sleep(0.5)  
        print(f"your 1st card is {cards1}")


        card2() 
        time.sleep(0.5) 
        print(f"your 2nd card is {cards2}") 
        if(cards2==11):
            print("want 11 or 1")
            ace=int(input(""))
            if(ace==1):
                cards2=1
            else:
                cards2=11
    
        cards4=cards2+cards1
        
        if(cards4==21):
            print(cards4)
            print("blackjack")
            money=money+bet*1.25
            pass
        else:
            print(f"you have {cards4}") 

        if(cards4==21):
            pblackjack=1 
        cards11=cards4
        break
    while 2:
        if(pblackjack==1):
            break 
        if(dblackjack==1):
            break 
        move=input("stand or hit:")
        if(move=="stand" or move=="s"):
            cards5=cards4
            break
        if(move=="hit" or move=="h"):
            card3() 
            time.sleep(0.5) 
            print(f"your card is {cards3}") 
            if(cards3==11):
                print("want 11 or 1")
                ace=int(input(""))
                if(ace==1):
                    cards3=1
                else:
                    cards3=11           
            cards5=cards4+cards3
            cards4=cards5
            print(f"you have {cards5}")
            if(cards5>21):
                print("you bust")
                money=money-bet
                break
            continue
            
    time.sleep(0.6)
    cards4=cards11

    while 3:
        if(stop==1):
            break
        if(stop1==1):
            break
        if(cards5>21):
            break
        if(pblackjack==1):
            break 
        if(dblackjack==1):
            break 
        while 10:
            print(f"dealer has {dealer4}")
            time.sleep(0.5)    
            if(dealer4>=17):
                print("dealer stands")
                if(dealer4>cards5):
                    print("dealer wins")
                    money=money-bet
                    stop=1
                    break
                if(dealer4==cards5):
                    print("dealer push")
                    money=money+bet
                    stop=1
                    break 
                if(dealer4<cards5):
                    print("you won")
                    bet=bet+bet
                    stop=1
                    break
            time.sleep(1)
            break
        while 101:
            if(stop==1):
                break
            time.sleep(0.5)    
            print("dealer hit")
            hit=1   
            dealer11()
            if(dealer3==11):
                dealer4=dealer3+dealer4
                if(dealer4>21):
                    dealer3=1
            dealer5=dealer4+dealer3
            dealer4=dealer5
            print(f"dealer has {dealer5}")
            if(dealer5>21):
                print("dealer bust")
                bet=bet+bet
                stop1=1
                break
            if(dealer5>=17):
                print("dealer stands")
                if(dealer5>cards5):
                    print("dealer wins")
                    money=money-bet
                    stop1=1
                    break
                if(dealer5==cards5):
                    print("dealer push")
                    money=money+bet 
                    stop1=1
                    break
                if(dealer5<cards5):
                    print("you won")
                    bet=bet+bet
                    stop1=1
                    break
                time.sleep(0.5)   
                break               
        
    time.sleep(1)

    money=money+bet
    if(money==0):
        over=1
        print("Game Over")
        print("you have no money left")
        break          
    else:
        print(f"you have {money}$")
    time.sleep(1)
    again=input("do you wish to play another round? (yes or no):")                    
    if(again=="yes") or (again=="y"):
        continue
    else:
        print("see you again next time")
        over=1


    while 1:
        if(game=="2"):

            random.seed()
            n1= random.randint(0,36)

            bet5=0
            bet6=0
            bet10=0
            bet15=0
            bet16=0
            bet18=0
            bet20=0
            bet21=0
            bet22=0
            bet23=0
            
            

            if(n1==1) or (n1==3) or (n1==5) or (n1==7) or (n1==9) or (n1==12) or (n1==14) or (n1==16) or (n1==18) or (n1==19) or (n1==21) or (n1==23) or (n1==25) or (n1==27) or (n1==30) or (n1==32) or (n1==34) or (n1==36):
                color2="red"
            else:
                color2="black"
                

            if(n1==1) or (n1==2) or (n1==3) or (n1==4) or (n1==5) or (n1==6) or (n1==7) or (n1==8) or (n1==9) or (n1==10) or (n1==11) or (n1==12):
                group12="12p"
                pass
            if(n1==13) or (n1==14) or (n1==15) or (n1==16) or (n1==17) or (n1==18) or (n1==19) or (n1==20) or (n1==21) or (n1==22) or(n1==23) or (n1==24):
                group12="12m"
                pass

            if(n1==25) or (n1==26) or (n1==27) or (n1==28) or (n1==29) or (n1==30) or (n1==31) or (n1==32) or (n1==33) or (n1==34) or(n1==35) or (n1==36):
                group12="12d"
                pass

            if(n1==1) or (n1==2) or (n1==3) or (n1==4) or (n1==5) or (n1==6) or (n1==7) or (n1==8) or (n1==9) or (n1==10) or (n1==11) or (n1==12) or (n1==13) or (n1==14) or (n1==15) or (n1==16) or (n1==17) or (n1==18):
                group18="manque"
            else:
                group18="passe"   
                pass

            if(n1%2==0):
                even="even"
            else:
                even="odd"
                pass
            if(rmoney==0):
                break
            print(f"you have {rmoney}$")
            number =input("what number do you want to bet on or none:")  
            while 6:
                try: 
                    number = int(number)
                    print(f"you have {rmoney}$ to bet ")
                    if(rmoney==0):
                        break
                    bet15=int(input(f"how much do you want to bet on {number}:")) 
                    if(bet15>rmoney):
                        print("you dont have enough to make that bet") 
                        continue
                    rmoney=rmoney-bet15  
                    bet16=bet15 
                    break   
                except(ValueError): 
                    try:
                        number = str(number)
                    finally:
                        break 
            print(f"you have {rmoney}$")           
            color1 =(input("red, black or none:"))
            if(color1=="red" or color1=="r"):
                color1="red"
                while 7:    
                    if(rmoney==0):
                        print("sorry you have 0$ cant bet")
                        break
                    print(f"you have {rmoney}$")
                    bet20=int(input("how much do you want to bet on red:"))
                    if(bet20>rmoney):
                        print("you dont have enough to make that bet")
                        continue
                    rmoney=rmoney-bet20    
                    bet21=bet20
                    break
            if(color1=="black" or color1=="b"):
                color1="black"
                while 8:
                    if(rmoney==0):
                        print("sorry you have 0$ cant bet")
                        break
                    print(f"you have {rmoney}$")
                    bet20=int(input("how much do you want to bet on black:"))
                    if(bet20>rmoney):
                        print("you dont have enough to make that bet")
                        continue
                    rmoney=rmoney-bet20 
                    bet21=bet20
                    break
            if(color1=="none" or color1=="n"):
                pass 
            print(f"you have {rmoney}$") 
            odd = (input("odd, even or none:"))
            if(odd=="odd" or odd=="o"):
                odd="odd"
                while 4:
                    if(rmoney==0):
                        print("sorry you have 0$ cant bet")
                        break
                    print(f"you have {rmoney}$")
                    bet5=int(input("how much do you want to bet on odd:"))
                    if(bet5>rmoney):
                        print("you dont have enough to make that bet") 
                        continue
                    rmoney=rmoney-bet5  
                    bet18=bet5
                    break
            if(odd=="even" or odd=="e"):
                odd="even"
                while 5:
                    if(rmoney==0):
                        print("sorry you have 0$ cant bet")
                        break
                    print(f"you have {rmoney}$")
                    bet5=int(input("how much do you want to bet on even:"))
                    if(bet5>rmoney):
                        print("you dont have enough to make that bet")
                        continue
                    rmoney=rmoney-bet5    
                    bet18=bet5
                    break
            if(odd=="none" or odd=="n"):
                pass
            print(f"you have {rmoney}$") 
            what18 = (input("manque, passe or none:"))
            if(what18=="manque" or what18=="m"):
                what18="manque"
                while 9:
                    if(rmoney==0):
                        print("sorry you have 0$ cant bet")
                        break
                    print(f"you have {rmoney}$")
                    bet22=int(input("how much do you want to bet on manque:"))
                    if(bet22>rmoney):
                        print("you dont have enough to make that bet")
                        continue
                    rmoney=rmoney-bet22
                    bet23=bet22
                    break
            if(what18=="passe" or what18=="p"):
                what18="passe"
                while 9:
                    if(rmoney==0):
                        print("sorry you have 0$ cant bet")
                        break
                    print(f"you have {rmoney}$")
                    bet22=int(input("how much do you want to bet on passe:"))
                    if(bet22>rmoney):
                        print("you dont have enough to make that bet")
                        continue
                    rmoney=rmoney-bet22
                    bet23=bet22
                    break  
            if(what18=="none" or what18=="n"):
                pass    
            print(f"you have {rmoney}$") 
            what12=(input("12p, 12m, 12d or none:"))
            if(what12=="12p" or what12=="p"):
                what12="12p"
                while 10:
                    if(rmoney==0):
                        print("sorry you have 0$ cant bet")
                        break 
                    print(f"you have {rmoney}$")   
                    bet6=int(input("how much do you want to bet on 1st 12:"))
                    if(bet6>rmoney):
                        print("you dont have enough to make that bet")
                        continue
                    rmoney=rmoney-bet6
                    bet10=bet6
                    break
            if(what12=="12m" or what12=="m"):
                what12="12m"
                while 10:
                    if(rmoney==0):
                        print("sorry you have 0$ cant bet")
                        break 
                    print(f"you have {rmoney}$")   
                    bet6=int(input("how much do you want to bet on 2nd 12:"))
                    if(bet6>rmoney):
                        print("you dont have enough to make that bet")
                        continue
                    rmoney=rmoney-bet6
                    bet10=bet6
                    break
            if(what12=="12d" or what12=="d"):
                what12="12d"
                while 10:
                    if(rmoney==0):
                        print("sorry you have 0$ cant bet")
                        break 
                    print(f"you have {rmoney}$")   
                    bet6=int(input("how much do you want to bet on last 12:"))
                    if(bet6>rmoney):
                        print("you dont have enough to make that bet")
                        continue
                    rmoney=rmoney-bet6
                    bet10=bet6
                    break
            if(what12=="none" or what12=="n"):
                pass

            while 2:
                if(number==n1):
                    bet16=bet15*35
                    bet16=bet15+bet16
                
                if(color1==color2):
                    bet20=bet21*1
                    bet20=bet21+bet20

                if(what18==group18):
                    bet22=bet23*1
                    bet22=bet23+bet22 

                if(what12==group12):
                    bet10=bet6*3
                    bet10=bet6+bet10

                if(even==odd):
                    bet18=bet5*1
                    bet18=bet5+bet18
                
                break    

            print("the wheel is spinning...")
            time.sleep(5)


            print("it landed on")



            if(n1==1) or (n1==3) or (n1==5) or (n1==7) or (n1==9) or (n1==12) or (n1==14) or (n1==16) or (n1==18) or (n1==19) or (n1==21) or (n1==23) or (n1==25) or (n1==27) or (n1==30) or (n1==32) or (n1==34) or (n1==36):
                color2="red"
                print(f"{color2}")
            else:
                color2="black"
                print(f"{color2}")  

            print(f"{n1}") 

            if(n1%2==0):
                even="even"
                print(f"{even}")
            else:
                even="odd" 
                print(f"{even}")   
                pass

            if(n1==1) or (n1==2) or (n1==3) or (n1==4) or (n1==5) or (n1==6) or (n1==7) or (n1==8) or (n1==9) or (n1==10) or (n1==11) or (n1==12):
                group12="12p"
                print(f"{group12}") 
                pass
            if(n1==13) or (n1==14) or (n1==15) or (n1==16) or (n1==17) or (n1==18) or (n1==19) or (n1==20) or (n1==21) or (n1==22) or(n1==23) or (n1==24):
                group12="12m"
                print(f"{group12}") 
                pass

            if(n1==25) or (n1==26) or (n1==27) or (n1==28) or (n1==29) or (n1==30) or (n1==31) or (n1==32) or (n1==33) or (n1==34) or(n1==35) or (n1==36):
                group12="12d"
                print(f"{group12}") 
                pass

            if(n1==1) or (n1==2) or (n1==3) or (n1==4) or (n1==5) or (n1==6) or (n1==7) or (n1==8) or (n1==9) or (n1==10) or (n1==11) or (n1==12) or (n1==13) or (n1==14) or (n1==15) or (n1==16) or (n1==17) or (n1==18):
                group18="manque"
                print(f"{group18}")
            else:
                group18="passe"
                print(f"{group18}") 



            if(n1!=number):
                bet16=0

            if(even!=odd):
                bet18=0

            if(color1!=color2):
                bet20=0

            if(what12!=group12):
                bet10=0

            if(what18!=group18):
                bet22=0    


            totalwinnings=bet16+bet20+bet18+bet10+bet22
            rmoney=rmoney+totalwinnings

            print(f"in total you won {totalwinnings}$ ")

            print(f"you have {rmoney}$")
            if(rmoney==0):
                print("GAME OVER")
                print("you ran out of money")
                break
            again=input("do you wish to play again?:")
            if(again=="yes") or (again=="y"):
                continue
            else:
                print("see you next time")
                break

        if(over==0):        
            time.sleep(0.5)                    
            again=input("do you wish to play another round? (yes or no):")                    
            if(again=="yes") or (again=="y"):
                continue
            else:
                print("see you again next time")
                break
        if(over==1):
            break        