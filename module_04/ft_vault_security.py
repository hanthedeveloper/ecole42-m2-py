def secure_archive(name: str, act: str = "r", content: str | None = None) -> tuple[bool, str]:
    if act != "w" and act != "r":
        return (False, "Unsupported action. Use 'w' or 'r' (default: 'r')")
    if act == "w" and content is None:
        return (False, "No content to write. (default: 'None')")
    try:
        with open(name, act) as file:
            if act == "w":
                file.write(content)
                cntnt = "Content successfully written to file"
            else:
                cntnt = file.read()
    except (OSError, UnicodeDecodeError) as e:
        return (False, str(e))
    else:
        return (True, cntnt)

if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    status, text = secure_archive("ancient_fragment.txt")
    print((status, text))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "w", text))