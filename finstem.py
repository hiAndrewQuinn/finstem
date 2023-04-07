import click 
import libvoikko

v = libvoikko.Voikko("fi")

@click.command()
@click.argument('word', nargs=-1, type=click.STRING)
def print_base(word):
    """Analyze word.

    WORD is a Finnish word which you want the base or 'sanakirja' form of.
    You can pass as many word as you want."""
    for w in word:
        analysis = v.analyze(w)
        if not analysis:
            click.echo(click.style(f"{w:20} -> Not found", fg='red'))
        elif len(analysis) == 1:
                click.echo(click.style(f"{w:20} -> {analysis[0]['BASEFORM']:20}", fg='green'))
        else:
            # Print the first one with the word, the rest without
            click.echo(click.style(f"{w:20} -> {analysis[0]['BASEFORM']:20}", fg='yellow'))
            for a in analysis[1:]:
                click.echo(click.style((" " * 20) + f" -> {a['BASEFORM']:20}", fg='yellow'))


if __name__ == '__main__':
    print_base()
