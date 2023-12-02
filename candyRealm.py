# <Student Name: Tanish Singh>             <11/13/23>
# <Assignment: 6>
# <Description: Game implementation involving a card-based race, named "Candy Realm." It includes functionalities for gameplay between human and AI players. Players draw cards ('M', 'R', 'B', 'G', 'C', 'Y', 'S') that decide their movement on a virtual board>

import random
import colorama
import pyfiglet

def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print()
    print_gradient("Candy Realm!")
    print()
    print_gradient("By: <Tanish Singh>")
    print_gradient("[COM S 127 <G>]")

def initialchoice():
    printbanner()
    choice = input("choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("error: please enter 'p', 'i', or 'q'...")
        choice = input("choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

def printbanner():
    print()
    print_gradient("#######################################################################")
    print()

def wait():
    """ this function has the computer 'wait' until the [enter] key is pressed. this allows 
    for better 'readability' in the final output.
    """
    print()
    input(print_gradient("press [enter] to continue..."))
    print()

def gamechoices(player,color,stop):
    choice = input(f"Player {color}{player}{stop} would you like to [d]raw a M card, [s]huffle the deck, or [q]uit?: ")
    print()

    while choice != "d" and choice != "s" and choice != "q":
        print("error: please enter 'd', 's', or 'q'...")
        choice = input("Would you like to [d]raw a M card, [s]huffle the deck, or [q]uit?: ")
    return choice

def choosenumofplayers():
    numplayers = input("Enter The Number Of Players (1 - 4): ")
    while True:
        if numplayers == "1" or numplayers == "2" or numplayers == "3" or numplayers == "4":
            break
        else:
            print()
            print("Please Valid Enter an Integer.")
            print()
            numplayers = input("Enter The Number Of Players (1 - 4): ")
    numplayers = int(numplayers)
    return numplayers 

def copies():
    copies = input("How Many Copies Of Each Card (1 - 5): ")
    print()
    while True:
        try:
            copies = int(copies)
            if copies >= 1 and copies <= 5:
                print()
                break
            else:
                print()
                print("Error!! Enter A Valid Number Of Copies Each Card Will Have!")
                copies = input("How Many Copies Of Each Card: ")
        except ValueError:
            print("Please Enter A Integer.")
            print()
            copies = input("How Many Copies Of Each Card (1 - 5): ")
            print()
    copies = int(copies)
    return copies

def startdeck(copies):
    colors = ["M","R","B","G","C","Y"]
    deck = []
    for i in range(copies):
        templist=[]
        while len(templist) < 6:
            randcolor = random.choice(colors)
            if randcolor not in templist:
                templist.append(randcolor)
        for i in templist:
            deck.append(i)
        templist = []
    return deck

def startdecks(copies):
    colors = ["M","R","B","G","C","Y","S"]
    deck = []
    for i in range(copies):
        templist=[]
        while len(templist) < 6:
            randcolor = random.choice(colors)
            if randcolor not in templist:
                templist.append(randcolor)
        for i in templist:
            deck.append(i)
        templist = []
    return deck

def deckfafterdraw(shuffleddeck):
    colors = ["M","R","B","G","C","Y","S"]
    newshuffleddeck = shuffleddeck[1:]
    newshuffleddeck.append(random.choice(colors))
    return newshuffleddeck

def cardsshuffler(shuffleddeck):
    random.shuffle(shuffleddeck)
    return shuffleddeck

def reachedgoal(startdeck1,lastindex,player):
    nowinner = True
    if lastindex == len(startdeck1)-1:
        nowinner = False
        return nowinner,player
    else:
        nowinner = True
        return nowinner,player

def printdecks(startdeck1, shuffleddeck):
    print(f"START", end= "")
    for i in startdeck1:
        color = findcolor(i)
        print(color,i, end = '')
    print(colorama.Fore.RESET+colorama.Style.RESET_ALL+" ", end=("\n"))

    print(f"CARDS", end= "")
    for i in shuffleddeck:
        color = findcolor(i)
        print(color,i, end = "")
    print(colorama.Fore.RESET+colorama.Style.RESET_ALL+" ", end=("\n"))
    pass

def p1position(shift,player):
    updatedshift = 6 + shift
    P1 = []
    for i in range(updatedshift):
        P1.append(" ")  
    P1.append(player)
    return P1

def printpositions(p1,card):
    if isinstance(card, str):
        color = findcolor(card)
    else:
        color = ""
    for i in p1:
        if i == " ":
            print(i, end='')
        else:
            print(f"{color}{i}",end="")
    print(colorama.Fore.RESET,end="")
    print("", end="\n")

def print_gradient(text):
    colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN, colorama.Fore.BLUE, colorama.Fore.MAGENTA,colorama.Fore.CYAN]
    step = len(text) / len(colors)

    for i, char in enumerate(text):
        if step != 0:
            color_index = int(i / step)
            color = colors[color_index]
            print(f"{color}{char}", end="")
    print(colorama.Fore.RESET)
    return ""

def printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4):
    printpositions(p1,card1)
    printpositions(p2,card2)
    printpositions(p3,card3)
    printpositions(p4,card4)
    printdecks(startdeck1,shuffleddeck)

