def main():
    from emojipasta.emojigene import EmojipastaGenerator
    import sys

    gen = EmojipastaGenerator.of_default_mappings()

    input = sys.stdin.read()
    out = gen.generate_emojipasta(input)
    print(out, end='')