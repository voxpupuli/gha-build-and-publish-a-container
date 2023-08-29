#!/usr/bin/env python3

import os
import argparse
import logging

parser = argparse.ArgumentParser(description='Get the tags!')
parser.add_argument("-l", "--log", dest="logLevel", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help="Set the logging level")
parser.add_argument("--ref", dest="github_ref_name")
parser.add_argument("--repo", dest="github_repository")

args = parser.parse_args()

if args.logLevel:
  logging.basicConfig(level=getattr(logging, args.logLevel))

logging.debug(f'ARGS: {args}')

image = f'ghcr.io/{args.github_repository}'
logging.debug(f'Image : {image}')

tags = set()
version = args.github_ref_name

if version.startswith('v'):
  version = args.github_ref_name.replace("v", "")
  tags.add(f"{image}:latest")

if version == 'main' or version == 'master':
  version = "development"

logging.debug(f'Version: {version}')

tags.add(f"{image}:{version}")
tags = ",".join(sorted(list(tags)))

logging.debug(f'Tags: {tags}')

with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
  print(f'tags={tags}', file=fh)