def celebration(player):
    text = "WOO HOO !!!"
    text1 = f"Player {player} Has Won" 
    font = pyfiglet.Figlet("small")
    result = font.renderText(text)
    result1 = font.renderText(text1)
    print()
    printbanner()
    print_gradient(result)
    print_gradient(result1)
    printbanner()

def findcolor(card):
    color = None
    if card == "Y":
        color = colorama.Style.BRIGHT+colorama.Fore.YELLOW
    elif card == "R":
        color = colorama.Style.BRIGHT+colorama.Fore.RED
    elif card == "B":
        color = colorama.Style.BRIGHT+colorama.Fore.BLUE
    elif card == "M":
        color = colorama.Style.BRIGHT+colorama.Fore.MAGENTA
    elif card == "G":
        color = colorama.Style.BRIGHT+colorama.Fore.GREEN
    elif card == "C":
        color = colorama.Style.BRIGHT+colorama.Fore.CYAN
    elif card == "S":
        color = colorama.Style.BRIGHT+colorama.Fore.BLACK
    else:
        color = colorama.Fore.RESET
    return color

def currentposition(player,currentshift):
    pos = 0
    playerlist = p1position(currentshift, player)
    for i in range(len(playerlist)):
        if playerlist[i] != " ":
            pos = i
    return pos

def updateposition(list, startdeck1, card, player, currentshift, copies,lastindex):
    targetindex, newshift = gainposition(startdeck1, card, player, currentshift, copies,lastindex)
    lastpos = currentposition(player, currentshift)
    list[lastpos] = " "
    color = findcolor(card)
    newlist = p1position(newshift, player)
    return newlist, newshift,targetindex,lastindex

def gainposition(startdeck1, card, player, currentshift, copies,lastindex):
    lastpos = currentposition(player, currentshift)
    shift = 0    
    try:
        if startdeck1[lastindex]== card and card in startdeck1[lastindex+1:]:
            if lastindex == 0 and lastindex == startdeck1.index(card):
                return lastindex, currentshift
            targetindex = startdeck1.index(card)
            targetindex1,targetindex2,targetindex3,targetindex4 = -1,-1,-1,-1
            if copies == 3:
                targetindex1 = startdeck1.index(card, targetindex+1)
                targetindex2 = startdeck1.index(card, targetindex1+1)
            elif copies == 4:
                targetindex1 = startdeck1.index(card, targetindex+1)
                targetindex2 = startdeck1.index(card, targetindex1+1)
                targetindex3 = startdeck1.index(card, targetindex2+1)
            elif copies == 5:
                targetindex1 = startdeck1.index(card, targetindex+1)
                targetindex2 = startdeck1.index(card, targetindex1+1)
                targetindex3 = startdeck1.index(card, targetindex2+1)
                targetindex4 = startdeck1.index(card, targetindex3+1)
            else:
                pass
            if targetindex+targetindex > lastpos-6:
                shift = currentshift+targetindex+targetindex
                return targetindex,shift
            elif targetindex+targetindex == lastpos-6: 
                targetindex1 = startdeck1.index(card, targetindex+1)
                shift = currentshift+targetindex1-targetindex+targetindex1-targetindex
                return targetindex1,shift
            elif targetindex1+targetindex1 == lastpos-6: 
                shift = currentshift+targetindex2-targetindex1+targetindex2-targetindex1
                return targetindex2,shift
            elif targetindex2+targetindex2 == lastpos-6:
                shift = currentshift+targetindex3-targetindex2+targetindex3-targetindex2
                return targetindex3,shift
            elif targetindex3+targetindex3 == lastpos-6: 
                shift = currentshift+targetindex4-targetindex3+targetindex4-targetindex3
                return targetindex4,shift
        elif startdeck1[lastindex] != card and card in startdeck1[lastindex:]:
            ind = (lastpos-6)/2
            targetindex = startdeck1.index(card, int(ind))
            shift = currentshift+targetindex-lastindex+targetindex-lastindex
            return targetindex,shift
        else:
            return targetindex, currentshift
    except Exception as e:
        pass
    return lastindex, currentshift

