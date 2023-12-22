from collections import Counter
import numpy as np

cards_dict = {}
cards = []

with open("input7.txt", "r", encoding="utf-8") as f:
    for line in f:
        card, bid = line.strip().split(" ")
        cards.append(card)
        cards_dict[card] = int(bid)

power_dict = {'five': 6, 'four': 5, 'full': 4, 'three': 3, 'two': 2, 'onepair': 1, 'high': 0}
cards_order = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}


def type_determine(card):
    lettr = [*card]
    cards_dict = Counter(lettr)

    if len(cards_dict) == 1:
        return 'five'
    elif len(cards_dict) == 2:
        if 4 in cards_dict.values():
            return 'four'
        else:
            return 'full'
    elif len(cards_dict) == 3:
        if 3 in cards_dict.values():
            return 'three'
        else:
            return 'two'
    elif len(cards_dict) == 4:
        return 'onepair'
    else:
        return 'high'

def compare_two_cards(card1, card2) -> bool:
    """Compares two cards. Returns true if rank of first card is smaller than
    rank of second card. Essentially, if the card is weaker"""
    if type_determine(card1) == type_determine(card2):
        for i in range(5):
            if card1[i] == card2[i]:
                continue
            return cards_order[card1[i]] < cards_order[card2[i]]

    return power_dict[type_determine(card1)] < power_dict[type_determine(card2)]

def partition(cards, low, high):
    pivot = cards[high]

    i = low - 1
    for j in range(low, high):
        if compare_two_cards(cards[j], pivot):
            i = i + 1

            (cards[i], cards[j]) = (cards[j], cards[i])

    (cards[i + 1], cards[high]) = (cards[high], cards[i + 1])

    return i + 1

def quick_sort(cards, low, high):
    if low < high:
        pi = partition(cards, low, high)

        # Recursive call on the left of pivot
        quick_sort(cards, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(cards, pi + 1, high)

def part1(cards):
    quick_sort(cards, 0, len(cards) - 1)
    sum = 0
    for i, card in enumerate(cards):
        sum += (i + 1) * cards_dict[card]
    return sum


# PART 2

cards_order_2 = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}

def type_determine_2(card):
    lettr = [*card]
    if "J" not in lettr:
        return type_determine(card)

    cards_dict = Counter(lettr)

    #find max. if max is j find next max. replace all max with j.

    max_value = max(cards_dict.values())

    #big_J is a boolean value that is True if J is also equal to the max
    #value of the cards, i.e. no card is repeated more than J
    big_J = False
    for card in cards_dict:
        if card == 'J' and cards_dict[card] == max_value:
            big_J = True
            break
        if cards_dict[card] == max_value:
            chosen = card
            break

    #handle in the case of J being the biggest, delete the first occurrence of J
    if big_J:
        cards_dict['J'] -= 1
        for card in cards_dict:
            max_value = max(cards_dict.values())
            if cards_dict[card] == max_value:
                chosen = card
                break

    for i, value in enumerate(lettr):
        if value == chosen:
            lettr[i] = 'J'

    return type_determine(''.join(lettr))

def compare_two_cards_2(card1, card2) -> bool:
    """Compares two cards. Returns true if rank of first card is smaller than
    rank of second card. Essentially, if the card is weaker"""
    if type_determine_2(card1) == type_determine_2(card2):
        for i in range(5):
            if card1[i] == card2[i]:
                continue
            return cards_order_2[card1[i]] < cards_order_2[card2[i]]
    print(type_determine_2(card1), type_determine_2(card2))
    return power_dict[type_determine_2(card1)] < power_dict[type_determine_2(card2)]

def partition_2(cards, low, high):
    pivot = cards[high]

    i = low - 1
    for j in range(low, high):
        if compare_two_cards_2(cards[j], pivot):
            i = i + 1

            (cards[i], cards[j]) = (cards[j], cards[i])

    (cards[i + 1], cards[high]) = (cards[high], cards[i + 1])

    return i + 1

def quick_sort_2(cards, low, high):
    if low < high:
        pi = partition_2(cards, low, high)

        # Recursive call on the left of pivot
        quick_sort_2(cards, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort_2(cards, pi + 1, high)


def part2(cards):
    quick_sort_2(cards, 0, len(cards) - 1)
    sum = 0
    for i, card in enumerate(cards):
        sum += (i + 1) * cards_dict[card]
    return sum

quick_sort_2(cards, 0, len(cards) - 1)
print(cards)

print(part2(cards))