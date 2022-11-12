# Setup

## Creating the initial app skeleton

Does not need to be done again.

```
npm install -g @angular/cli

cd angular_client
ng new --minimal --directory=. --routing --style=scss angular_client
ng add angular-auth-oidc-client \
  --flow-type "OIDC Code Flow PKCE using refresh tokens" \
  --authority-url-or-tenant-id "http://localhost:8080/realms/myrealm/protocol/openid-connect/token"
```

## Starting the application

Start using `ng serve --open`.

## Further Reading

* [Angular CLI](https://angular.io/cli)
* [angular-auth-oidc-client samples](https://angular-auth-oidc-client.com/docs/samples/samples)
* [angular-auth-oidc-client pkce with refresh token sample](https://github.com/damienbod/angular-auth-oidc-client/tree/main/projects/sample-code-flow-refresh-tokens)
