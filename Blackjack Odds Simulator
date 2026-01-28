Function playOneGame()
    Deal two cards to player
    Deal two cards to dealer
    If player total is 21 and dealer total is not 21
        Player wins
    Else if player total > 21
        Player loses
    Else
        While player total < 17
            Player hits
            Add card to player total
            If player total > 21
                Player loses
        While dealer total < 17
            Dealer hits
            Add card to dealer total
        If dealer total > 21
            Player wins
        Else if dealer total > player total
            Player loses
        Else if dealer total < player total
            Player wins
        Else
            Tie
    Return result

Main Program
    Set wins = 0
    Set losses = 0
    Set ties = 0
    Input number of games to simulate
    Loop from 1 to number of games
        Call playOneGame()
        Update wins/losses/ties based on result
    Output total wins, losses, ties, and win percentage
    Save results to log file
