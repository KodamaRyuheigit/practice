def create_boad():
    return[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "],
    ]
def display_boad(boad):
    for i in range(3):
        print('|'.join(boad[i]))
        print("------")

def player1_input(boad):
    while True:
        A, B = map(int, input("置きたい場所を指定してください").split())
        if 0<= A <=2 and 0<= B <=2:
            if boad[A][B]==" ":
                return A,B,"o"
            else:
                print("ここには置けません")
        else:
            print("範囲外です")

def player2_input(boad):
    while True:
        A, B = map(int, input("置きたい場所を指定してください").split())
        if 0<= A <=2 and 0<= B <=2:
            if boad[A][B]==" ":
                return A,B,"x"
            else:
                print("ここには置けません")
        else:
            print("範囲外です")

def update_boad(boad,A,B,symbol):
    boad[A][B] = symbol

def player1_win(boad)->bool:
    for i in range(3):
        if boad[i] == ["o","o","o"]:
            return True
    for i in range(3):
        if boad[0][i]==boad[1][i]==boad[2][i]=="o":
            return True
    if boad[0][0]==boad[1][1]==boad[2][2]=="o":
        return True
    if boad[0][2]==boad[1][1]==boad[2][0]=="o":
        return True
    return False

def player2_win(boad)->bool:
    for i in range(3):
        if boad[i] == ["x","x","x"]:
            return True
    for i in range(3):
        if boad[0][i]==boad[1][i]==boad[2][i]=="x":
            return True
    if boad[0][0]==boad[1][1]==boad[2][2]=="x":
        return True
    if boad[0][2]==boad[1][1]==boad[2][0]=="x":
        return True
    return False

def check_draw(boad)->bool:
    for i in range(3):
        for j in range(3):
            if boad[i][j]=="o" or boad[i][j] =="x":
                pass
            else:
                return False
    return True

def main():
    boad=create_boad()
    display_boad(boad)
    while True:
        A,B,symbol=player1_input(boad)
        update_boad(boad,A,B,symbol)
        display_boad(boad)
        if player1_win(boad):
            print("Player1 Win")
            break
        if check_draw(boad):
            print("draw")
            break
        A,B,symbol=player2_input(boad)
        update_boad(boad,A,B,symbol)
        display_boad(boad)
        if player2_win(boad):
            print("Player2 Win")
            break  
        if check_draw(boad):
            print("draw")
            break
    
if __name__ == "__main__":
    main()


    