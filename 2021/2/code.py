def get_commands(file_name):
    return [ command.split(" ") for command in open(file_name).read().split("\n")[:-1]]

def process_commands_part1(commands):
    forward = 0
    depth = 0
    depth_v2 = 0
    aim = 0
    for command, units in commands:
        units=int(units)
        if command == "forward":
            forward+=units
            depth_v2+=aim*units
        elif command == "up":
            aim-=units
        elif command == "down":
            aim+=units
        else:
            print(f"unknown command: {command}")
    depth = aim
    return forward, depth, depth_v2

data_file = "input1.txt"
commands = get_commands(data_file)
forward, depth, depth_v2 = process_commands_part1(commands)
print(f"forward: {forward}, depth: {depth}, depth_v2: {depth_v2}")
print(f"part 1: {depth*forward}")
print(f"part 2: {forward*depth_v2}")
