import curses

class Table:
    def __init__(self):
        self.pieces = [
            ['r','n','b','q','k','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R']
        ]

    def str_table(self):
        table_str = ''
        for r in range(9):
            if not r:
                for c in range(9):
                    if not c:
                        table_str += '   '
                    else:
                        table_str += f' {c} '
            else:
                for c in range(9):
                    if not c:
                        table_str += f' {chr(64+r)} '
                    else:
                        table_str += f'[{self.pieces[r-1][c-1]}]'
            table_str += '\n'
        return table_str

    def move_piece(self, start_pos, end_pos):
        if isinstance(start_pos, str):
            start_pos = start_pos.upper()
            s_r = int(ord(start_pos[0]))-65
            s_c = int(start_pos[1])-1
        if isinstance(end_pos, str):
            end_pos = end_pos.upper()
            e_r = int(ord(end_pos[0]))-65
            e_c = int(end_pos[1])-1
        
        p = self.pieces[s_r][s_c]
        self.pieces[s_r][s_c] = ' '
        self.pieces[e_r][e_c] = p

def main(scr):
    h, w = scr.getmaxyx()
    
    scr.clear()
    # curses.resizeterm(10, 10*3)
    # h = 10
    # w = 30
    str_table = table.str_table()
    for i, l in enumerate(str_table.split('\n')):
        r = (h - 9)//2 + i
        c = (w - 9)//2
        scr.addstr(r, c, l)
    scr.refresh()
    scr.getch()

if __name__ == "__main__":
    global table
    table = Table()
    curses.wrapper(main)