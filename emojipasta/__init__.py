def main():
    from emojipasta.emojigene import EmojipastaGenerator
    import sys

    gen = EmojipastaGenerator.of_default_mappings()

    out = gen.generate_emojipasta(sys.stdin.read())
    print(out)