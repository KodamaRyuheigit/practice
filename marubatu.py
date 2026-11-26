def creat_map():
    return
    [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "],
    ]
def display_map(map):
    for i in range(3):
        print('|'.join(map[i]))
        print("------------")

def player1_input():
    A, B = map(int, input("置きたい場所を指定してください" \
        "例：1 1").split())
    return A,B,"o"

def player2_input():
    A, B = map(int, input("置きたい場所を指定してください" \
        "例：1 1").split())
    return A,B,"x"

def update_map(map,A,B,symbol):
    map[A][B] = symbol
    
def main():
    map=creat_map()
    display_map(map)
    while True:
        player1_input()
    