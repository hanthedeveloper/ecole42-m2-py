import sys

print("=== Player Score Analytics ===")

length = len(sys.argv)
newlist: list[int] = []
i = 1
while i < length:
    try:
        newlist = newlist + [int(sys.argv[i])]
    except ValueError:
        print(f"Invalid parameter: '{sys.argv[i]}'")
    i += 1
if len(newlist) == 0:
    print("No scores provided. Usage: python3 ft_score_analytics.py", end=" ")
    print("<score1> <score2> ...")
else:
    print("Scores processed:", newlist)
    print("Total players:", len(newlist))
    print("Total score:", sum(newlist))
    print("Average score:", (sum(newlist) / len(newlist)))
    print("High score:", max(newlist))
    print("Low score", min(newlist))
    print("Score range:", (max(newlist) - min(newlist)))
