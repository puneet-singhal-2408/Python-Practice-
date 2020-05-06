def main():
    
    Player_1 = input("Enter your name : ")
    Player_2 = input("Enter your name : ")

    P1 = input("Select one from Rock Paper Scissors : ")
    P2 = input("Select one from Rock Paper Scissors : ")

    P1.lower()
    P2.lower()
        
    def winner(P1,P2):
        if P1=="rock" and P2=="paper":
            return("Player2 Wins")
        elif P1== "rock" and P2== "scissors":
            return("Player1 Wins")
        elif P1== "paper" and P2== "rock":
            return("Player1 wins")    
        elif P1== "paper" and P2== "scissors":
            return("player2 wins")
        elif P1 == "scissors" and P2 == "rock":
            return("Player2 Wins")
        elif P1 == "scissors" and P2 == "paper":
            return("Player1 wins")

    print(winner(P1,P2))
    play_again = input("play again ? 1: Press 1 to Play again , 2: Press 2 to Exit")
    if play_again == "1":
        main()
    else:
        exit()
if __name__ == "__main__":
    main()
