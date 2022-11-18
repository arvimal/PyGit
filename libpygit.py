#!/usr/bin/env python3

import argparse
import collections
import configparser
import hashlib
import os
import re
import sys
import zlib
from math import ceil

## Define the main parser, named `argparser`
argparser = argparse.ArgumentParser(description="A Git-type change-tracker, in Python")

## Define sub-parsers for the main parser
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True


# PyGit Argument parser
def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)

    if args.command == "init":
        cmd_init(args)
    elif args.command == "add":
        cmd_add(args)
    elif args.command == "cat-file":
        cmd_cat_file(args)
    elif args.command == "checkout":
        cmd_checkout(args)
    elif args.command == "commit":
        cmd_commit(args)
    elif args.command == "hash-object":
        cmd_hash_object(args)
    elif args.command == "log":
        cmd_log(args)
    elif args.command == "ls-files":
        cmd_ls_files(args)
    elif args.command == "ls-tree":
        cmd_ls_tree(args)
    elif args.command == "merge":
        cmd_merge(args)
    elif args.command == "rebase":
        cmd_rebase(args)
    elif args.command == "rev-parse":
        cmd_rev_parse(args)
    elif args.command == "rm":
        cmd_rm(args)
    elif args.command == "show-ref":
        cmd_show_ref(args)
    elif args.command == "tag":
        cmd_tag(args)

class GitRepository:
    """
    A Git repository object
    """
    worktree = None
    gitdir = None
    conf = None

    def __init__(self, path, force=False):
        self.worktree = path
        self.gitdir = os.path.join(path, ".git")

        if not (force or os.path.isdir(self.gitdir)):
            raise Exception(f"{path} is not a Git repository")

        # Read configuration file at `.git/config`
        self.conf = configparser.ConfigParser()
        cf = repo_file(self, ".config")