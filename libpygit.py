#!/usr/bin/env python3

import argparse
import collections
import configparser
import hashlib
from math import ceil
import os
import re
import sys
import zlib

## Define the main parser, named `argparser`
argparser = argparse.ArgumentParser(description="A Git-type change tracker in Python")

## Define sub-parsers for the main parser
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True


