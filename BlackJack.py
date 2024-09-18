import random, subprocess

def clear():
    subprocess.run('cls', shell='True')        

def blackjack():
    cardsPlayer = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    cardsComputer = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    totalPlayerValue = 0
    totalComputerValue = 0
    playerLost = False
    computerLost = False
    gameContinue = True
    playerCards = []
    computerCards = []
    
    response = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")
    
    if response == 'n':
        gameContinue = False
        clear()
        print("Play again soon!")
    else:
            clear()
            playerCards.append(cardsPlayer[random.randint(0,10)])
            totalPlayerValue = playerCards[0]
            if totalPlayerValue > 10:
                cardsPlayer[0] = 1 
            playerCards.append(cardsPlayer[random.randint(0,10)])
            computerCards.append(cardsComputer[random.randint(0,10)])
            if totalComputerValue > 10:
                cardsComputer[0] = 1
            computerCards.append(cardsComputer[random.randint(0,10)])
            if totalComputerValue > 10:
                cardsComputer[0] = 1
            print(f"Your cards: {playerCards}")
            print(f"Computer's first card: {computerCards[0]}")
            for card in computerCards:
                    totalComputerValue += card
            while totalComputerValue < 17:
                        computerCards.append(cardsComputer[random.randint(0,10)])
                        totalComputerValue += computerCards[len(computerCards)-1]
    while gameContinue == True:
            response2 = input("Type 'y' to get another card, type 'n' to pass: ")
            if response2 == 'y':
                playerCards.append(cardsPlayer[random.randint(0,10)])
                print(f"Your cards: {playerCards}")
                print(f"Computer's first card: {computerCards[0]}")
            else:
                for card in playerCards:
                    totalPlayerValue += card
                totalPlayerValue -= playerCards[0]
                if totalPlayerValue > 21:
                     playerLost = True
                if totalComputerValue > 21:
                     computerLost = True
                if playerLost:
                    if computerLost:
                        print(f"Your final hand: {playerCards}")
                        print(f"Computer's final hand: {computerCards}")
                        print("You both went overboard. Draw")
                        gameContinue = False
                        blackjack()
                    else:  
                        print(f"Your final hand: {playerCards}")
                        print(f"Computer's final hand: {computerCards}")
                        print("You went overboard. Computer Wins")
                        gameContinue = False
                        blackjack()
                elif computerLost:
                    if playerLost:
                        print(f"Your final hand: {playerCards}")
                        print(f"Computer's final hand: {computerCards}")
                        print("You both went overboard. Draw")
                        gameContinue = False
                        blackjack()
                    else:  
                        print(f"Your final hand: {playerCards}")
                        print(f"Computer's final hand: {computerCards}")
                        print("Computer went overboard. You Win")
                        gameContinue = False
                        blackjack()
                else:
                    if totalPlayerValue > totalComputerValue:
                        print(f"Your final hand: {playerCards}")
                        print(f"Computer's final hand: {computerCards}")
                        print("You Win")
                        gameContinue = False
                        blackjack()
                    elif totalPlayerValue < totalComputerValue:
                        print(f"Your final hand: {playerCards}")
                        print(f"Computer's final hand: {computerCards}")
                        print("You Lose")
                        gameContinue = False
                        blackjack()
                    else:
                        print(f"Your final hand: {playerCards}")
                        print(f"Computer's final hand: {computerCards}")
                        print("Draw")
                        gameContinue = False
                        blackjack()
blackjack()    
