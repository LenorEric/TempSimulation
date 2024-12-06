prog_bk = 0
import sys

def progress_bar(prog):
    global prog_bk
    prog = round(prog)
    if prog != prog_bk:
        sys.stdout.flush()
        prog_bk = prog
        print("\r", end="")
        print("Calc progress: {}%: ".format(prog), "▋" * (prog // 2), end="")