def humanplayer(shuffleddeck,startdeck1,player,shift1,copies,targetindex):
    card = startdeck1[targetindex]
    color = findcolor(card)
    stop = colorama.Style.RESET_ALL+colorama.Fore.RESET
    choice = gamechoices(player,color,stop)
    if choice == "s":
        p1 = p1position(shift1, player)
        shuffleddeck = cardsshuffler(shuffleddeck)
        card = startdeck1[targetindex]
        color = findcolor(card)
        print(f"Player {color}{player}{stop} Chose To Shuffle")
        print()
        nowinners = True
        winner = -1
        return p1, shuffleddeck,shift1,nowinners,winner,targetindex,card
    elif choice == "d":
        card = shuffleddeck[0]
        if shuffleddeck[0] == startdeck1[0]and targetindex == 0:
            card = startdeck1[targetindex]
            color = findcolor(card)
            p1 = p1position(shift1,player)
            lastindex = targetindex
            print(f"Player {color}{player}{stop}, You Need To Draw A Different Color Than Your Starting Color To Begin!")
            print()
            nowinners,winner = reachedgoal(startdeck1,targetindex,player)
            shuffleddeck = deckfafterdraw(shuffleddeck)
            return p1, shuffleddeck,shift1,nowinners,winner,targetindex,card
        elif card != "S":
            p1, shift1,targetindex,lastindex = updateposition(p1position(shift1, player),startdeck1,card,player,shift1,copies,targetindex)
            if lastindex < targetindex and card != "S":
                color = findcolor(card)
                print(f"Player {color}{player}{stop} Drew a: {color}{card}{stop}")
                print()
            elif targetindex == lastindex and targetindex > 0 and card != "S":
                print(f"Player {color}{player}{stop} Drew a: {color}{card}{stop}")
                card = startdeck1[lastindex]
                color = findcolor(card)
                print()
                print(f"Player {color}{player}{stop}, Your Card Is No Longer In The Board So Your Turn Has Been Skipped")
        elif card == "S":
            card = startdeck1[targetindex]
            color = findcolor(card)
            p1 = p1position(shift1,player)
            lastindex = targetindex
            print(f"Player {color}{player}{stop} Landed On A Sticky Card!")
            print()
        nowinners,winner = reachedgoal(startdeck1,targetindex,player)
        shuffleddeck = deckfafterdraw(shuffleddeck)
        return p1, shuffleddeck,shift1,nowinners,winner,targetindex,card
    elif choice == "q":
        p1 = p1position(shift1, player)
        nowinners = -1
        winner = -1
        card = startdeck1[targetindex]
        color = findcolor(card)
        stop = colorama.Style.RESET_ALL+colorama.Fore.RESET
        print(f"Player {color}{player}{stop} Quit The Game.")
        print()
        return p1, shuffleddeck,shift1,nowinners,winner,targetindex,card
    while choice != "s" and choice != "d" and choice != "q":
        print("error: please enter 'd', 's', or 'q'...")
        choice = gamechoices()
    pass 

