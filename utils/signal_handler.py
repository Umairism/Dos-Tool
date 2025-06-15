import signal
import sys
from colorama import Fore

def setup_signal_handler(stop_event, all_threads=None):
    def handle(sig, frame):
        print(Fore.RED + "\n[!] SIGINT received. Stopping attack gracefully...")
        stop_event.set()
        if all_threads:
            for t in all_threads:
                t.join()
        print(Fore.YELLOW + "\n[✓] Attack stopped.")
        sys.exit(0)

    signal.signal(signal.SIGINT, handle)
