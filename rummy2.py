import random

# Setup
players = 0
suits = ['S', 'H', 'C', 'D']
ranks = ['2', '3', '4', '5', '6', '7',
         '8', '9', '10', 'J', 'Q', 'K', 'A']
# Game
deck = []
hands = []
discard_pile = []
points = []
played_cards = []
game_in_progress = False
winner = False


def setup_game():
    players = 3
    winning_points = 500

    def shuffle(deck):
        for i in range(1000):
            a = random.randrange(0, 51)
            b = random.randrange(0, 51)
            deck[a], deck[b] = deck[b], deck[a]
        return deck

    def create_deck(deck):
        # suits = ['S', 'H', 'C', 'D']
        # ranks = ['2', '3', '4', '5', '6', '7',
        #          '8', '9', '10', 'J', 'Q', 'K', 'A']

        for r in range(len(ranks)):
            for s in range(len(suits)):
                deck.append(ranks[r]+suits[s])
        return deck

    shuffle(create_deck(deck))
    # deal
    for p in range(players):
        hands.append([])
        played_cards.append([])
        for c in range(7):
            hands[p].append(draw())
    # flip discard
    discard_pile.append(draw())
    print("Discard pile:", discard_pile)
    # for p in range(players):
    #     print("Player",p)
    #     for c in range(len(playerhands[p])):
    #         print(playerhands[p][c])


def print_game_for_player(p):
    # print discard
    print('Discards:', hand_to_str(discard_pile))
    # print played
    print('Played:', played_cards)
    # print player p's hand
    print('Your Hand:',hand_to_str(hands[p]),'\n')


def draw():
    return deck.pop()


def ai_think():
    def get_points(card):
        ten_cards = ['10', 'J', 'Q', 'K']
        if card[0] == 'A':
            return 3
        elif card[0] in ten_cards:
            return 2
        else:
            return 1


    def get_next_in_suit(c):
        if ranks.index(c) == 12:
            return c[0] + ranks[0]
        else:
            return c[0] + ranks[ranks.index(c)+1]

    def get_prev_in_suit(c):
        if ranks.index(c) == 0:
            return c[0] + ranks[12]
        else:
            return c[0] + ranks[ranks.index(c)-1]


    def get_same_rank_as(c):
        pass


    def create_prospects(hand):
        prospects = {}
        for c in hand:
            pass

        # print(prospects)

    def augment_prospect(c):
        if c in prospects:
            prospects[c] += get_points(c)
        else:
            prospects[c] = get_points(c)


    def ai_turn(player_number):
        pass

    # def card_to_str(card):
    #     return str(card[0])


def discard(cards):
    return cards.pop()


def hand_to_str(hand):
    s = ''
    for c in hand:
        s += '[' + c + ']'
    return s


def player_turn(player_number):
    global winner
    print("Player", player_number, "'s turn:")
    # print("hand:", hand_to_str(hands[player_number]))
    # print("discards:", hand_to_str(discard_pile))
    # print(len(hands[player_number]))

    print_game_for_player(player_number)

    if len(hands[player_number]) > 0:
        discard_pile.append(discard(hands[player_number]))
    else:
        winner = True
        print(winner)


def play():
    rounds = 0
    while winner is False and rounds < 5:
        rounds += 1
        print("******** Round:", rounds,"********")
        for p in range(len(hands)):
                player_turn(p)


def main():

    setup_game()
    play()


if __name__ == '__main__':
    main()
