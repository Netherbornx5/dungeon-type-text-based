import curses
from curses.textpad import rectangle


def main(stdscr):
    global new_head
    curses.curs_set(0)

    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_RED)
    RED_AND_CYAN = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(3)
    LAVA_LAVA_LAVA = curses.color_pair(2)

    sh, sw = stdscr.getmaxyx()
    box = [[3, 3], [sh - 15, sw - 105]]
    death_box = [[2, 2], [sh - 14, sw - 104]]

    stdscr.attron(GREEN_AND_BLACK)
    rectangle(stdscr, 3, 3, 15, 15)
    stdscr.attroff(GREEN_AND_BLACK)
    stdscr.attron(LAVA_LAVA_LAVA)
    rectangle(stdscr, 2, 2, 16, 16)
    stdscr.attroff(LAVA_LAVA_LAVA)

    snake =[[(sh//10)+1, (sw//10)-7]]
    direction = curses.KEY_RIGHT
    for y, x in snake:
        stdscr.addstr(y, x, "H")

    #box2 = [[14, 4], [sh - 15, sw - 70]]

    ablock = [[(sh//10)+11, (sw//10)-7]]
    for y, x in ablock:
        stdscr.addstr(y, x, "I")

    bblock = [[(sh // 10) + 11, (sw // 10) - 5]]
    for y, x in bblock:
        stdscr.addstr(y, x, "P")

    running = True

    dmg = 10

    while (running):

        key = stdscr.getch()

        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = key

            head = snake[0]

            if direction == curses.KEY_RIGHT:
                new_head = [head[0], head[1] + 1]
            if direction == curses.KEY_LEFT:
                new_head = [head[0], head[1] - 1]
            if direction == curses.KEY_UP:
                new_head = [head[0] - 1, head[1]]
            if direction == curses.KEY_DOWN:
                new_head = [head[0] + 1, head[1]]

            snake.insert(0, new_head)
            stdscr.addstr(new_head[0], new_head[1], "H")

            stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()
            if (snake[0][0] in [box[0][0], box[1][0]] or
                snake[0][1] in [box[0][1], box[1][1]] or
                snake[0] in snake[1:]):
                stdscr.nodelay(0)
                stdscr.getch()
                stdscr.refresh()

            #if snake.y == bblock.y and snake.x ==bblock.x:
            #    dmg += 10
            #    stdscr.addstr(sh // 2 + 2, sw // 2 - 23 // 2, "You got the Phoenix Blade! That does 10 damage!", RED_AND_CYAN)

            duh = True

            if (snake[0][0] in [death_box[0][0], death_box[1][0]] or
                snake[0][1] in [death_box[0][1], death_box[1][1]] or
                snake[0] in snake[1:]):
                duh = False
                msg = "GAME OVER!!!"
                stdscr.addstr(sh // 2 - 2, sw // 2 - len(msg) // 2, msg)
                stdscr.nodelay(0)
                stdscr.getch()
                break
            if (running) and duh == True:
                msg = "P=Pheonix blade, " \
                      "W=Wizard stone, " \
                      "S=Spellbook, " \
                      "H=Hero," \
                      "V=Villain, " \
                      "E=Enemy, " \
                      "B=boss"
                stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)

            stdscr.refresh()

curses.wrapper(main)
