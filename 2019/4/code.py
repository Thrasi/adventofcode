import re
def has_adjacent_pair(number):
    return True if re.search(r'(\d)\1', str(number)) else False

def never_decreases(number):
    number_list = [n for n in str(number)]
    return number_list == sorted(number_list)
        
def fulfills_facts(number):
    return has_adjacent_pair(number) and never_decreases(number) 

passwords = range(254032,789861) 
possible_passwords = [p for p in passwords if fulfills_facts(p)]
print len(possible_passwords)
def stricter_pair(number):
    return False if re.search(r'(\d)\1\1', str(number)) else True


# possible_password contain pairs and are monotonously increasing
# if the password still fulfills adjacency with sequences longer than 2 removed, it is correct
pp = [ p for p in possible_passwords if has_adjacent_pair(re.sub(r'([0-9])\1{2,}','',str(p))) ]
print len(pp)
