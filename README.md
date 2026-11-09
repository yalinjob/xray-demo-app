# xray-demo-app

> **Intentionally vulnerable.** The Python dependencies in `requirements.txt` are pinned to old versions with known medium/high CVEs so JFrog Xray has something to find. Do not deploy this anywhere real.

A tiny Flask service (`/`, `/health`, `/versions`, `/encrypt/<text>`) packaged as a Docker image. A GitHub Action builds it and pushes it to the Artifactory Docker repo `yalin-demo-xray-local` on `solenglatest.jfrog.io`.

## Run locally

```bash
docker build -t xray-demo-app .
docker run --rm -p 8080:8080 xray-demo-app
curl localhost:8080/health
```

## CI

`.github/workflows/docker-build.yml` runs on push to `main` and pushes
`solenglatest.jfrog.io/yalin-demo-xray-local/xray-demo-app:<sha>` and `:latest`.

Required repository secrets:

| Secret | Value |
|---|---|
| `JF_USER` | Artifactory username (or email) |
| `JF_TOKEN` | Access token / API key with deploy permission on `yalin-demo-xray-local` |

## Xray

Make sure the repository is indexed by Xray (Administration → Xray Settings → Indexed Resources). After the first push, open the image under the repo in Artifactory → *Xray Data* to see the findings.
