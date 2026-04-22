def count_lines(name):
    with open(name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return len(lines)


def count_chars(name):
    with open(name, 'r', encoding='utf-8') as f:
        text = f.read()
    return len(text)


def test(name):
    lines = count_lines(name)
    chars = count_chars(name)

    print(f"Lines: {lines}")
    print(f"Chars: {chars}")