def aiplayer(shuffleddeck,startdeck1,player,shift1,copies,targetindex):
    card = shuffleddeck[0]
    lastpos1= currentposition(player, shift1)
    ind1 = (lastpos1-6)/2
    stop = colorama.Style.RESET_ALL+colorama.Fore.RESET
    if shuffleddeck[0] == startdeck1[0] and targetindex == 0:
        card = startdeck1[targetindex]
        color = findcolor(card)
        stop = colorama.Style.RESET_ALL+colorama.Fore.RESET
        p1 = p1position(shift1,player)
        lastindex = targetindex
        print(f"Player {color}{player}{stop}, You Need To Draw A Different Color Than Your Starting Color To Begin!")
        print()
        nowinners,winner = reachedgoal(startdeck1,targetindex,player)
        shuffleddeck = deckfafterdraw(shuffleddeck)
        return p1, shuffleddeck,shift1,nowinners,winner,targetindex,card
    elif card == "S":
        card = startdeck1[targetindex]
        color = findcolor(card)
        stop = colorama.Style.RESET_ALL+colorama.Fore.RESET
        p1 = p1position(shift1,player)
        lastindex = targetindex
        print(f"Player {color}{player}{stop} Landed On A Sticky Card!")
        print()
        nowinners,winner = reachedgoal(startdeck1,targetindex,player)
        shuffleddeck = deckfafterdraw(shuffleddeck)
        return p1, shuffleddeck,shift1,nowinners,winner,targetindex,card
    try:
        targetindextest = startdeck1.index(card, int(ind1))
        if targetindex+targetindextest > targetindex+1:
            card = shuffleddeck[0]
            p1, shift1,targetindex,lastindex = updateposition(p1position(shift1, player),startdeck1,card,player,shift1,copies,targetindex)
            if lastindex < targetindex:
                color = findcolor(card)
                stop = colorama.Style.RESET_ALL+colorama.Fore.RESET
                print(f"Player {color}{player}{stop} Drew a: {color}{card}{stop}")
                print()
            elif targetindex == lastindex and targetindex > 0:
                card = startdeck1[lastindex]
                color = findcolor(card)
                stop = colorama.Style.RESET_ALL+colorama.Fore.RESET
                print(f"Player {color}{player}{stop} Drew a: {color}{card}{stop}")
                print()
                print(f"Player {color}{player}{stop}, Your Card Is No Longer In The Board So Your Turn Has Been Skipped")
            nowinners,winner = reachedgoal(startdeck1,targetindex,player)
            shuffleddeck = deckfafterdraw(shuffleddeck)
            return p1,shuffleddeck,shift1,nowinners,winner,targetindex,card
        else:
            p1 = p1position(shift1, player)
            card = startdeck1[targetindex]
            color = findcolor(card)
            stop = colorama.Style.RESET_ALL+colorama.Fore.RESET
            print(f"Player {color}{player}{stop} Chose To Shuffle")
            
            print()
            shuffleddeck = cardsshuffler(shuffleddeck)
            nowinners = True
            winner = -1
            return p1,shuffleddeck,shift1,nowinners,winner,targetindex,card
    except Exception:
        p1 = p1position(shift1, player)
        card = startdeck1[targetindex]
        return p1, shuffleddeck,shift1,True,-1,targetindex,card
    
