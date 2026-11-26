def creat_map():
    return[
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

def player1_win(map)->bool:
    for i in range(3):
        if map[i] == ["o","o","o"]:
            return True
    for i in range(3):
        if map[0][i]==map[1][i]==map[2][i]=="o":
            return True
    if map[0][0]==map[1][1]==map[2][2]=="o":
        return True
    if map[0][2]==map[1][1]==map[2][0]=="o":
        return True
    return False

def player2_win(map)->bool:
    for i in range(3):
        if map[i] == ["x","x","x"]:
            return True
    for i in range(3):
        if map[0][i]==map[1][i]==map[2][i]=="x":
            return True
    if map[0][0]==map[1][1]==map[2][2]=="x":
        return True
    if map[0][2]==map[1][1]==map[2][0]=="x":
        return True
    return False

def main():
    map=creat_map()
    display_map(map)
    for i in range(9):
        A,B,symbol=player1_input()
        update_map(map,A,B,symbol)
        display_map(map)
        if player1_win(map):
            print("Player1 Win")
            break
        A,B,symbol=player2_input()
        update_map(map,A,B,symbol)
        display_map(map)
        if player2_win(map):
             print("Player2 Win")
             break  
    else:
        display_map(map)
        print("draw")

if __name__ == "__main__":
    main()


    