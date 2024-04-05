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
    get_resonse=input("Tap or Hold (t/h)? ")
    if get_resonse=='t':
        player["cards"].append(choosefrom(deck))
        player["cards"]=check_n_choose_A(player["cards"])

def results(player,dealer):
    if sum(player["cards"])==21 and sum(dealer['cards']) !=21:
        print("Your won !!!!!!")
        player['coins']=1.5*player['coins']
    elif sum(player["cards"])==21 and sum(dealer['cards']) ==21:
        print("Draw!!!!!!")
    elif sum(player["cards"]) >21:
        print(f"player Brusted!! {player['name']} looses!!!!!!!!1")
        player['coins']-=player['bet']
    elif sum(player['cards']) >sum(dealer['cards']):
        print("you won!!")
        player['coins']=2*player['coins']

    print(f"remaining coins:{player['coins']}")


def blackjack():
    player['cards']=[]
    dealer['cards']=[]
    get_name=input("enter your name: ")
    player["name"]=get_name
    get_coins=int(input("dollars to buys coins: "))/10
    player['coins']=get_coins
    
    get_bet=int(input("coins to bet: "))
    player["bet"]=get_bet
    
    player["coins"]-=player["bet"]
    
    for i in range(2):
        player['cards'].append(choosefrom(deck))
        dealer['cards'].append(choosefrom(deck))
    
    player["cards"]=check_n_choose_A(player["cards"])
    dealer["cards"]=check_n_choose_A(dealer["cards"])

    print(player["cards"])
    print(dealer["cards"])
        
    if sum(player["cards"])==21:
        print("BLackjack!!! You won!!!!!") 
    
    else:
        while sum(player["cards"]) <21:
            tap_or_hold(player)
            results(player,dealer)
         
while True:
    gamble=input('You want to play BlackJack(y/n)?: ')
    if gamble=='y':
        blackjack()
    else:
        break
       

    
  
