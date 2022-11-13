import {Component, OnInit} from '@angular/core';
import {
  OidcClientNotification,
  OidcSecurityService,
  OpenIdConfiguration,
  UserDataResult
} from 'angular-auth-oidc-client';
import {catchError, Observable, throwError} from 'rxjs';
import {AsyncPipe, JsonPipe} from '@angular/common';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: 'home.component.html',
  providers: [
    JsonPipe, AsyncPipe
  ]
})
export class HomeComponent implements OnInit {
  configuration$: Observable<OpenIdConfiguration>;
  userDataChanged$: Observable<OidcClientNotification<any>>;
  userData$: Observable<UserDataResult>;
  isAuthenticated = false;
  userInfo: any = undefined;

  constructor(public oidcSecurityService: OidcSecurityService, private httpClient: HttpClient) {
  }

  ngOnInit() {
    this.configuration$ = this.oidcSecurityService.getConfiguration();
    this.userData$ = this.oidcSecurityService.userData$;

    this.oidcSecurityService.isAuthenticated$.subscribe(({isAuthenticated}) => {
      this.isAuthenticated = isAuthenticated;

      console.warn('authenticated: ', isAuthenticated);
    });
  }

  login() {
    this.oidcSecurityService.authorize();
  }

  refreshSession() {
    this.oidcSecurityService.forceRefreshSession().subscribe((result) => console.log(result));
  }

  logout() {
    this.oidcSecurityService.logoff();
  }

  logoffAndRevokeTokens() {
    this.oidcSecurityService.logoffAndRevokeTokens().subscribe((result) => console.log(result));
  }

  revokeRefreshToken() {
    this.oidcSecurityService.revokeRefreshToken().subscribe((result) => console.log(result));
  }

  revokeAccessToken() {
    this.oidcSecurityService.revokeAccessToken().subscribe((result) => console.log(result));
  }

  accessProtectedApiResource() {
    this.oidcSecurityService.getAccessToken().subscribe((token) => {
      const httpOptions = {
        headers: new HttpHeaders({
          Authorization: 'Bearer ' + token,
        }),
      };
      console.log("Requesting protected resource")
      this.httpClient.get("/api/protected", httpOptions).pipe(catchError((error: HttpErrorResponse) => {
        if (error.status === 0) { // A client-side or network error occurred
          console.error('An error occurred:', error.error);
        } else { // The backend returned an unsuccessful response code
          console.error(`Backend returned code ${error.status}, body was: `, error.error);
        }
        // Return an observable with a user-facing error message.
        return throwError(() => new Error('Something bad happened; please try again later.'));
      })).subscribe((data) => this.userInfo = data)
    });
  }
}
