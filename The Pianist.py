number = int(input())
pieces = {}
for _ in range(number):
    piece, composer, key = input().split("|")
    pieces[piece] = {"composer": composer, "key": key}

command = input()

while not command == "Stop":
    if command.startswith("Add"):
        piece, composer, key = command.split("|")[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command.startswith("Remove"):
        command, piece = command.split("|")
        if piece in pieces:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command.startswith("ChangeKey"):
        piece, new_key = command.split("|")[1:]
        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

sorted_pieces = sorted(pieces.items(), key=lambda kvp: (kvp[0], kvp[1]["composer"]))

for piece in sorted_pieces:
    print(f"{piece[0]} -> Composer: {piece[1]['composer']}, Key: {piece[1]['key']}")
