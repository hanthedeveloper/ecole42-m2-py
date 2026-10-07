import sys

if len(sys.argv) != 2:
    print("Usage: ft_archive_creation.py <file>")

else:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        fd_orj = open(sys.argv[1])
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}':", e)
    else:
        try:
            red = fd_orj.read()
            print("---\n")
            print(red)
            print("---")
        except (OSError, UnicodeDecodeError) as e:
            print(f"Error reading file '{sys.argv[1]}':", e)
            fd_orj.close()
            print(f"\nFile '{sys.argv[1]}' closed.")
        else:
            fd_orj.close()
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

            try:
                filename = input("Enter new file name (or empty): ")
            except EOFError:
                print("EOFError: Not saving data, input interrupted.")
            else:
                newfile = filename.strip()
                if not newfile:
                    print("Not saving data.")
                else:
                    print(f"Saving data to '{newfile}'")
                    try:
                        fd_new = open(newfile, "w")
                    except OSError as e:
                        print(f"Error opening file '{newfile}':", e)
                    else:
                        try:
                            fd_new.write(f"{newstr}\n")
                        except OSError as e:
                            print(f"Error writing to file '{newfile}':", e)
                        else:
                            print(f"Data saved in file '{newfile}'.")
                        fd_new.close()
