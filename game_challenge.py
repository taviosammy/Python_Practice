
# This is the simulation of a game made up of black and white pieces represented by w and b.
#Two players will take turns removing their designated piece.
#A player may remove 1 piece per turn, given that piece is between two pieces of the same color.
#The winner is decided once one player has no more available moves, then their opponent wins.
#White always plays first

#eg. If colors = "bwwwb", and  it is white's turn, white will remove the middle piece, leaving 
#colors = 'bwwb'. It is then Black's turn but since there are no moves, white wins


colors = input("Enter a sequence of 'w' and 'b' to similuta game starting point n\ eg. 'wwwwwbbbbbbbwwwwwbbbww' ")

def game(colors):
    player = 'wendy'
    outcome = 'continue'

    while outcome == 'continue':


        if player == 'wendy':
            if 'www' in colors:
                colors = colors.replace('www','ww',1)

                player = 'bob'

            else: 
                outcome ='bob wins'

        elif player == 'bob':
            if 'bbb' in colors:
                colors = colors.replace('bbb','bb',1)

                player = 'wendy'
            else:
                outcome = 'wendy wins'
    print(outcome)


game(colors)


        