import click

@click.group()
def main():
    """Starter Template CLI"""
    pass

@main.command()
def hello():
    """Print a hello message."""
    click.echo("Hello from the starter template!")

@main.command()
def build():
    """Simulate a build step."""
    click.echo("Building the application...")
    # Simulate build logic
    click.echo("Build complete!")

if __name__ == "__main__":
    main() 