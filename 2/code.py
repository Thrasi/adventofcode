def process(program):
    for x in range(0,len(program),4):
        if program[x] == 99:
            return program
        else:
            [op, i, j, k] = program[x:x+4]
            program[k] = program[i] + program[j] if op == 1 else program[i] * program[j] 

with open('input.txt','r') as f:
    program = map(int, f.readlines()[0].split(','))
    program[1]=12
    program[2]=2
    print process(program)
