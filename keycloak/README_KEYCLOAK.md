# Keycloak

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

## Get endpoint configuration info

Use the following URL: `http://localhost:8080/realms/myrealm/.well-known/openid-configuration`.

## Token examples

ID Token (to be used only by the web application):

```
{
  "exp": 1668291458,
  "iat": 1668291158,
  "auth_time": 1668291158,
  "jti": "63b80f9e-d288-4cf5-b25f-32ab927709e2",
  "iss": "http://localhost:8080/realms/myrealm",
  "aud": "myclient",
  "sub": "ba8a7668-5250-4ab1-9880-566c42ebd599",
  "typ": "ID",
  "azp": "myclient",
  "nonce": "e04af1b19ca51c9f20335811ead522e6e0eDzilhW",
  "session_state": "2d0f4fc2-facc-4daf-a149-cc0d4e6a26b5",
  "at_hash": "rBI7O3SmpIBocjmQoQdQGQ",
  "acr": "1",
  "sid": "2d0f4fc2-facc-4daf-a149-cc0d4e6a26b5",
  "email_verified": false,
  "preferred_username": "myuser",
  "given_name": "",
  "family_name": ""
}
```

Access Token (to be used only for the resource server; not to be inspected by the web application):

```
{
  "exp": 1668291458,
  "iat": 1668291158,
  "auth_time": 1668291158,
  "jti": "1f078076-6ee3-474b-b0b4-500e6d146702",
  "iss": "http://localhost:8080/realms/myrealm",
  "aud": "account",
  "sub": "ba8a7668-5250-4ab1-9880-566c42ebd599",
  "typ": "Bearer",
  "azp": "myclient",
  "nonce": "e04af1b19ca51c9f20335811ead522e6e0eDzilhW",
  "session_state": "2d0f4fc2-facc-4daf-a149-cc0d4e6a26b5",
  "acr": "1",
  "allowed-origins": [
    "http://localhost:63342",
    "http://localhost:4200"
  ],
  "realm_access": {
    "roles": [
      "user"
    ]
  },
  "resource_access": {
    "account": {
      "roles": [
        "manage-account",
        "manage-account-links",
        "view-profile"
      ]
    }
  },
  "scope": "openid email profile",
  "sid": "2d0f4fc2-facc-4daf-a149-cc0d4e6a26b5",
  "email_verified": false,
  "preferred_username": "myuser",
  "given_name": "",
  "family_name": ""
}
```
