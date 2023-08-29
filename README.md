# GHA to build and publish a 🛢️ container

## Usage

```yaml
on:
  - push

jobs:
  build_job:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v3
      - uses: betadots/gha-build-and-publish-a-container@main
        with:
          github_token: ${{ secrets.github_token }}
          build_arch: linux/amd64,linux/arm64

```
