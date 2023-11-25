import click
import libvoikko

v = libvoikko.Voikko("fi")


@click.command()
@click.argument("word", nargs=-1, type=click.STRING)
# Add a click option to suppress Wiktionary entries.
@click.option(
    "-N", "--no-wiktionary", is_flag=True, help="Suppress Wiktionary entries."
)
@click.option(
    "--no-color", is_flag=True, help="Suppress color output. Useful for scripting."
)
def print_base(word, no_wiktionary, no_color):
    """Analyze word.

    WORD is a Finnish word which you want the base or 'sanakirja' form of.
    You can pass as many word as you want."""
    for w in word:
        unique_baseforms = set()
        for a in v.analyze(w):
            unique_baseforms.add(a["BASEFORM"])
        if len(unique_baseforms) == 0:
            click.echo(
                click.style(f"{w:20} -> Not found", fg="red")
                if not no_color
                else f"{w:20} -> Not found"
            )
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
            w = w if first_entry else ""
            click.echo(
                click.style(f"{w:20} -> {a:15} {wiktionary_entry}", fg=color)
                if not no_color
                else f"{w:20} -> {a:15} {wiktionary_entry}"
            )
            first_entry = False


if __name__ == "__main__":
    print_base()
