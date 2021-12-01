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
    points = []
    start = (0,0)
    for command in wire:
        segment = get_segment(start, command)
        points+=segment[1:]
        start = segment[-1]
    return points

def manhattan_distance(point):
    return sum(map(abs,point))

with open("input.txt","r") as f:
    [w1,w2] = f.readlines()
    p1 = get_segments_from_wire(w1.split(','))
    p2 = get_segments_from_wire(w2.split(','))
    intersections = set(p1).intersection(set(p2))
    print min(map(manhattan_distance, intersections))

    total_steps = 0
    intersection_steps={}
    for i, step in enumerate(p1,1):
        if step in intersections:
            intersection_steps[step] = i
    for i, step in enumerate(p2,1):
        if step in intersections:
            intersection_steps[step]+=i
    print min(intersection_steps.values())

