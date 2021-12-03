from functools import reduce

def get_inputs(file_name):
    inputs = open("input.txt").read().split("\n")[:-1]
    return [ list(map(int,[b for b in bits])) for bits in inputs ]
    
def add_elementwise(l1, l2):
   return map(sum,zip(l1, l2))

def get_most_common_bit_values(report):
    summed_values = reduce(add_elementwise, report)
    return [ int(i >= len(report)/2) for i in summed_values ]

def get_least_common_bit_values(report):
    summed_values = reduce(add_elementwise, report)
    return [ int(i < len(report)/2) for i in summed_values ]

def filter_by_bits(report, bit_filter_func):
    report =  [i[:] for i in diagnostic_report]
    for i in range(len(report[0])):
        bit_filter_values = bit_filter_func(report)
        report = [ number for number in report if number[i]==bit_filter_values[i]]
        if len(report)==1:
            break
    return report

def list_of_bits_to_int(arr):
    return int("".join(map(str, arr)),2)

input_file = "input.txt"
diagnostic_report = get_inputs(input_file)

binary_gamma = get_most_common_bit_values(diagnostic_report)
binary_epsilon = [ abs(b-1) for b in binary_gamma ]

gamma_rate = list_of_bits_to_int(binary_gamma)
epsilon_rate = list_of_bits_to_int(binary_epsilon)

print(f"Gamma rate: {gamma_rate}")
print(f"Epsilon rate: {epsilon_rate}")
print(f"Power consumption: {gamma_rate*epsilon_rate}")

report =  [i[:] for i in diagnostic_report]
[binary_oxygen_generator_rating] = filter_by_bits(report, get_most_common_bit_values)
oxygen_generator_rating = list_of_bits_to_int(binary_oxygen_generator_rating)
print(f"oxygen_generator_rating: {oxygen_generator_rating}")

report =  [i[:] for i in diagnostic_report]
[binary_CO2_crubber_rating] = filter_by_bits(report, get_least_common_bit_values)
CO2_scrubber_rating = list_of_bits_to_int(binary_CO2_crubber_rating)
print(f"CO2_scrubber_rating: {CO2_scrubber_rating}")
print(f"life support rating: {oxygen_generator_rating*CO2_scrubber_rating}")
