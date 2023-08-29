#!/usr/bin/env python3

import os
import sys

# ARGs
github_repository = sys.argv[1]
github_ref_name   = sys.argv[2]

image   = f'ghcr.io/{github_repository}'
tags    = set()
version = github_ref_name

if version.startswith('v'):
  version = github_ref_name.replace("v", "")
  tags.add(f"{image}:latest")

if version == 'main':
  version = "development"

tags.add(f"{image}:{version}")
tags = ",".join(sorted(list(tags)))

with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
  print(f'tags={tags}', file=fh)
