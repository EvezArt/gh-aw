import click
import requests

BASE_URL = "http://localhost:8000"

@click.group()
def cli():
    pass

@cli.command()
@click.argument("text")
def seed(text):
    resp = requests.post(f"{BASE_URL}/aftermath/seed", json={"text": text, "motifs": [], "personas": []})
    click.echo(resp.json())

@cli.command()
def scan():
    resp = requests.post(f"{BASE_URL}/aftermath/scan")
    click.echo(resp.json())

# Add more commands for metrics/nav
