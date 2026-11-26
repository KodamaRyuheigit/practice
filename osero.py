def creat_map():
    map = [["   " for i in range(8)] for i in range(8)]
    map[3][3]=" o "
    map[4][4]=" o "
    map[3][4]= " x "
    map[4][3]= " x "
    return map
def display_map(map):
    for i in range(8):
        print('|'.join(map[i]))
        print("-------------------------------")

def player1_input():
    A, B = map(int, input("Player1:").split())
    return A,B," o "

def player2_input():
    A, B = map(int, input("Player2:").split())
    return A,B," x "

def can_place(map,A,B,symbol):
def main():
    map = creat_map()
    display_map(map)

if __name__ == "__main__":
    main()