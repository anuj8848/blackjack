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
        
    # if player["cards"].sum==21:
    #     print("BLackjack!!! You won!!!!!") 
    # else
           
  
    
            
    

blackjack()
        
        

    
