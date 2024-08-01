import cmd
import telnetlib

class ShiterTelnetShell(cmd.Cmd):
    prompt = 'Shiter Telnet> '
    intro = "Welcome to Shiter Telnet Client\nEscape character is 'CTRL+]'\n"

    def do_open(self, arg):
        """Connect to a host (default port is 23). Usage: open hostname [port]"""
        args = arg.split()
        hostname = args[0]
        port = int(args[1]) if len(args) > 1 else 23
        try:
            self.tn = telnetlib.Telnet(hostname, port)
            print(f"Connected to {hostname}:{port}")
        except Exception as e:
            print("Error:", e)

    def do_send(self, arg):
        """Send a string to the server"""
        if hasattr(self, 'tn'):
            self.tn.write(arg.encode('utf-8') + b"\n")
            output = self.tn.read_until(b"Shiter Telnet> ").decode('utf-8')
            print(output, end='')
        else:
            print("Error: Not connected to a host. Use 'open' command to connect.")

    def do_close(self, arg):
        """Close the current connection"""
        if hasattr(self, 'tn'):
            self.tn.close()
            del self.tn
            print("Connection closed.")
        else:
            print("Error: Not connected to a host.")

    def do_quit(self, arg):
        """Exit the telnet client"""
        print("Exiting Shiter Telnet Client.")
        return True

    def help_help(self):
        print("Print help information")

    def help_open(self):
        print("Connect to a host (default port is 23). Usage: open hostname [port]")

    def help_send(self):
        print("Send a string to the server")

    def help_close(self):
        print("Close the current connection")

    def help_quit(self):
        print("Exit the telnet client")

    def default(self, line):
        print(f"Unrecognized command: {line}")

if __name__ == '__main__':
    ShiterTelnetShell().cmdloop()
