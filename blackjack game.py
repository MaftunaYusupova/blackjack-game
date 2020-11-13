import random

# # MTE Assignment - Blackjack game
# # Maftuna Yusupova
# /Section B /B.Tech


# The planning of the game
# Dealer and player cards
# Deal and display the cards
# Sum of dealer, player cards and compare them
# if Player card is greater than 21=Bust
# if player card is less than 21=Stay or hit
# if stay then compare player and dealer
# if player sum<21 and > dealer then player wins
# if player sum<dealer then player loses
dealer=[]
player=[]
while len(dealer)!=2:
    dealer.append(random.randint(1,11))
    if len(dealer)==2:
        print("Dealer has ",dealer)
while len(player)!=2:
    player.append(random.randint(1,11))
    if len(player)==2:
        print("Player has ",player)
if sum(dealer)==21:
    print("Dealer has 21 and wins")
elif sum(dealer)>21:
    print("Dealer has busted")
while sum(player)<21:
    action=str(input("Do you want to stay or hit: "))
    if action=='hit':
        player.append(random.randint(1,11))
        print("You have a total of "+str(sum(player))+"from these cards",player)
    else:
        print("The dealer has a total of "+str(sum(dealer))+"from these cards",dealer)
        print("You have a total of "+str(sum(player))+"from these cards",player)
        if sum(dealer)>sum(player):
            print("Dealer wins!!!")
        else:
            print("You win!!!")
            break
if sum(player)>21:
    print("Dealer wins! You busted")
elif sum(player)==21:
    print("You win!!! You have Blackjack")
