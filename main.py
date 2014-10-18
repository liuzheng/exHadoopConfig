# coding=utf-8
__author__ = 'liuzheng'


def main():
    print "heoo"
    stdscr = curses.initscr()

def ccc():
    import curses

    myscreen = curses.initscr()

    myscreen.border(0)
    myscreen.addstr(12, 25, "Python curses in action!")
    myscreen.refresh()
    myscreen.getch()

    curses.endwin()

def npy():
    import npyscreen



if __name__=='__main__':
    ccc()
    # npy()