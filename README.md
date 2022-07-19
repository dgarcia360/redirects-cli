# redirects-cli

A CLI to create static redirections from a YAML file.

## Why?

You are relying on GitHub Pages to host your site. However, whenever you move a page from one folder to another, your users get the 404 page. 

With `redirects-cli`, you can define 301 redirects for the pages you have moved  in a YAML file. Then, you can generate static redirects for each path with one command.

In my case, I use this command in the project's CI pipelines before publishing the site to the `gh-pages` branch. If I define the redirections correctly, that means no more 404 errors!

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
redirects-cli fromfile --help
```

## Usage

To generate static redirections from a YAML file:

1. Define the redirects in a new file named `redirections.yaml`.
This file must follow this syntax:

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

The CLI creates the static redirections you have defined in the `redirections.yaml` file within the folder `html`. 
For this example, it creates the following folder structure:

```
my-app/
├─ html/
│  ├─ original-path/page-a.html
│  ├─ original-path/page-b.html
├─ redirects.yaml
```

## Contributing

Contributions are welcome and appreciated!
If you want to enhance the CLI, please read [CONTRIBUTING.md](CONTRIBUTING.md) file first.

## License

Copyright (c) 2022-present David Garcia ([@dgarcia360](https://davidgarcia.dev)). Licensed under the [MIT License](LICENSE.md).
