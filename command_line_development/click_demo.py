# coding: utf8
# @version : 2
# @Time    : 2020/3/26 4:35 下午
# @Author  : llf
# @File    : click_demo.py
import click


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    print(count, name)

    for _ in range(count):
        click.echo(f"Hello, {name}!")


if __name__ == '__main__':
    hello()
