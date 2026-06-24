import argparse
import sys
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# --- Dazai's Personal Detective Aesthetic ---
TRENCH_BROWN = "\033[38;5;137m"     # Detective Trench Coat Brown
BANDAGE_WHITE = "\033[38;5;253m"    # Crisp White Bandages
SUICIDE_BLUE = "\033[38;5;24m"      # Deep Melancholic River Blue
DETECTIVE_GRAY = "\033[38;5;244m"   # Apathetic Office Gray
RESET = "\033[0m"
BOLD = "\033[1m"

def print_banner():
    print(f"""{TRENCH_BROWN}{BOLD}
    ┌────────────────────────────────────────────────────────┐
    │  [🩹]  NO LONGER HUMAN: DYNAMIC FILE STAGER            │
    │      "Move your data cleanly through the background"   │
    └────────────────────────────────────────────────────────┘{RESET}""")

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="Osamu Dazai's Standalone FTP Stager")
    parser.add_argument("-p", "--port", type=int, default=2121, help="Port to bind the server to (Default: 2121)")
    parser.add_argument("-d", "--directory", default=".", help="Directory to share over FTP (Default: current directory)")
    parser.add_argument("--anonymous", action="store_true", help="Enable complete anonymous read/write access")
    args = parser.parse_args()

    # Normalize the sharing directory pathway
    abs_share_dir = os.path.abspath(args.directory)
    
    # Initialize the user authorization engine
    authorizer = DummyAuthorizer()

    if args.anonymous:
        print(f"{SUICIDE_BLUE}[!] Note: Opening anonymous channels. Full Read/Write access granted.{RESET}")
        # 'elradfmwMT' permissions grant absolute read, write, and directory traversal permissions
        authorizer.add_anonymous(abs_share_dir, perm='elradfmwMT')
    else:
        # Default authenticated access for structured operations
        username = "dazai"
        password = "det-agency-password"
        print(f"{DETECTIVE_GRAY}[*] Enforcing secure credentials -> User: {username} | Pass: {password}{RESET}")
        authorizer.add_user(username, password, abs_share_dir, perm='elradfmwMT')

    # Bind the handler to our custom authorizer
    handler = FTPHandler
    handler.authorizer = authorizer
    
    # Customize the FTP banner presented to target machines connecting to us
    handler.banner = "No Longer Human Staging Node - Let us move data effortlessly."

    # Fire up the staging machine on all local network interfaces
    address = ('0.0.0.0', args.port)
    server = FTPServer(address, handler)

    # Set maximum connection parameters for fast multi-session exam situations
    server.max_cons = 256
    server.max_cons_per_ip = 10

    print(f"{TRENCH_BROWN}{BOLD}[+] Staging node active! Root Directory: {abs_share_dir}{RESET}")
    print(f"{BANDAGE_WHITE}[*] Listening for incoming data loops on port {args.port}... Close with Ctrl+C{RESET}\n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{DETECTIVE_GRAY}[*] Tearing down file infrastructure. Dazai stager deactivated.{RESET}")

if __name__ == "__main__":
    main()
