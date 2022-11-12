import {NgModule} from '@angular/core';
import {AuthModule, LogLevel} from 'angular-auth-oidc-client';


@NgModule({
  imports: [AuthModule.forRoot({
    config: {
      authority: 'http://localhost:8080/realms/myrealm/protocol/openid-connect/token', // token url from
      authWellknownEndpointUrl: 'http://localhost:8080/realms/myrealm/.well-known/openid-configuration', // well known url
      redirectUrl: window.location.origin,
      postLogoutRedirectUri: window.location.origin,
      clientId: 'myclient', // client id
      scope: 'openid profile', // 'offline_access' scope requires user consent which needs to be enabled in auth server
      responseType: 'code',
      silentRenew: true,
      useRefreshToken: true,
      renewTimeBeforeTokenExpiresInSeconds: 30,
      logLevel: LogLevel.Debug,
      ignoreNonceAfterRefresh: true,
    }
  })],
  exports: [AuthModule],
})
export class AuthConfigModule {
}
