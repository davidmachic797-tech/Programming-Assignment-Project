import random

def deal_card():
    """Returns a random card value between 1 and 11 (simplified for simulation)."""
    return random.randint(1, 11)

def play_one_game():
    player_total = deal_card() + deal_card()
    dealer_total = deal_card() + deal_card()

    # Check for immediate win/loss
    if player_total == 21 and dealer_total != 21:
        return "win"
    elif player_total > 21:
        return "loss"

    # Player hits until 17 or bust
    while player_total < 17:
        player_total += deal_card()
        if player_total > 21:
            return "loss"

    # Dealer hits until 17 or bust
    while dealer_total < 17:
        dealer_total += deal_card()
        if dealer_total > 21:
            return "win"

    # Compare totals
    if dealer_total > player_total:
        return "loss"
    elif dealer_total < player_total:
        return "win"
    else:
        return "tie"

def main():
    wins = 0
    losses = 0
    ties = 0

    try:
        num_games = int(input("Enter number of games to simulate: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for _ in range(num_games):
        result = play_one_game()
        if result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        else:
            ties += 1

    print(f"Results after {num_games} games:")
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")

if __name__ == "__main__":
    main()
