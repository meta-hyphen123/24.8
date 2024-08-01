import os
import sys
import socket
import time
from attacks import *

# Main function
def main():
    print("Welcome to 🌲 Shitersploit!")

    while True:
        print("1. Exploit vulnerabilities")
        print("2. Deliver payloads")
        print("3. Social engineering")
        print("4. Command and control")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            target = input("Enter the target: ")
            exploit(target)
        elif choice == "2":
            target = input("Enter the target: ")
            payload = input("Enter the payload: ")
            deliver_payload(target, payload)
        elif choice == "3":
            target = input("Enter the target: ")
            social_engineering(target)
        elif choice == "4":
            command_and_control()
        elif choice == "5":
            print("Exiting 🌲 Shitersploit...")
            break
        else:
            print("Invalid choice. Try again.")

# Entry point
if __name__ == "__main__":
    main()