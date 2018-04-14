import click
import requests
import json
from terminaltables import SingleTable


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
    click.secho('  Login  ', bg='green', fg='white', bold=True)
    email = click.prompt(click.style(
        '>> What is your email address? ', fg='yellow'), type=str)
    password = click.prompt(click.style(
        '>> Enter your password', fg='yellow'), type=str)
    # click.secho('  SUCCESS!  ', bg='green', fg='white', bold=True)
    # click.secho('  Logged in  ', bg='white', fg='black', bold=True)

    click.secho('  ERROR!  ', bg='red', fg='white', bold=True)
    click.secho('  Wrong email and or password  ',
                bg='white', fg='black', bold=True)


@cli.group()
def menu():
    """Manages Menu Operations."""


@menu.command('add')
def menu_new():
    """Creates a new menu item."""
    click.clear()
    click.secho('  New Menu Item  ', bg='green', fg='white', bold=True)
    name = click.prompt(click.style(
        '>> What is the name of the food? ', fg='yellow'), type=str)
    price = click.prompt(click.style(
        '>> How much does it cost? ', fg='yellow'), type=int)

    url = 'http://127.0.0.1:5000/menu/'

    data = {
        "name": name,
        "price": price
    }
    requests.post(url, json=data)

    click.secho('  SUCCESS!  ', bg='green', fg='white', bold=True)
    click.secho('  Food item %s, which costs %s added to the menu  ' %
                (name, price), bg='white', fg='black', bold=True)


@menu.command('view')
def menu_view():
    """Shows menu food items."""
    url = 'http://127.0.0.1:5000/menu/'
    response = requests.get(url)

    click.clear()
    click.secho('  Menu Items  ', bg='green', fg='white', bold=True)
    # click.echo(response.status_code)
    table_data = []
    table_data.append(['Food ID', 'Food Name', 'Price (Kshs)'])
    x = response.json()
    for key, value in x.items():
        table_data.append([key, value['name'], value['price']])
        table = SingleTable(table_data)
    print(table.table)
