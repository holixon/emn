---
title: Project Setup
---

If you are interested in developing and building the project please follow the following instruction.

## Version control

To get sources of the project, please execute:

```bash
git clone https://github.com/holixon/emn.git
cd emn
```

We are using gitflow in our git SCM. That means that you should start from `develop` branch,
create a `feature/<name>` out of it and once it is completed create a pull request containing
it. Please squash your commits before submitting and use semantic commit messages, if possible.

## Build Documentation Site

We are using MkDocs for generation of a static site documentation and rely on Markdown as much as possible.
MkDocs is written in Python 3 and needs to be installed on your machine. For the installation please run the following
command from your command line:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r ./docs/requirements.txt
```

As alternative, you might want to install `pip` and `python`. Then use `python3 -m pip install --user -r ./docs/requirements.txt --break-system-packages`.

For creation of documentation, please run:

```bash
mkdocs build
```

The docs are generated into `site` directory.

!!! note
    If you want to develop your docs in 'live' mode, run `mkdocs serve` and access the [http://localhost:8000/](http://localhost:8000/) from your browser.

## Continuous Integration

GitHub Actions is building all branches on commit hook. 

### Trigger new release

!!! warning
    This operation requires special permissions.

We rely on GitHub Action to create a new release. Just publish a new release in GitHub, and a special workflow will publish 
a new release in GitHub Package Repository.
