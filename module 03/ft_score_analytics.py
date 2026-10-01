import sys

print("=== Player Score Analytics ===")

l = len(sys.argv)
newlist = []
i = 1
while i < l:
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
    print("Highest score:", max(newlist))
    print("Lowest score", min(newlist))
    print("Score range:", (max(newlist) - min(newlist)))