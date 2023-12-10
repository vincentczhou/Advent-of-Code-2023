chars = "23456789TJQKA"
char_ranking = {char: i for i, char in enumerate(chars)}


def matches(hand):
    char_match = {}
    for char in hand:
        if char not in char_match.keys():
            char_match[char] = 1
        else:
            char_match[char] += 1

    two_kind = 0
    three_kind = False
    four_kind = False
    five_kind = False

    for value in char_match.values():
        if value == 2:
            two_kind += 1
        if value == 3:
            three_kind = True
        if value == 4:
            four_kind = True
        if value == 5:
            five_kind = True

    if five_kind:
        return 6
    elif four_kind:
        return 5
    elif three_kind and two_kind == 1:
        return 4
    elif three_kind:
        return 3
    elif two_kind == 2:
        return 2
    elif two_kind == 1:
        return 1
    else:
        return 0


def main():
    with open("input") as input:
        hands_bid = {}
        hand_order = {}
        for line in input:
            chunk = line.strip().split()
            hands_bid[chunk[0]] = int(chunk[1])
            hand_order[chunk[0]] = [0, 0]

        hand_list = list(hands_bid.keys())

        char_sort_hl = sorted(hand_list, key=lambda hand: [
            char_ranking[char] for char in hand])
        for i, hand in enumerate(char_sort_hl):
            hand_order[hand][1] = i

        for hand in hand_list:
            hand_order[hand][0] = matches(hand)

        final_sort_hl = sorted(hand_list, key=lambda hand: hand_order[hand])

        sum = 0
        for i, hand in enumerate(final_sort_hl):
            sum += (i + 1) * hands_bid[hand]

        print(f"The sum is: {sum}")


if __name__ == "__main__":
    main()

# The sum is: 249726565
