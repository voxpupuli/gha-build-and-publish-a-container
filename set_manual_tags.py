#!/usr/bin/env python3

import argparse
import os
import logging

def determine_tags(image: str, version: str, latest: bool) -> set[str]:
    """
    >>> determine_tags('ghcr.io/example.com', 'foo', True)
    {'ghcr.io/example.com:foo', 'ghcr.io/example.com:latest'}
    >>> determine_tags('ghcr.io/example.com', 'bar', False)
    {'ghcr.io/example.com:bar'}
    """

    tags = set()

    if latest:
        tags.add(f"{image}:latest")

    logging.debug('Version: %s', version)

    tags.add(f"{image}:{version}")

    logging.debug('Tags: %s', tags)
    return tags


def main():

    parser = argparse.ArgumentParser(description='Get the tags!')
    parser.add_argument("-l", "--log", dest="log_level",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help="Set the logging level")
    parser.add_argument("--repo", dest="github_repository")
    parser.add_argument("--tags", dest="manual_tags")

    args = parser.parse_args()

    if args.log_level:
        logging.basicConfig(level=getattr(logging, args.log_level))

    logging.debug('ARGS: %s', args)

    image = f'ghcr.io/{args.github_repository}'
    logging.debug('Image : %s', image)

    version = args.manual_tags.split(',')

    tags = determine_tags(image, version)

    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as output:
        output.write(f'tags={",".join(sorted(tags))}')


if __name__ == '__main__':
    main()
