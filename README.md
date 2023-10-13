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
      - name: Build and publish a container
        uses: voxpupuli/gha-build-and-publish-a-container@v1
        with:
          registry: docker.io                 # Default: ghcr.io
          registry_username: foobar           # Default: github.repository_owner
          registry_password: "P4SSw0rd!"      # No default, for github set it to ${{ secrets.GITHUB_TOKEN }}
          build_arch: linux/amd64,linux/arm64 # Default: linux/amd64
          build_args: 'PUPPET_VERSION=8'      # No default
          build_context: 'puppetdb'           # Default: .
          buildfile: Dockerfile.something     # Default: Dockerfile
          publish: 'false'                    # Default: 'true'
```

Test container build in ci:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: read
    steps:
    - name: Test container build
      uses: voxpupuli/gha-build-and-publish-a-container@v1
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish: 'false'
```

# Behavior

The `main`-branch will always be tagged with the `development` container-tag.
If one does a git-tag like `v1.0.0` this will translate into `1.0.0` container-tag.
The last git-tag also will be tagged with the `latest` container-tag.
