# fastapi-oidc

## Purpose

Demonstrate how to use OIDC with PKCE with keycloak, fastapi and angular. 

## Setup

Install miniconda and install the environment with `conda env create -f environment.yml`. 
Update with `conda env update -f environment.yml`.

Install pre-commit hooks: `pre-commit install`.

## Starting

Start [keycloak](./keycloak/README_KEYCLOAK.md).

Start the python api server with `python -m fastapi_oidc.main`. Documentation on using 
SwaggerUI can be found in [fastapi oidc](./fastapi_oidc/README_FASTAPI.md).

Then start the [angular app](./angular_client/README_ANGULAR.md).

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
* [oidc-client-ts](https://github.com/authts/oidc-client-ts)

## Further Reading

OpenID Connect:
* [OpenID Connect Documentation](https://openid.net/connect/)
* [Certified OpenID Connect Implementations](https://openid.net/developers/certified/)
* [OAuth 2.0 and OpenID Connect Overview (Okta)](https://developer.okta.com/docs/concepts/oauth-openid/)
* [An Illustrated Guide to OAuth and OpenID Connect (Okta)](https://developer.okta.com/blog/2019/10/21/illustrated-guide-to-oauth-and-oidc) 
* [Implement the OAuth 2.0 Authorization Code with PKCE Flow (Okta)](https://developer.okta.com/blog/2019/08/22/okta-authjs-pkce)

Validation of the Access Token
* [Validating Access Tokens (Auth0)](https://auth0.com/docs/secure/tokens/access-tokens/validate-access-tokens)
* [Token Introspection Endpoint (Okta)](https://www.oauth.com/oauth2-servers/token-introspection-endpoint/)
* [mircoprofile-jwt for Interoperability between Identity and Service Providers](https://github.com/eclipse/microprofile-jwt-auth/blob/master/spec/src/main/asciidoc/interoperability.asciidoc)

Keycloak:
* [Running Keycloak in a Container](https://www.keycloak.org/server/containers)
* [Getting Started Docker](https://www.keycloak.org/getting-started/getting-started-docker)
* [Automatically Importing a Realm](https://keepgrowing.in/tools/keycloak-in-docker-2-how-to-import-a-keycloak-realm/)

JWT:
* [RFC7519 describing jwt](https://www.rfc-editor.org/rfc/rfc7519.html)
