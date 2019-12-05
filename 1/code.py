with open('input.txt','r') as f:
    print sum([ int(int(mass) / 3.) - 2 for mass in f.readlines()])
    
