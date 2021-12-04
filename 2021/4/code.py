class BingoBoard():
    def __init__(self, board):
        self.board = board

    def mark(self, number):
        for row in self.board:
            for column in range(len(row)):
                if row[column]==number:
                    row[column]= -row[column]-1
                    return self.bingo(row, column)

    def bingo(self, row, column):
        return max(row) < 0 or max([ r[column] for r in self.board]) < 0

    def score(self, number):
        return sum([ column for row in self.board for column in row if column >= 0])*number

    def __str__(self):
        string = ""
        for row in self.board:
            string+=str(row)+"\n"
        return string

def get_inputs(file_name):
    lines = open(file_name).readlines()
    drawn_numbers = list(map(int,lines[0].split(",")))
    boards = [ BingoBoard([list(map(int,line.split(" "))) for line in lines[x:x+5]]) for x in range(2,len(lines),6)]
    return drawn_numbers, boards

def play_bingo(numbers, boards):
    winners = set()
    place = 1
    for number in numbers:
        print(number)
        for board in boards:
            if board.mark(number):
                print(f"BINGO!\n{place}. place got a score of: {board.score(number)}")
                print(board)
                winners.add(board)
                place+=1
        if winners:
            boards = list(set(boards)-winners)
            winners = set()
            if len(boards) == 0:
                return

file_name = "input.txt"
numbers, bingo_boards = get_inputs(file_name)
play_bingo(numbers, bingo_boards)
