#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''{{ cookiecutter.project_slug }}
Usage:
  {{ cookiecutter.project_slug }} -h | --help
  {{ cookiecutter.project_slug }} --version
  {{ cookiecutter.project_slug }} [OPTIONS] ARGS

Arguments:

Options:
  -h --help     Show this screen.
  --version     Show version.
'''

from __future__ import print_function
from docopt import docopt

def main():
    '''Main entry point for the {{ cookiecutter.project_slug }} CLI.'''
    args = docopt(__doc__)
    print(args)

if __name__ == '__main__':
    main()
