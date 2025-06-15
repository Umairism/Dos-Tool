
import argparse
import os
from datetime import datetime

def get_default_log_path():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return os.path.join("logs", f"whistler_{timestamp}.log")

def parse_args():
    parser = argparse.ArgumentParser(description="Whistler v0.3 - DDoS Simulation CLI Tool")

    parser.add_argument("-t", "--attack-type", choices=["syn", "http"], help="Type of attack (syn or http)")
    parser.add_argument("--ip", help="Target IP address (required for SYN flood)")
    parser.add_argument("--port", type=int, help="Target port (required for SYN flood)")
    parser.add_argument("--url", help="Target URL (required for HTTP GET flood)")
    parser.add_argument("-th", "--threads", type=int, required=True, help="Number of threads")
    parser.add_argument("-d", "--duration", type=int, required=True, help="Duration of attack in seconds")
    parser.add_argument("--log", nargs="?", const=True, default=None, help="Enable logging (optional path)")

    return parser.parse_args()









# import argparse

# def get_arguments():
#     parser = argparse.ArgumentParser(
#         description="Whistler v0.3 - DDoS Simulation CLI Tool",
#         formatter_class=argparse.ArgumentDefaultsHelpFormatter
#     )

#     parser.add_argument(
#         "-t", "--type",
#         dest="attack_type",
#         choices=["syn", "http"],
#         required=False,
#         help="Type of attack: 'syn' or 'http'"
#     )

#     parser.add_argument("--ip", help="Target IP address (required for SYN flood)")
#     parser.add_argument("--port", type=int, help="Target port (required for SYN flood)")
#     parser.add_argument("--url", help="Target URL (required for HTTP flood)")

#     parser.add_argument(
#         "-th", "--threads",
#         type=int,
#         required=True,
#         help="Number of threads to use"
#     )

#     parser.add_argument(
#         "-d", "--duration",
#         type=int,
#         required=True,
#         help="Attack duration in seconds"
#     )

#     parser.add_argument(
#         "--log",
#         dest="log_path",
#         help="Path to save log output (optional)"
#     )

#     return parser.parse_args()
