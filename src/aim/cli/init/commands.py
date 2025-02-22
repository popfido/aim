import click
import os

from aim.sdk.repo import Repo
from aim.sdk.utils import clean_repo_path

from aim.core.utils.tracking import analytics


@click.command()
@click.option('--repo', required=False, type=click.Path(exists=True,
                                                        file_okay=False,
                                                        dir_okay=True,
                                                        writable=True))
@click.option('-y', '--yes', is_flag=True, help='Automatically confirm prompt')
def init(repo, yes):
    """
    Initializes new repository in the --repo directory.
    Initializes new repository in the current working directory if --repo argument is not provided:
     - Creates .aim directory & runs upgrades for structured DB
    """
    repo_path = clean_repo_path(repo) or os.getcwd()
    re_init = False
    if Repo.exists(repo_path):
        if yes:
            re_init = True
        else:
            re_init = click.confirm('Aim repository is already initialized. '
                                    'Do you want to re-initialize to empty Aim repository?')
        if not re_init:
            return
        # Clear old repo
        Repo.rm(repo_path)

    repo = Repo.from_path(repo_path, init=True)
    if re_init:
        analytics.track_event(event_name='[Repo] Initialize')
        click.echo(
            'Re-initialized empty Aim repository at {}'.format(repo.root_path))
    else:
        analytics.track_event(event_name='[Repo] Re-initialize')
        click.echo('Initialized a new Aim repository at {}'.format(repo.root_path))
