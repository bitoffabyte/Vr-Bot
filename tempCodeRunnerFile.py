        finally:
            #Close down curses properly, inc turn echo back on!
            curses.nocbreak(); screen.keypad(0); curses.echo()
            curses.endwin()
            # GPIO.cleanup()