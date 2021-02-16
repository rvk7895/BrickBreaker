import termios
import sys
import tty
import signal
from time import sleep

class Input:
    def _get_key_raw(self):
        fd = sys.stdin.fileno()
        self.old_config = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.buffer.raw.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, self.old_config)
        return ch
    
    def _timeout_handler(self, signum, frame):
        raise TimeoutError
    
    def get_parsed_input(self, timeout=0.1):
        signal.signal(signal.SIGALRM, self._timeout_handler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            ip = self._get_key_raw()
            signal.alarm(0)
            if ip == b'\x03':
                text = 'quit'
            elif ip == b'\x1b[D' or ip == b'a':
                text = 'a'
            elif ip == b'\x1b[C' or ip == b'd':
                text = 'd'
            elif ip == b' ':
                text = 'space'
            elif ip == b'\r':
                text = 'enter'
            elif ip == b'q':
                text = 'q'
            else:
                text = 'none'
            sleep(timeout)
            return text
        except TimeoutError:
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return None