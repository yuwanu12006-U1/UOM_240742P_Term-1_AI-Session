def print_christmas_tree(lines: int):
    if lines <= 0:
        print("Please enter a positive integer.")
        return

    # Leaves
    for i in range(1, lines + 1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (lines - i)
        print(spaces + stars)

    # Trunk
    trunk_width = lines // 3
    if trunk_width % 2 == 0:
        trunk_width += 1
    if trunk_width == 0:
        trunk_width = 1

    trunk_height = max(1, lines // 4)
    trunk_padding = ' ' * ((2 * lines - 1 - trunk_width) // 2)
    for _ in range(trunk_height):
        print(trunk_padding + '#' * trunk_width)


if __name__ == "__main__":
    try:
        n = int(input("Enter number of lines: ").strip())
        print_christmas_tree(n)
    except ValueError:
        print("Invalid input. Please enter an integer.")
