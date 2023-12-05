with open('input') as cards:
    points = 0
    for card in cards.readlines():
        card = card[:-1]
        winners = [i for i in card.split('|')[0].split(' ')[2:] if i != '']
        numbers = [i for i in card.split('|')[1].split(' ') if i != '']
        card_matches = 0
        for number in numbers:
            card_matches += int(number in winners)
        
    print(points)