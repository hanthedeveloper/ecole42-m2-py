import sys


if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")

else:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        fd = open(sys.argv[1])
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}':", e)
    else:
        try:
            red = fd.read()
            print("---\n")
            print(red)
            print("---")
        except (OSError, UnicodeDecodeError) as e:
            print(f"Error reading file '{sys.argv[1]}':", e)
        finally:
            fd.close()
            print(f"File '{sys.argv[1]}' closed.")
