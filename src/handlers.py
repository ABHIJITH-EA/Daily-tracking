import signal

def ctrl_c(signum, frame):
    print("CTRL_C Can't process")


def init_handlers():
    signal.signal(signal.SIGINT, ctrl_c)