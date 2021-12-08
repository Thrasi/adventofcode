def get_line_segments(file_name):
    lines = open(file_name).readlines()
    return [ [list(map(int,point.split(",")))
              for point in line.split(" -> ")]
             for line in lines]

def is_straight(segment):
    [[x1,y1],[x2,y2]] = segment
    return x1 == x2 or y1 == y2

def get_points_in_segment(segment):
    points = set(map(str,segment))
    dx = 1
    [[x1,y1],[x2,y2]] = segment

    while x1 != x2 or y1 != y2:
        if x1 != x2:
            x1+=int((x2-x1)/abs(x2-x1))
        if y1 != y2:
            y1+=int((y2-y1)/abs(y2-y1))

        points.add(str([x1,y1]))

    return points

segments = get_line_segments("input.txt")
#segments = list(filter(is_straight, segments))  ## used for part1

### Inefficient: 
sorted_segments = [sorted(segment) for segment in segments]

from collections import defaultdict
counts = defaultdict(lambda: 0)
for segment in sorted_segments:
    for point in get_points_in_segment(segment):
        counts[point]+=1

intersection_count = len([item for item in counts.items() if item[1]>=2])
print(f"points where at least 2 intersect: {intersection_count}")
