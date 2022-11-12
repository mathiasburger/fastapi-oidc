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
