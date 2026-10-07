import sys

if len(sys.argv) != 2:
    print("Usage: ft_stream_management.py <file>")

else:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        fd_orj = open(sys.argv[1])
    except OSError as e:
        print(f"[STDERR] Error opening file '{sys.argv[1]}':", e, file=sys.stderr)
    else:
        try:
            red = fd_orj.read()
            print("---\n")
            print(red)
            print("---")
        except (OSError, UnicodeDecodeError) as e:
            print(f"[STDERR] Error reading file '{sys.argv[1]}':", e, file=sys.stderr)
            try:
                fd_orj.close()
            except OSError as e:
                print(f"[STDERR] Error closing file '{sys.argv[1]}':", e, file=sys.stderr)
            else:
                print(f"\nFile '{sys.argv[1]}' closed.")
        else:
            try:
                fd_orj.close()
            except OSError as e:
                print(f"[STDERR] Error closing file '{sys.argv[1]}':", e, file=sys.stderr)
            else:
                print(f"File '{sys.argv[1]}' closed.\n")
            print("Transform data:")
            print("---\n")
            splitlist: list[str] = red.splitlines()
            newlist: list[str] = []
            for line in splitlist:
                newlist.append(line + "#")
            newstr = "\n".join(newlist)
            print(newstr)
            print("\n---")
            print("Enter new file name (or empty):", end=" ", flush=True)
            filename = sys.stdin.readline()
            newfile = filename.strip()
            if not newfile:
                print("Not saving data.")
            else:
                print(f"Saving data to '{newfile}'")
                try:
                    fd_new = open(newfile, "w")
                except OSError as e:
                    print(f"[STDERR] Error opening file '{newfile}':", e, file=sys.stderr)
                    print("Data not saved.")
                else:
                    try:
                        fd_new.write(f"{newstr}\n")
                    except OSError as e:
                        print(f"[STDERR] Error writing to file '{newfile}':", e, file=sys.stderr)
                        print("Data not saved.")
                    else:
                        print(f"Data saved in file '{newfile}'.")
                    try:
                        fd_new.close()
                    except OSError as e:
                        print(f"[STDERR] Error closing file '{newfile}':", e, file=sys.stderr)