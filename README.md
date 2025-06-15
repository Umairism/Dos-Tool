# Whistler - DDoS Simulation CLI Tool

Whistler is a command-line tool for simulating DDoS (Distributed Denial of Service) attacks for educational and testing purposes. It provides two main attack types: SYN Flood (for local network testing) and HTTP GET Flood (for websites). The tool is modular, supports multi-threading, and includes logging and graceful shutdown.

## Features

- **SYN Flood**: Simulate TCP SYN packet floods to a target IP and port.
- **HTTP GET Flood**: Simulate HTTP GET request floods to a target URL.
- **Multi-threaded**: Launch multiple attack threads for higher throughput.
- **Logging**: Optional logging of attack details and summaries.
- **Graceful Shutdown**: Handles Ctrl+C (SIGINT) to stop attacks cleanly.
- **Statistics**: Displays summary of attack duration, threads, and request/packet counts.
- **Colorful CLI**: Uses colorama for colored terminal output.

## Requirements

- Python 3.7+
- [colorama](https://pypi.org/project/colorama/)
- Works on Windows, Linux, and macOS (for HTTP flood; SYN flood may require admin/root privileges)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Umairism/Dos-Tool.git
   cd dos-tool
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

   *Or manually:*
   ```sh
   pip install colorama
   ```

## Usage

You can run Whistler in two ways: **command-line arguments** or **interactive mode**.

### Command-Line Arguments

```sh
python main.py --attack-type syn --ip <TARGET_IP> --port <PORT> --duration <SECONDS> --threads <COUNT> [--log <LOG_PATH>]
python main.py --attack-type http --url <TARGET_URL> --duration <SECONDS> --threads <COUNT> [--log <LOG_PATH>]
```

**Examples:**
- SYN Flood:  
  `python main.py --attack-type syn --ip 192.168.1.10 --port 80 --duration 30 --threads 10`
- HTTP GET Flood:  
  `python main.py --attack-type http --url http://example.com --duration 30 --threads 10 --log attack.log`

### Interactive Mode

Simply run:
```sh
python main.py
```
You will be prompted to select the attack type and enter parameters interactively.

## Command-Line Arguments

| Argument         | Description                                 | Required for SYN | Required for HTTP |
|------------------|---------------------------------------------|:---------------:|:-----------------:|
| `--attack-type`  | Attack type: `syn` or `http`                | Yes             | Yes               |
| `--ip`           | Target IP address                           | Yes             | No                |
| `--port`         | Target port                                 | Yes             | No                |
| `--url`          | Target URL (http:// or https://)            | No              | Yes               |
| `--duration`     | Attack duration in seconds                  | Yes             | Yes               |
| `--threads`      | Number of threads to use                    | Yes             | Yes               |
| `--log`          | Path to log file (optional)                 | No              | No                |

## Project Structure

```
dos-tool/
│
├── main.py                # Main CLI entry point
├── cli/
│   └── arguments.py       # Argument parsing utilities
├── core/
│   ├── syn_flood.py       # SYN flood attack logic
│   └── http_flood.py      # HTTP GET flood logic
├── utils/
│   ├── banner.py          # CLI banner display
│   ├── signal_handler.py  # Signal handling for graceful shutdown
│   └── logger.py          # Logging setup
└── README.md
```

## Notes

- **Legal Warning:** This tool is for educational and authorized testing only. Do not use it against systems you do not own or have explicit permission to test.
- **SYN Flood** may require administrative/root privileges.
- **Logging** is optional and can be enabled with the `--log` argument.

## License

MIT License. See [LICENSE](LICENSE) for details.
