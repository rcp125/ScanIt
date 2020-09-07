import computer_vision.business_card.extract_fields as bc

selection_map = {
    '1': 'Business Card',
    '2': 'Placeholder',
    '3': 'Placeholder'
}

if __name__ == "__main__":
    print("Welcome to ScanIt Document Parser! What would you like to parse?\n(1) Business Card\n(2) Placeholder\n(3) Placeholder\n")

    selection = input("User Selection: ")
    while(1):
        
        if int(selection) < 1 or int(selection) > 3:
            print("Invalid Option.\n")
            selection = input("Try again:")
        else:
            print("Starting to parse {}...".format(selection_map[selection]))
            break

    bc.hello()
