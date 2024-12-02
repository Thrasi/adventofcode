import re

class Day5:
    def __init__(self):
        pass

    def map(self, x, mapping_rules):
        for rule in mapping_rules:
            if x >= rule[1] and x < rule[1] + rule[2]:
                return x + (rule[0] - rule[1])
        return x
    
    
    def map_range(self, input_range, mapping_rules):
        output_ranges = []
        (x1, x2) = input_range
        
        for rule in mapping_rules:
            print()
            print(f"rule: {rule}")
            print(f"x1: {x1}, x2: {x2}")
            rule_x1, rule_x2 = rule[1], rule[1] + rule[2]
            if x2 < rule_x1 or x1 > rule_x2: # no overlap
                print("no overlap")
                continue
            elif x1 >= rule_x1 and x2 < rule_x2: # input range is completely within rule range
                print("input range is completely within rule range")
                output_ranges.append([self.map(x1, [rule]), self.map(x2, [rule])])
            elif x1 < rule_x1:
                print("x1 < rule_x1")
                output_ranges.append([x1, rule_x1 - 1])
                x1 = rule_x1
            if x2 < rule_x2:
                print("x2 <= rule_x2")
                output_ranges.append([self.map(x1, [rule]), self.map(x2 - 1, [rule])])
                print(f"output_ranges: {output_ranges}")
            elif x2 >= rule_x2:
                print("x2 >= rule_x2")
                output_ranges.append([self.map(x1, [rule]), self.map(rule_x2 - 1, [rule])])
                print(f"output_ranges: {output_ranges}")
                x1 = rule_x2
                    
            # elif x1 >= rule_x1:
            #     print("x1 >= rule_x1")
            #     if x2 < rule_x2:
            #         print("x2 < rule_x2")
            #         output_ranges.append([self.map(x1, [rule]), self.map(x2 - 1, [rule])])
            #         print(f"output_ranges: {output_ranges}")
            #     elif x2 >= rule_x2:
            #         print("x2 >= rule_x2")
            #         output_ranges.append([self.map(x1, [rule]), self.map(rule_x2 - 1, [rule])])
            #         print(f"output_ranges: {output_ranges}")
            #         x1 = rule_x2
        
        print(f"x1: {x1}, x2: {x2}")
        print(f"output_ranges: {output_ranges}")
        output_ranges.append([x1, x2])
        return output_ranges
    
    
    def get_mappings(self, task_input):
        mappings = task_input.split(":\n")[1:]
        mappings = [mapping.split("\n")[:-2] for mapping in mappings]
        mappings = [[list(map(int, map_row.split())) for map_row in mapping] for mapping in mappings ]
        return [sorted(mapping, key=lambda x: x[1]) for mapping in mappings]

    def task1(self, task_input):
        lines = task_input.split("\n")
        mapping_seeds = list(map(int, lines[0].split()[1:]))
        mappings = self.get_mappings(task_input)
        

        for i, mapping in enumerate(mappings):
            mapping_seeds = [self.map(seed, mapping) for seed in mapping_seeds]

        return min(mapping_seeds)
    
    def task2(self, task_input):
        lines = task_input.split("\n")
        seed_starts = list(map(int, lines[0].split()[1::2]))
        intervals = list(map(int, lines[0].split()[2::2]))
        print(seed_starts)
        print(intervals)
        
        seed_intervals = [[start, start + length - 1] for (start, length) in list(zip(seed_starts, intervals))]
        mappings = self.get_mappings(task_input)
        print(seed_intervals)
        mapped_intervals = []
        intervals_to_map = seed_intervals[:]
        for interval in seed_intervals:
            intervals_before_mapping = [interval]
            for i, mapping in enumerate(mappings):
                intervals_after_mapping = []
                for inter in intervals_before_mapping:
                    intervals_after_mapping += self.map_range(inter, mapping)
                print(f"intervals_after_mapping {i}: {intervals_after_mapping}")
                intervals_before_mapping = intervals_after_mapping[:]
            mapped_intervals += intervals_after_mapping
        print()
        print(mapped_intervals[:10])
        a=sorted(mapped_intervals[:10], key=lambda x: x[0])
        min([interval[0] for interval in mapped_intervals])
        print(a)
                
        return min([interval[0] for interval in mapped_intervals])
