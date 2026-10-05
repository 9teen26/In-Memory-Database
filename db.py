import sys
import os

class IMDB:
    def __init__(self):
        self.db = {}

    def exec_command(self, userinput):
        parts = userinput.strip().split()
        if not parts:
            return ""

        command = parts[0].upper()

        # SET Command
        if command == "SET":
            if len(parts) < 3:
                return "ERROR: Syntax is SET <key> <value>"
            key = parts[1]
            value = " ".join(parts[2:])
            self.db[key] = value
            return "OK"

        # GET Command
        elif command == "GET":
            if len(parts) != 2:
                return "ERROR: Syntax is GET <key>"
            key = parts[1]
            if key in self.db:
                return self.db[key]
            return "ERROR: Key not found"

        # DEL Command
        elif command == "DEL":
            if len(parts) != 2:
                return "ERROR: Syntax is DEL <key>"
            key = parts[1]
            if key in self.db:
                del self.db[key]
                return "OK"
            return "ERROR: Key not found"

        # EXISTS Command
        elif command == "EXISTS":
            if len(parts) != 2:
                return "ERROR: Syntax is EXISTS <key>"
            key = parts[1]
            return "Exists" if key in self.db else "Not found"

        # SAVE Command
        elif command == "SAVE":
            if len(parts) != 2:
                return "ERROR: Syntax is SAVE <filename>"
            filename = parts[1]
            try:
                with open(filename, 'w') as f:
                    for k, v in self.db.items():
                        f.write(f"{k}={v}\n")
                return f"OK: Saved to {filename}"
            except Exception as e:
                return f"ERROR: Could not save file: {str(e)}"

        # LOAD Command
        elif command == "LOAD":
            if len(parts) != 2:
                return "ERROR: Syntax is LOAD <filename>"
            filename = parts[1]
            if not os.path.exists(filename):
                return "ERROR: File does not exist"
            try:
                # Clear active memory state before loading new file state
                self.db.clear()
                with open(filename, 'r') as f:
                    for line in f:
                        if '=' in line:
                            # Split exactly on the first '=' to protect values with '=' in them
                            k, v = line.strip().split('=', 1)
                            self.db[k] = v
                return f"OK: Loaded from {filename}"
            except Exception as err:
                return f"ERROR: Could not load file: {str(err)}"

        # EXIT Command
        elif command == "EXIT":
            print("CLI database closed.")
            sys.exit(0)

        else:
            return f"ERROR: Unknown command '{command}'"

# REPL
if __name__ == "__main__":
    database = IMDB()
    print("CLI database initiated. Type EXIT to quit.")
    while True:
        try:
            userinput = input("> ")
            result = database.exec_command(userinput)
            if result:
                print(result)
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break
