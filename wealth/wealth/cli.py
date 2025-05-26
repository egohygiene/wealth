import click

from wealth.mock import generate_mock_finance
from wealth.core.engine import FinanceEngine

@click.group()
def cli():
    """Wealth CLI – personal finance system control panel."""
    pass

@cli.command()
@click.option('--user-id', default=None, help='Specify user_id (default: random UUID)')
def generate(user_id: str | None = None):
    """Generate a mock Finance profile and print as JSON."""
    finance = generate_mock_finance(user_id)
    click.echo(finance.to_json(indent=2))

@cli.command()
@click.option('--user-id', default=None, help='Generate and summarize a mock finance object')
def summary(user_id: str | None = None):
    """Print a quick summary of a Finance profile."""
    finance = generate_mock_finance(user_id)
    engine = FinanceEngine(finance)
    click.echo(engine.summary().to_json())

@cli.command()
@click.option('--filename', default='finance_output.json', help='Filename to export to')
def export(filename: str):
    """Export a mock Finance profile to a JSON file."""
    finance = generate_mock_finance()
    with open(filename, 'w') as f:
        f.write(finance.to_json(indent=2))
    click.echo(f"✅ Exported finance profile to {filename}")
