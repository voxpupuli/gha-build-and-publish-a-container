#!/usr/bin/env python3

import argparse
import os
import logging

def determine_tags(image: str, version: str) -> set[str]:
    """
    >>> determine_tags('ghcr.io/example.com', 'v1.2.3')
    {'ghcr.io/example.com:1.2.3', 'ghcr.io/example.com:latest'}
    >>> determine_tags('ghcr.io/example.com', 'main')
    {'ghcr.io/example.com:development'}
    >>> determine_tags('ghcr.io/example.com', 'master')
    {'ghcr.io/example.com:development'}
    """

    tags = set()

    if version.startswith('v'):
        version = version.replace("v", "")
        tags.add(f"{image}:latest")
    elif version in ('main', 'master'):
        version = "development"

    logging.debug('Version: %s', version)

    tags.add(f"{image}:{version}")

    logging.debug('Tags: %s', tags)
    return tags


def main():

    parser = argparse.ArgumentParser(description='Get the tags!')
    parser.add_argument("-l", "--log", dest="log_level",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help="Set the logging level")
    parser.add_argument("--ref", dest="github_ref_name")
    parser.add_argument("--repo", dest="github_repository")

    args = parser.parse_args()

    if args.log_level:
        logging.basicConfig(level=getattr(logging, args.log_level))

    logging.debug('ARGS: %s', args)

    image = f'ghcr.io/{args.github_repository}'
    logging.debug('Image : %s', image)

    version = args.github_ref_name

    tags = determine_tags(image, version)

    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as output:
        output.write(f'tags={",".join(sorted(tags))}')


if __name__ == '__main__':
    main()
