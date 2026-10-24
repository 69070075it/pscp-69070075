'''B - Fully pair?'''
def main():
    '''B - Fully pair?'''
    text = input().strip()
    unpaired = []

    for char in text:
        if text.count(char) % 2 and char not in unpaired:
            unpaired.append(char)

    if unpaired:
        print("".join(unpaired))
    else:
        print("fully paired")

main()
