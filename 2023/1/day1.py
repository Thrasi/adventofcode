class Day1:
    def __init__(self):
        pass

    def extract_first_and_last_number(self, line):
        digits = [char for char in line if char.isdigit()]
        return int(f"{digits[0]}{digits[-1]}") if len(digits) > 0 else None
    
    def task1(self, task_input):
        lines = task_input.split("\n")
        digits = filter(lambda x: x!=None , list(map(self.extract_first_and_last_number, lines)))
        return sum(digits)
    

    def find_first_occurence_of_number(self, line, reverse=False):
        numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        if reverse:
            line = line[::-1]
            numbers = [number[::-1] for number in numbers]
        
        for index, char in enumerate(line):
            if char.isdigit():
                return char
            else:
                for number, number_word in enumerate(numbers):
                    if line[index:].startswith(number_word):
                        return str(number)
        return None

    def extract_first_and_last_number_with_words(self, line):
        first_number = self.find_first_occurence_of_number(line)
        last_number = self.find_first_occurence_of_number(line, reverse=True)
        return int(f"{first_number}{last_number}") if first_number != None else None
    
    def task2(self, task_input):
        lines = task_input.split("\n")
        digits = filter(lambda x: x!=None , list(map(self.extract_first_and_last_number_with_words, lines)))
        return sum(digits)