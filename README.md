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
      - uses: voxpupuli/gha-build-and-publish-a-container@main
        with:
          github_token: ${{ secrets.github_token }}
          build_arch: linux/amd64,linux/arm64
```

# Behavior

The `main`-branch will always be tagged with the `development` container-tag.
If one does a git-tag like `v1.0.0` this will translate into `1.0.0` container-tag.
The last git-tag also will be tagged with the `latest` container-tag.
