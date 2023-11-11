# Input
width, length = int(input()), int(input())

total_pieces = width * length

# Logics
pieces_eaten = 0

while total_pieces >= pieces_eaten:
    pieces = input()

    if pieces == "STOP":
        print(f"{total_pieces - pieces_eaten} pieces are left.")
        break
    else:
        pieces_eaten += int(pieces)
else:
    print(f"No more cake left! You need {pieces_eaten - total_pieces} pieces more.")
