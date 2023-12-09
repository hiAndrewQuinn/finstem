import click
import libvoikko

v = libvoikko.Voikko("fi")


def print_base_DEPRECATED(words, no_wiktionary, no_color):
    """Analyze words.

    words is a Finnish words which you want the base or 'sanakirja' form of.
    You can pass as many words as you want."""
    for w in words:
        unique_baseforms = get_baseforms_of_word(w)
        if len(unique_baseforms) == 0:
            click.echo(
                click.style(f"{w:20} -> Unknown", fg="red")
                if not no_color
                else f"{w:20} -> Unknown", color=True)
            continue
        elif len(unique_baseforms) == 1:
            color = "green"
        else:
            color = "yellow"

        first_entry = True
        for a in unique_baseforms:
            if not no_wiktionary:
                wiktionary_entry = f"https://en.wiktionary.org/wiki/{a}#Finnish"
            else:
                wiktionary_entry = ""
            w = w if first_entry or is_thick else ""
            click.echo(
                click.style(f"{w:20} -> {a:15} {wiktionary_entry}", fg=color)
                if not no_color
                else f"{w:20} -> {a:15} {wiktionary_entry}", color=True)
            first_entry = False


def get_baseforms_of_word(word: str) -> set:
    """Return a set of unique baseforms for a word.

    :param word: str
    """
    unique_baseforms = set()
    for a in v.analyze(word):
        unique_baseforms.add(a["BASEFORM"])
    return unique_baseforms


def get_baseforms_of_words(words: list) -> list:
    """Return a set of unique baseforms for a list of words, in the same order
    as the input list itself.

    :param words: list
    """
    return [(word, get_baseforms_of_word(word)) for word in words]


@click.command()
@click.argument("words", nargs=-1, type=click.STRING)
@click.option(
    "-f",
    "--format",
    type=click.Choice(["CSV", "TSV", "JSON", "nice"], case_sensitive=False),
    default="nice",
    help="Output format. The default with the colors and arrows is 'nice'; the other options are useful for scripting.",
)
@click.option(
    "-N", "--no-wiktionary", is_flag=True, help="Suppress Wiktionary entries."
)
@click.option(
    "--no-color",
    is_flag=True,
    help='(Only for the "nice" format.) Suppress color output. Useful for scripting.',
)
@click.option(
    "--thick",
    is_flag=True,
    help="(Pretty only.) Print the word on every line, even if there are multiple possible dictionary forms.",
)
def main(words, format, no_wiktionary, no_color, thick):
    words = strip_punctuation(words)
    global is_thick
    is_thick = thick or (format == "CSV" or format ==
                         "TSV" or format == "JSON")
    if format == "CSV":
        return print_csv(words, no_wiktionary)
    elif format == "TSV":
        return print_tsv(words, no_wiktionary)
    elif format == "JSON":
        return print_json(words, no_wiktionary)
    else:
        return print_base(words, no_wiktionary, no_color)


def strip_punctuation(words):
    return [word.strip(".,;:!?*`()[]{}") for word in words]


def print_csv(words, no_wiktionary):
    """Print baseforms in CSV format."""
    click.echo("word,possible_baseform,wiktionary", color=True)
    for w in words:
        unique_baseforms = get_baseforms_of_word(w)
        if len(unique_baseforms) == 0:
            click.echo(f"{w},Unknown,", color=True)
            continue
        elif len(unique_baseforms) == 1:
            color = "green"
        else:
            color = "yellow"

        first_entry = True
        for a in unique_baseforms:
            if not no_wiktionary:
                wiktionary_entry = f"https://en.wiktionary.org/wiki/{a}#Finnish"
            else:
                wiktionary_entry = ""
            w = w if first_entry or is_thick else ""
            click.echo(f"{w},{a},{wiktionary_entry}", color=True)
            first_entry = False


def print_tsv(words, no_wiktionary):
    """Print baseforms in TSV format."""
    click.echo("word\tpossible_baseform\twiktionary", color=True)
    for w in words:
        unique_baseforms = get_baseforms_of_word(w)
        if len(unique_baseforms) == 0:
            click.echo(f"{w}\tUnknown", color=True)
            continue
        elif len(unique_baseforms) == 1:
            color = "green"
        else:
            color = "yellow"

        first_entry = True
        for a in unique_baseforms:
            if not no_wiktionary:
                wiktionary_entry = f"https://en.wiktionary.org/wiki/{a}#Finnish"
            else:
                wiktionary_entry = ""
            w = w if first_entry or is_thick else ""
            click.echo(f"{w}\t{a}\t{wiktionary_entry}", color=True)
            first_entry = False


def print_json(words, no_wiktionary):
    """Print baseforms in JSON format. (Could use some work!)"""
    for w in words:
        unique_baseforms = get_baseforms_of_word(w)
        if len(unique_baseforms) == 0:
            click.echo(f'{{"word": "{w}", "baseforms": []}}', color=True)
            continue
        elif len(unique_baseforms) == 1:
            color = "green"
        else:
            color = "yellow"

        first_entry = True
        for a in unique_baseforms:
            if not no_wiktionary:
                wiktionary_entry = f"https://en.wiktionary.org/wiki/{a}#Finnish"
            else:
                wiktionary_entry = ""
            w = w if first_entry or is_thick else ""
            click.echo(
                f'{{"word": "{w}", "baseforms": ["{a}"], "wiktionary": "{wiktionary_entry}"}}', color=True)
            first_entry = False


def print_base(words, no_wiktionary, no_color):
    """Print baseforms in nice format."""
    for w in words:
        unique_baseforms = get_baseforms_of_word(w)
        if len(unique_baseforms) == 0:
            click.echo(
                click.style(f"{w:20} -> Unknown", fg="red")
                if not no_color
                else f"{w:20} -> Unknown", color=True)
            continue
        elif len(unique_baseforms) == 1:
            color = "green"
        else:
            color = "yellow"

        first_entry = True
        for a in unique_baseforms:
            if not no_wiktionary:
                wiktionary_entry = f"https://en.wiktionary.org/wiki/{a}#Finnish"
            else:
                wiktionary_entry = ""
            w = w if first_entry or is_thick else ""
            click.echo(
                click.style(f"{w:20} -> {a:15} {wiktionary_entry}", fg=color)
                if not no_color
                else f"{w:20} -> {a:15} {wiktionary_entry}", color=True)
            first_entry = False


if __name__ == "__main__":
    main()