def main():
    """This function is where all the fun happens!
    """
    printTitleMaterial()
    choice = initialchoice()
    printbanner()
    while choice == "i":
        print("Choose the number of players (1-4) and the number of copies for each card (1-5).")
        wait()
        print("Players take turns drawing cards ('M', 'R', 'B', 'G', 'C', 'Y', 'S') that determine movement or actions on the board.")
        wait()
        print("Choose to draw a 'M' card, shuffle the deck ('S'), or quit ('Q') when prompted.")
        wait()
        print("Players navigate the board based on the drawn cards, aiming to reach the goal.")
        wait()
        print("The first player to reach the goal wins the game.")
        wait()
        print("Alternates between human and AI players, displaying positions and decks after each turn.")
        wait()
        print("Certain cards, notably 'S' (sticky), affect player movement by altering their position or limiting their actions on the board.")
        wait()
        print("Players must draw a card different from the starting card at the beginning of the game to initiate movement on the board.")
        wait()
        print("If a player's drawn card is no longer present on the board, their turn gets skipped, requiring strategic card selection to ensure continued progress.")
        choice = initialchoice()
        print()
    if choice == "p":
        numplayer = choosenumofplayers()
        copies1 = copies()
        print()
        print()        
        startdeck1 = startdeck(copies1)
        shuffleddeck = startdecks(copies1)
        shift1,shift2,shift3,shift4 = 0,0,0,0
        card1,card2,card3,card4 = startdeck1[0],startdeck1[0],startdeck1[0],startdeck1[0]
        p1,p2,p3,p4 = p1position(shift1,1),p1position(shift1,2),p1position(shift3,3),p1position(shift4,4)
        printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
        print()
        nowinner = True
        printbanner()
        if numplayer == 1:
            targetindex1,targetindex2,targetindex3,targetindex4= 0,0,0,0
            while nowinner == True:
                wait()
                p1,shuffleddeck,shift1,nowinner,winner,targetindex1,card1 = humanplayer(shuffleddeck,startdeck1,1,shift1,copies1,targetindex1)
                if nowinner != -1:
                    printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
                wait()
                p2,shuffleddeck,shift2,nowinner,winner,targetindex2,card2 = aiplayer(shuffleddeck,startdeck1,2,shift2,copies1,targetindex2)
                printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
                wait()
                p3,shuffleddeck,shift3,nowinner,winner,targetindex3,card3 = aiplayer(shuffleddeck,startdeck1,3,shift3,copies1,targetindex3)
                printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
                wait()
                p4,shuffleddeck,shift4,nowinner,winner,targetindex4,card4 = aiplayer(shuffleddeck,startdeck1,4,shift4,copies1,targetindex4)
                printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
            if nowinner != True and nowinner != -1:
                celebration(winner)
        elif numplayer == 2:
            targetindex1,targetindex2,targetindex3,targetindex4= 0,0,0,0
            while nowinner == True:
                wait()
                p1,shuffleddeck,shift1,nowinner,winner,targetindex1,card1 = humanplayer(shuffleddeck,startdeck1,1,shift1,copies1,targetindex1)
                if nowinner != -1:
                    printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
                wait()
                p2, shuffleddeck,shift2,nowinner,winner,targetindex2,card2 = humanplayer(shuffleddeck,startdeck1,2,shift2,copies1,targetindex2)
                if nowinner != -1:
                    printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
                wait()
                p3,shuffleddeck,shift3,nowinner,winner,targetindex3,card3 = aiplayer(shuffleddeck,startdeck1,3,shift3,copies1,targetindex3)
                printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
                wait()
                p4,shuffleddeck,shift4,nowinner,winner,targetindex4,card4 = aiplayer(shuffleddeck,startdeck1,4,shift4,copies1,targetindex4)
                printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
            if nowinner != True and nowinner != -1:
                celebration(winner)
        elif numplayer == 3:
            targetindex1,targetindex2,targetindex3,targetindex4= 0,0,0,0
            while nowinner == True:
                wait()
                p1,shuffleddeck,shift1,nowinner,winner,targetindex1,card1 = humanplayer(shuffleddeck,startdeck1,1,shift1,copies1,targetindex1)
                if nowinner != -1:
                    printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
                wait()
                p2,shuffleddeck,shift2,nowinner,winner,targetindex2,card2 = humanplayer(shuffleddeck,startdeck1,2,shift2,copies1,targetindex2)
                if nowinner != -1:
                    printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
                wait()
                p3,shuffleddeck,shift3,nowinner,winner,targetindex3,card3 = humanplayer(shuffleddeck,startdeck1,3,shift3,copies1,targetindex3)
                if nowinner != -1:
                    printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
                wait()
                p4,shuffleddeck,shift4,nowinner,winner,targetindex4,card4 = aiplayer(shuffleddeck,startdeck1,4,shift4,copies1,targetindex4)
                printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
            if nowinner != True and nowinner != -1:
                celebration(winner)
        else:
            targetindex1,targetindex2,targetindex3,targetindex4= 0,0,0,0
            while nowinner == True:
                wait()
                p1,shuffleddeck,shift1,nowinner,winner,targetindex1,card1 = humanplayer(shuffleddeck,startdeck1,1,shift1,copies1,targetindex1)
                if nowinner != -1:
                    printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
                wait()
                p2,shuffleddeck,shift2,nowinner,winner,targetindex2,card2 = humanplayer(shuffleddeck,startdeck1,2,shift2,copies1,targetindex2)
                if nowinner != -1:
                    printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
                wait()
                p3,shuffleddeck,shift3,nowinner,winner,targetindex3,card3 = humanplayer(shuffleddeck,startdeck1,3,shift3,copies1,targetindex3)
                if nowinner != -1:
                    printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
                wait()
                p4,shuffleddeck,shift4,nowinner,winner,targetindex4,card4 = humanplayer(shuffleddeck,startdeck1,4,shift4,copies1,targetindex4)
                if nowinner != -1:
                    printpostionsanddecks(p1,p2,p3,p4,startdeck1,shuffleddeck,card1,card2,card3,card4)
                if nowinner != True or nowinner == -1:
                    break
            if nowinner != True and nowinner != -1:
                celebration(winner)
    elif choice == "q":
        print("GoodBye!!")
        print()
        pass


if __name__ == "__main__":
    main()
    
