import click


@click.group()
@click.version_option()
def cli():
    """
    Hotel Menu CLI.

    Grab yourself some food :)
    """


@cli.group()
def user():
    """Manages Users."""


@user.command('register')
def user_new():
    """Creates a new user."""
    first_name = click.prompt(click.style(
        '>> What is your first name? ', fg='yellow'), type=int)
    last_name = click.prompt(click.style(
        '>> What about your last name? ', fg='yellow'), type=str)
    email = click.prompt(click.style(
        '>> What is your email address? ', fg='yellow'), type=str)
    password = click.prompt(click.style(
        '>> Enter your password', fg='yellow'), type=str)
    click.secho('  SUCCESS!  ', bg='green', fg='white', bold=True)
    click.secho('  Created user %s %s  ' %
                (first_name, last_name), bg='white', fg='black', bold=True)


@user.command('login')
def user_login():
    """Logs in a registered user."""
    email = click.prompt(click.style(
        '>> What is your email address? ', fg='yellow'), type=str)
    password = click.prompt(click.style(
        '>> Enter your password', fg='yellow'), type=str)
    # click.secho('  SUCCESS!  ', bg='green', fg='white', bold=True)
    # click.secho('  Logged in  ', bg='white', fg='black', bold=True)

    click.secho('  ERROR!  ', bg='red', fg='white', bold=True)
    click.secho('  Wrong email and or password  ',
                bg='white', fg='black', bold=True)
