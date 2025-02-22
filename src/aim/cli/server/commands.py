import os
import click

from aim.cli.utils import set_log_level
from aim.sdk.repo import Repo, RepoStatus
from aim.sdk.utils import clean_repo_path
from aim.core.transport.config import AIM_SERVER_DEFAULT_HOST, AIM_SERVER_DEFAULT_PORT, AIM_SERVER_MOUNTED_REPO_PATH
from aim.core.transport.server import start_server

from aim.core.utils.tracking import analytics


@click.command()
@click.option('-h', '--host', default=AIM_SERVER_DEFAULT_HOST, type=str)
@click.option('-p', '--port', default=AIM_SERVER_DEFAULT_PORT, type=int)
@click.option('-w', '--workers', default=1, type=int)
@click.option('--repo', required=False, type=click.Path(exists=True,
                                                        file_okay=False,
                                                        dir_okay=True,
                                                        writable=True))
@click.option('--ssl-keyfile', required=False, type=click.Path(exists=True,
                                                               file_okay=True,
                                                               dir_okay=False,
                                                               readable=True))
@click.option('--ssl-certfile', required=False, type=click.Path(exists=True,
                                                                file_okay=True,
                                                                dir_okay=False,
                                                                readable=True))
@click.option('--log-level', required=False, default='', type=str)
@click.option('-y', '--yes', is_flag=True, help='Automatically confirm prompt')
def server(host, port, workers,
           repo, ssl_keyfile, ssl_certfile,
           log_level, yes):
    # TODO [MV, AT] remove code duplication with aim up cmd implementation
    if log_level:
        set_log_level(log_level)

    repo_path = clean_repo_path(repo) or Repo.default_repo_path()
    repo_status = Repo.check_repo_status(repo_path)
    if repo_status == RepoStatus.MISSING:
        if yes:
            init_repo = True
        else:
            init_repo = click.confirm(f'\'{repo_path}\' is not a valid Aim repository. Do you want to initialize it?')

        if not init_repo:
            click.echo('To initialize repo please run the following command:')
            click.secho('aim init', fg='yellow')
            return
        repo_inst = Repo.from_path(repo_path, init=True)
    elif repo_status == RepoStatus.UPDATE_REQUIRED:
        # TODO: add version migration handling script(s)
        if yes:
            upgrade_repo = True
        else:
            upgrade_repo = click.confirm(f'\'{repo_path}\' requires upgrade. Do you want to run upgrade automatically?')
        if upgrade_repo:
            pass
        else:
            click.echo('To upgrade repo please run the following command:')
            click.secho(f'aim upgrade --repo {repo_path}', fg='yellow')
            return
    elif repo_status == RepoStatus.UNKNOWN:
        click.echo(f'\'{repo_path}\' is not a valid Aim repository. '
                   f'To initialize repo please run the following command:')
        click.secho('aim init', fg='yellow')
        return
    else:
        repo_inst = Repo.from_path(repo_path)

    os.environ[AIM_SERVER_MOUNTED_REPO_PATH] = repo_inst.path

    click.echo(
        click.style('Running Aim Server on repo `{}`'.format(repo_inst),
                    fg='yellow'))
    click.echo('Server is mounted on {}:{}'.format(host, port), err=True)
    click.echo('Press Ctrl+C to exit')
    analytics.track_event(event_name='[Aim Remote Tracking] Start server')

    try:
        start_server(host, port, workers, ssl_keyfile, ssl_certfile)
    except Exception:
        click.echo('Failed to run Aim Tracking Server. '
                   'Please see the logs for details.')
        return
