# fastapi-oidc

## Purpose

Demonstrate how to use OIDC with PKCE with fastapi and angular. 

It builds solely upon OIDC certified dependencies.

## Setup

Install miniconda and install the environment with `conda env create -f environment.yml`. 
Update with `conda env update -f environment.yml`.

Install pre-commit hooks: `pre-commit install`.

## Starting

Start the server with `python -m fastapi_oidc.main`.

### Keycloak

See [keycloak](./keycloak/README_KEYCLOAK.md).

## Certified Implementations of OIDC

OpenID Connect Provider (Authentication Server, supports PKCE):
* [oidc-op](https://github.com/IdentityPython/oidc-op)
* [oidc-op docs](https://oidcop.readthedocs.io/en/latest/)

OpenID Connect Relying Party (Client, e.g.Webapp, supports PKCE):
* [oidcrp](https://github.com/IdentityPython/JWTConnect-Python-OidcRP)
* [oidcrp docs](https://oidcrp.readthedocs.io/en/latest/)

Angular OIDC Client (supports PKCE):
* [angular-auth-oidc-client](https://github.com/damienbod/angular-auth-oidc-client)

React OIDC (based upon certified oidc-client-js):
* [oidc-react](https://github.com/bjerkio/oidc-react)
* [oidc-client-js](oidc-client-js 1.3)

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
