cards = {}
with open('input') as cards_file:
    points = 0
    for card_number, card in enumerate(cards_file.readlines()):
        card = card[:-1]
        winners = [i for i in card.split('|')[0].split(' ')[2:] if i != '']
        numbers = [i for i in card.split('|')[1].split(' ') if i != '']
        card_matches = 0
        for number in numbers:
            card_matches += int(number in winners)
        cards[card_number] = card_matches
    # Processing card duplication
    new_cards = {key : 0 for key in cards}
    for card_number in range(len(cards)):
        new_cards[card_number] += 1
        for i in range(1, cards[card_number] + 1):
             new_cards[card_number + i] += new_cards[card_number]
    print(sum(new_cards.values()))