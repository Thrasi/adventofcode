import re

class Day3:
    def __init__(self):
        self.symbol_pattern = p=re.compile(r"[^0-9\.]")
        self.number_pattern = p=re.compile(r"\d+")
    
    def span_has_symbol(self, span, line):
        slice = line[max(span[0]-1, 0):min(span[1]+1, len(line))]
        return bool(re.search(self.symbol_pattern, slice))
    
    def is_part_number(self, number, lines_to_check):
        for line in lines_to_check:
            if self.span_has_symbol(number.span(), line):
                return True
        return False
    
    def overlap(self, span1, span2):
        """Overlapping of right non inclusive spans: [c, d) and [a, b)"""
        return span1[1]-1 >= span2[0] and span2[1]-1 >= span1[0]
    
    def get_overlapping_numbers(self, gear_span, numbers_to_check):
        return [number for number in numbers_to_check if self.overlap(gear_span, number.span())]
    
    def is_gear(self, gear_span, numbers_to_check):
        numbers = self.get_overlapping_numbers(gear_span, numbers_to_check)
        return len(numbers) == 2
    
    def get_increased_span(self, span):
        return [span[0]-1, span[1]+1]

    def task2(self, task_input):
        lines = task_input.split("\n")
        star_lines = [list(re.finditer(r"\*", line)) for line in lines]
        number_lines = [list(re.finditer(self.number_pattern, line)) for line in lines]
        gears = []
        for line_nr, stars in enumerate(star_lines):
            number_lines_to_check = number_lines[max(line_nr-1, 0):min(line_nr+2, len(number_lines))]
            numbers_to_check = [number for number_line in number_lines_to_check for number in number_line]
            star_spans = [self.get_increased_span(star.span()) for star in stars]
            gears_stars = [star for star in star_spans if self.is_gear(star, numbers_to_check)]
            gears += [self.get_overlapping_numbers(star, numbers_to_check) for star in gears_stars]

        gear_sum = sum(map(lambda x: int(x[0][0])*int(x[1][0]), gears))
        return gear_sum

    def task1(self, task_input):
        lines = task_input.split("\n")
        part_numbers = []

        for line_nr, line in enumerate(lines):
            lines_to_check = lines[max(line_nr-1, 0):min(line_nr+2, len(lines))]
            numbers = list(re.finditer(self.number_pattern, line))
            part_numbers += [int(number[0]) for number in numbers if self.is_part_number(number, lines_to_check)]
            
        return sum(part_numbers)
    