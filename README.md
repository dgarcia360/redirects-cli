# redirects-cli

A CLI to create static redirections from a YAML file.

## Why?

You are relying on GitHub Pages to host your site. However, whenever you move a page from one folder to another, your users get the 404 page.

With `redirects-cli`, you can define 301 redirects for the pages you have moved in a YAML file. Then, you can generate static redirects for each page with one command.

In my case, I use this CLI tool in the project's CI pipelines before publishing the site to the `gh-pages` branch.

## Getting started

### Requirements

* Python >= 3.7
* pip

### Installation

```
pip install redirects_cli
```

### Quickstart

```
redirects-cli --help
```

## Usage

### Generate redirects from a static file

To generate static redirects from a YAML file:

1. Define the redirects in a new file named `redirects.yaml`. This file must follow this syntax:

    ```
    # old_path: new_path
    # Example

    # internal link example
    /original-path/page-a.html: /new-path/page-a.html

    # external link example
    /original-path/page-b.html: https://example.local
    ```

2. Run the command:

    ```
    redirects-cli fromfile --yaml-file redirects.yaml --output-dir html
    ```

    The CLI creates the static redirects you have defined in the `redirects.yaml` file within the folder `html`.
    For this example, it creates the following folder structure:

    ```
    my-project/
    ├─ html/
    │  ├─ original-path/page-a.html
    │  ├─ original-path/page-b.html
    ├─ redirects.yaml
    ```

### Create a single redirect

To create a single redirect, you can run the command:

```
redirects-cli --output-file index.html  --redirect-to https://davidgarcia.dev
```

This command creates a 301 redirect to `https://davidgarcia.dev`in the file `index.html`.

## Contributing

Contributions are welcome and appreciated!
If you want to enhance the CLI, please read [CONTRIBUTING.md](CONTRIBUTING.md) file first.

## License

Copyright (c) 2022-present David Garcia ([@dgarcia360](https://davidgarcia.dev)). Licensed under the [MIT License](LICENSE.md).
