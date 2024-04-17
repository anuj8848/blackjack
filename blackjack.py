from random import choice as choosefrom

deck=[2,3,4,5,6,7,8,9,10,10,10,'A']

player={}
dealer={"name":"dealer"}

def check_n_choose_A(checklists):
    for i in range(len(checklists)):
        if checklists[i]=='A':
            get_value_of_A=int(input("choose your value for 'A': "))
            checklists[i]=get_value_of_A

    return checklists
 
def tap_or_hold(player):
    while True:
        get_resonse=input("Tap or Hold (t/h)? ")
        if get_resonse=='t':
            player["cards"].append(choosefrom(deck))
            player["cards"]=check_n_choose_A(player["cards"])
            print(player["cards"])
            if sum(player['cards'])>=21:
                break
        else:
            print(player['cards'])
            break


def results(player,dealer):
    print(str(player["cards"]).center(100))
    print(str(dealer["cards"]).center(100))
    if sum(player["cards"])==21 and sum(dealer['cards']) !=21:
        print("Your won !!!!!!".center(100))
        player['coins']+=1.5*player['bet']
    elif sum(player["cards"])==21 and sum(dealer['cards']) ==21:
        print("Draw!!!!!!".center(100))
    elif sum(player["cards"]) >21:
        print(f"player Brusted!! {player['name']} looses!!!!!!!!1".center(100))
        player['coins']-=player['bet']
    elif sum(player['cards']) >sum(dealer['cards']):
        print("you won!!".center(100))
        player['coins']+=2*player['bet']

    print(f"remaining coins:{player['coins']}".center(100))


def blackjack():
    player['cards']=[]
    dealer['cards']=[]
    get_name=input("enter your name: ")
    player["name"]=get_name
    get_coins=int(input("dollars to buys coins: "))/10
    player['coins']=get_coins
    
    get_bet=int(input("coins to bet: "))
    player["bet"]=get_bet
    
   
    for i in range(2):
        player['cards'].append(choosefrom(deck))
        dealer['cards'].append(choosefrom(deck))

    player["cards"]=check_n_choose_A(player["cards"])

    
    print(player["cards"])
        
    if sum(player["cards"])==21:
        print("BLackjack!!! You won!!!!!") 
    
    else:
        tap_or_hold(player)
        results(player,dealer)
         
while True:
    gamble=input('You want to play BlackJack(y/n)?: ').lower()
    if gamble=='y':
        blackjack()
    else:
        break
       

    
