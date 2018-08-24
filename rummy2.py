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
collections = []
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
        collections.append([])
        # test collections_to_str
        # collections[p].append(['AH','AC','AD'])
        for c in range(7):
            hands[p].append(draw())
    # flip discard
    discard_pile.append(draw())
    print("Discard pile:", discard_pile)
    # for p in range(players):
    #     print("Player",p)
    #     for c in range(len(playerhands[p])):
    #         print(playerhands[p][c])
    print('Hands:', hands)


def print_game_for_player(p):
    def hand_to_str(hand):
        s = ''
        for c in hand:
            s += f' ({hand.index(c)}): ' + c + '  '
        return s

    def collections_to_str(collections):
        coll_str = ''
        for collection in collections:
            coll_str = coll_str + '\n['
            for play in collection:
                coll_str = coll_str + '(' + hand_to_str(play) + ')'
            coll_str = coll_str + ']'
        return coll_str
    # print played
    print(f'Played:{collections_to_str(collections)}')
    # print discard
    print('Discards:', hand_to_str(discard_pile))
    # print player p's hand
    print('Your Hand:', hand_to_str(hands[p]), '\n')


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


def draw_input(player_number):
    '''Replaces inline draw code
    '''
    pass


def player_turn(player_number):
    global winner
    global discard_pile
    print(f"**** Player {player_number}'s turn: ****")

    print_game_for_player(player_number)
    draw_source = input('Draw a (N)ew card or from (D)iscard?').lower()[0]
    if draw_source == 'n':
        hands[player_number].append(draw())
        print('You drew a', hands[player_number][-1])
    elif draw_source == 'd':
        bottom = int(input("what's the bottom card?"))
        print(bottom)
        # needs all cases covered
        if bottom == 0:
            hands[player_number].extend(discard_pile)
            discard_pile = []
        elif bottom < len(discard_pile)-1:
            hands[player_number].extend(discard_pile[bottom:])
            discard_pile = discard_pile[:bottom]

    discard_pile.append(discard(hands[player_number]))
    if len(hands[player_number]) == 0:
        winner = True
        print(f'Player {player_number} wins!')

    print_game_for_player(player_number)


def play():
    rounds = 0
    while winner is False and rounds < 10:
        rounds += 1
        print(f"******** Round: {rounds} ********")
        for p in range(len(hands)):
                player_turn(p)


def main():

    setup_game()
    play()


if __name__ == '__main__':
    main()
