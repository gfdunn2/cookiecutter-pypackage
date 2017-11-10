#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    cli_dst_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')

    cli_src_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli_click.py')
    if 'click' == '{{ cookiecutter.command_line_interface|lower }}':
        os.rename(cli_src_file, cli_dst_file)
    else:
        remove_file(cli_src_file)

    cli_src_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli_docopt.py')
    if 'docopt' == '{{ cookiecutter.command_line_interface|lower }}':
        os.rename(cli_src_file, cli_dst_file)
    else:
        remove_file(cli_src_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
