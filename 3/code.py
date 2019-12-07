wire2="R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
wire1="U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
w1=wire1.split(',')
w2=wire2.split(',')

def get_segment(start, command):
    moves = range(int(command[1:])+1)
    if command[0] == "U":
        return [(start[0],start[1]+i) for i in moves]
    if command[0] == "D":
        return [(start[0],start[1]-i) for i in moves]
    if command[0] == "L":
        return [(start[0]-i,start[1]) for i in moves]
    if command[0] == "R":
        return [(start[0]+i,start[1]) for i in moves]

def get_segments_from_wire(wire):
    points = []#set()
    start = (0,0)
    #print wire
    for command in wire:
        #print command
        segment = get_segment(start, command)
        #points.update(set(segment))
        points+=segment
        start = segment[-1]
    return points

def manhattan_distance(point):
    return sum(map(abs,point))

with open("input.txt","r") as f:
    #[w1,w2] = f.readlines()
    w2="R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    w1="U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

    p1 = get_segments_from_wire(w1.split(','))
    p2 = get_segments_from_wire(w2.split(','))
    #p1.remove((0,0))
    intersections = set(p1[1:]).intersection(set(p2))
    #intersections = p1.intersection(p2)
    #print intersections
    print min(map(manhattan_distance, intersections))

    total_steps = 0
    for i, step in enumerate(p1,1):
        if step in intersections:
            total_steps+=i
            break
    for i, step in enumerate(p2):
        if step in intersections:
            total_steps+=i
            break
    print total_steps
