def get_windows(input_list, window_size=1):
    return [input_list[i:i+window_size] for i in range(0,len(input_list))
            if len(input_list[i:i+window_size]) == window_size]

def count_increases(depths):
    increases = 0
    for i in range(len(depths)-1):
        if depths[i+1]-depths[i] > 0:
            increases+=1
    return increases

for data_file, window_size in [("test-input.txt",1), ("input.txt",1), ("test-input-2.txt",3), ("input-2.txt",3)]:
    raw_depths = list(map(int, open(data_file).read().split("\n")[:-1]))
    depths = [sum(depth) for depth in get_windows(raw_depths, window_size)]
    print(f"""{data_file} has {count_increases(depths)} increases using window_size {window_size}""")
