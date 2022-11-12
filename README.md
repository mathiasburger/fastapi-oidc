# fastapi-oidc

## Purpose

Demonstrate how to use OIDC with fastapi.

## Setup

Install miniconda and install the environment with `conda env create -f environment.yml`. 
Update with `conda env update -f environment.yml`.

Install pre-commit hooks: `pre-commit install`.

## Starting

Start the server with `python -m fastapi_oidc.main`.

### Keycloak

Change to the keycloak directory with `cd keycloak`.
* Start: `docker-compose up`.
* Stop and remove data: `docker-compose rm -f -v`

Start the browser on 'http://localhost:8080'.

Configuration:
* Login to admin console: `http://localhost:8080/admin` with `admin`, `KcAdmin1234`.
* There is a realm `myrealm`.
  * Contains a user `myuser` with password `myuser`. 
  * Contains client `testclient` to be used with OIDC test page `https://www.keycloak.org/app/#url=http://localhost:8080&realm=myrealm&client=testclient`.
  * Contains client `myclient` to be used with OIDC + PKCE (S256) on `localhost:8000` (for the python client implementation provided in this repository).

## Certified Python Implementations of OIDC

OpenID Connect Provider (Authentication Server):
* [oidc-op](https://github.com/IdentityPython/oidc-op)
* [oidc-op docs](https://oidcop.readthedocs.io/en/latest/)

OpenID Connect Relying Party (Client, e.g.Webapp):
* [oidcrp](https://github.com/IdentityPython/JWTConnect-Python-OidcRP)
* [oidcrp docs](https://oidcrp.readthedocs.io/en/latest/)

## Further Reading

OpenID Connect:
* [OpenID Connect Documentation](https://openid.net/connect/)
* [Certified OpenID Connect Implementations](https://openid.net/developers/certified/)
* [OAuth 2.0 and OpenID Connect Overview (Okta)](https://developer.okta.com/docs/concepts/oauth-openid/)
* [An Illustrated Guide to OAuth and OpenID Connect (Okta)](https://developer.okta.com/blog/2019/10/21/illustrated-guide-to-oauth-and-oidc) 
* [Implement the OAuth 2.0 Authorization Code with PKCE Flow (Okta)](https://developer.okta.com/blog/2019/08/22/okta-authjs-pkce)

Keycloak:
* [Running Keycloak in a Container](https://www.keycloak.org/server/containers)
* [Getting Started Docker](https://www.keycloak.org/getting-started/getting-started-docker)
* [Automatically Importing a Realm](https://keepgrowing.in/tools/keycloak-in-docker-2-how-to-import-a-keycloak-realm/)
