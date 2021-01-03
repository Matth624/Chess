class Table:
    def __init__(self):
        self.pieces = [
            '♖♘♗♔♕♗♘♖',
            '♙♙♙♙♙♙♙♙',
            '        ',
            '        ',
            '        ',
            '        ',
            '♟♟♟♟♟♟♟♟',
            '♜♞♝♚♛♝♞♜'
        ]

        self.draw()

    def draw(self):
        for r in range(9):
            if not r:
                for c in range(9):
                    if not c:
                        print('   ', end='')
                    else:
                        print(f' {c} ', end='')
            else:
                for c in range(9):
                    if not c:
                        print(f' {chr(64+r)} ', end='')
                    else:
                        print(f'[{self.pieces[r-1][c-1]}]', end='')
            print('')


if __name__ == "__main__":
    table = Table()