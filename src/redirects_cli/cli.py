import os
from typing import Optional

import typer
import yaml

from redirects_cli import __app_name__, __version__

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


def _build_redirect_body(path: str) -> str:
    html = """
<html>
    <head>
        <meta http-equiv="refresh" content="0; url={path}">
    </head>
</html>
    """.format(
        path=path
    )
    return html


@app.command()
def fromFile(
    file_path: str = typer.Option(
        "redirects.yaml",
        "--yaml-file",
        "-y",
        prompt="path to redirects.yaml file?",
        help="Path to redirects.yaml file.",
    ),
    out_dir: str = typer.Option(
        ".",
        "--output-dir",
        "-o",
        prompt="directory path to save the static redirects?",
        help="Path of the directory to save the static redirects.",
    ),
) -> None:
    try:
        with open(file_path, "r") as yaml_file:
            content = yaml.full_load(yaml_file)
            if content:
                for from_path, redirect_to in content.items():
                    target_path = out_dir + "/" + from_path
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    with open(os.path.join(target_path), "w+") as t_file:
                        t_file.write(_build_redirect_body(redirect_to))
                typer.secho("Redirects created.", fg=typer.colors.GREEN)
            else:
                typer.secho(
                    "The redirects file is empty.",
                    fg=typer.colors.YELLOW,
                )
    except Exception:
        typer.secho(
            "The redirects file does not exist.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)


@app.command()
def create(
    redirect_to: str = typer.Option(
        "/path/to/redirect",
        "--redirect-to",
        "-r",
        prompt="redirects path?",
        help="URL or relative path to redirect to.",
    ),
    out_file: str = typer.Option(
        "index.html",
        "--output-file",
        "-o",
        prompt="file path to save the redirects?",
        help="Path of the file to save the static redirects.",
    ),
) -> None:
    try:
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
    except Exception:
        pass

    try:
        with open(os.path.join(out_file), "w+") as t_file:
            t_file.write(_build_redirect_body(redirect_to))
            typer.secho("Redirects created.", fg=typer.colors.GREEN)
    except Exception:
        typer.secho(
            "Cannot write on the output file.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
