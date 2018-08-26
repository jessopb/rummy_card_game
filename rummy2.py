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
            a = random.randint(0, 51)
            b = random.randint(0, 51)
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
        for c in range(7):
            hands[p].append(draw())
    # flip discard
    discard_pile.append(draw())


def print_game_for_player(p):
    def hand_to_str(hand):
        s = ''
        for c in hand:
            s += f' ({hand.index(c)}): ' + c + '  '
        return s

    def play_to_str(pl):
        s = ''
        for c in pl:
            s += f' {c} '
        return s

    def collections_to_str(collections):
        coll_str = ''
        for collection in collections:
            coll_str = coll_str + '\n['
            for play in collection:
                coll_str = coll_str + '(' + play_to_str(play) + ')'
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
    def get_points(c):
        pass


    def get_neighbors_in_suit(c):
        pass


    def get_same_rank_as(c):
        pass


    def create_prospects(hand):
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


def discard(hand, hi=0):
    discard_pile.append(hand.pop(hi))


def player_turn(player_number):
    global winner

    def draw_phase():
        global discard_pile
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
            elif bottom == len(discard_pile)-1:
                hands[player_number].append(discard_pile.pop())

    def play_to_collection(play_index_list, player_number):
        '''REFACTOR
        '''
        the_play = []
        for p in play_index_list:
            the_play.append(hands[player_number][int(p)])
        for c in the_play:
            hands[player_number].remove(c)
        print(the_play)
        print(hands[player_number])
        return the_play

    def discard_phase(player_number):
        index_to_discard = int(input('What would you like to discard? #:'))
        discard_pile.append(hands[player_number].pop(index_to_discard))

    print(f"**** Player {player_number}'s turn: ****")

    print_game_for_player(player_number)
    # TODO catch errors, draw again
    draw_phase()

    print_game_for_player(player_number)

    # TODO play_phase function
    # TODO loop play_phase until NO
    to_play = 'n'
    to_play = input('Would you like to play any of your cards?(Y,N)').lower()[0]
    if to_play == 'y':
        what_to_play_str = input('Enter cards you would like to play( \'1,4,12\' ):')
        what_to_play = what_to_play_str.split(',')
        collections[player_number].append(play_to_collection(what_to_play, player_number))

    print_game_for_player(player_number)
    discard_phase(player_number)

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
