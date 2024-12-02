import re

class Day4:
    def __init__(self):
        pass

    def get_number_of_winning_numbers(self, card):
        winning_numbers = set(card[0].split())
        numbers = set(card[1].split())
        return len(winning_numbers.intersection(numbers))

    def task1(self, task_input):
        lines = task_input.split("\n")
        cards = [line.split(":")[1].split("|") for line in lines]
        winning_numbers = filter(lambda x: x > 0, map(self.get_number_of_winning_numbers, cards))
        return sum(map(lambda x: 2**(x-1), winning_numbers))
    
    def task2(self, task_input):
        lines = task_input.split("\n")
        cards = [line.split(":")[1].split("|") for line in lines]
        winning_numbers = list(map(self.get_number_of_winning_numbers, cards))
        card_copies = len(cards) * [1]
        for card, winnings in enumerate(winning_numbers):
            for i in range(winnings):
                card_copies[card+i+1] += card_copies[card]
        
        return sum(card_copies)