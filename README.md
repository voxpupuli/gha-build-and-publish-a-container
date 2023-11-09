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
        uses: voxpupuli/gha-build-and-publish-a-container@v2
        with:
          registry: docker.io                 # Default: ghcr.io
          registry_username: foobar           # Default: github.repository_owner
          registry_password: "P4SSw0rd!"      # No default, for github set it to ${{ secrets.GITHUB_TOKEN }}
          build_arch: linux/amd64,linux/arm64 # Default: linux/amd64
          build_args: |                       # No Default, can be empty
            PUPPET_VERSION=8.2.0
            PUPPET_RELEASE=8
          build_context: 'puppetdb'           # Default: .
          buildfile: Dockerfile.something     # Default: Dockerfile
          publish: 'false'                    # Default: 'true'
          docker_username: 'someone'          # No default, can be empty
          docker_password: 'docker hub pass'  # No default, can be empty
          tags: |                             # No default, can be empty
            docker.io/${{ github.repository }}:3.2
            docker.io/${{ github.repository }}:latest
            ghcr.io/${{ github.repository }}:3.2
            ghcr.io/${{ github.repository }}:latest
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
      uses: voxpupuli/gha-build-and-publish-a-container@v2
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish: 'false'
        tags: ci/test:dummy
```

# Behavior

## Tagging

The git `main`-branch will automatically be tagged with the `development` container-tag, if no custom tags are supplied.
If one does a git-tag like `v1.0.0` this will translate into `1.0.0` container-tag.
The last git-tag also will be tagged with the `latest` container-tag.
If custom tags are supplied, this rules are not valid anymore.
The tags which are supplied will then be used. The tags have to be supplied in a newline seperated list.
The format is: `registry/user/repo:tag-name`.

## Push to hub.docker.com

If you specify a docker_username and a docker_password, the action will do a second registry login.
It will then automatically also log in to docker.io. To push images to docker.io you have to add tags with the docker.io registry path in front.

f.e.:
```yaml
tags: |
  ghcr.io/${{ github.repository }}:${{ github.ref_name }}-${{ matrix.release }}
  docker.io/${{ github.repository }}:${{ github.ref_name }}-${{ matrix.release }}
  ghcr.io/${{ github.repository }}:latest
  docker.io/${{ github.repository }}:latest
```
