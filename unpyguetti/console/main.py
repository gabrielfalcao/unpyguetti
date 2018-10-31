import click

from unpyguetti.engine import RefactoringSession
from unpyguetti.loader import LoadingError


@click.command()
@click.option('-i', '--import-module', multiple=True, help='lookup module name where unpyguetti will find defined strategies')
@click.option('-l', '--load-module', multiple=True, help='read the source code from this file and import')
@click.argument('targets', nargs=-1, required=True)
def entrypoint(import_module, load_module, targets):

    session = RefactoringSession()

    for name in import_module:
        session.load.from_module(name)

    for path in load_module:
        session.load.from_source(path)
    # except LoadingError as e:
    #     raise
    #     click.echo(click.style(f'warning: {e}', fg='yellow'))

    session.run(targets)

    print('unpyguetti', import_module, load_module)
