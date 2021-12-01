def process(program):
    for x in range(0,len(program),4):
        if program[x] == 99:
            return program
        else:
            [op, i, j, k] = program[x:x+4]
            program[k] = program[i] + program[j] if op == 1 else program[i] * program[j] 

with open('input.txt','r') as f:
    orig_program = map(int, f.readlines()[0].split(','))
    program = orig_program[:]
    program[1]=12
    program[2]=2
    print process(program)

    inputs = [(x, y) for x in xrange(100) for y in xrange(100)]
    for noun, verb in inputs:
        program = orig_program[:]
        program[1]=noun
        program[2]=verb
        result = process(program)[0]
        if result == 19690720:
            print 100 * noun + verb, result

            
