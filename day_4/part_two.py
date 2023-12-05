def num_matches(tuple_card):
    matches = 0
    for num in tuple_card[1]:
        if num in tuple_card[0]:
            matches += 1
    return matches


def parse_line(line):
    chunk = line.strip().split(":")
    id = int(chunk[0].split(" ")[-1])
    card_set = chunk[1].split("|")
    win_card = card_set[0].strip().split()
    my_card = card_set[1].strip().split()

    matches = num_matches((win_card, my_card))

    return id, matches


def recursion(cards, curr_card, limit, base, memo):
    if (curr_card > limit):
        return 0

    matches = cards[curr_card]
    current_card_tot_matches = 1
    if (curr_card == limit or (matches == 0 and not base)):
        return current_card_tot_matches

    for i in range(matches):
        to_add = 0
        if (curr_card + i + 1) in memo.keys():
            to_add = memo[curr_card + i + 1]
        else:
            to_add = recursion(cards,
                               curr_card + i + 1, limit, False, memo)
        current_card_tot_matches += to_add

    if (curr_card not in memo.keys()):
        memo.update({curr_card: current_card_tot_matches})

    if base:
        return current_card_tot_matches + recursion(cards, curr_card + 1, limit, True, memo)
    return current_card_tot_matches


def main():
    with open("input") as input:
        cards = {}
        for line in input:
            id, matches = parse_line(line)
            cards.update({id: matches})

        limit = len(cards.items())
        sum = recursion(cards, 1, limit, True, {})
        print(f"The sum is: {sum}")


if __name__ == "__main__":
    main()

# The sum is: 5554894
