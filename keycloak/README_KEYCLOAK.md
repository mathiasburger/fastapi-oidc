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

Certs

```
{
    "keys": [
        {
            "kid": "YEfRXx0Q9F64e14yvy-pY0A0zWKEfJuS6X7FsE2rBCU",
            "kty": "RSA",
            "alg": "RS256",
            "use": "sig",
            "n": "rbuRWmi_NZ-0Q0g24ud0O8doTG0cKgeIoaP6Rhcg3QIX8ytdMCBsUI1Enu2DiXaUfbuaGSrVG-JGv1CYnc8GALC98zisboD8hTVQLcaiIfW3t4yFLQeo_GdiDSFPGJx3xxcaqaxoJYO8pUa4ivZh5WBAMqMlIU5p39lc9Crw2D8MUt_AYj1F9SXbWFS0NCS0PdietYiJun997rKKWyBw1KV50o0CIGpoCYPxhcjv5hIacIodTIw3yAk-M0J0WugG31OmqWTUFJprUtyG511BaPJ6PMkwdA60xDSJR3P2Qmz4soI-h4mFize4ec8o2dw_0RDE7HQwqUscS5ynqVlzKw",
            "e": "AQAB",
            "x5c": [
                "MIICnTCCAYUCBgGEcDIdfTANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdteXJlYWxtMB4XDTIyMTExMzA4NTIyM1oXDTMyMTExMzA4NTQwM1owEjEQMA4GA1UEAwwHbXlyZWFsbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK27kVpovzWftENINuLndDvHaExtHCoHiKGj+kYXIN0CF/MrXTAgbFCNRJ7tg4l2lH27mhkq1RviRr9QmJ3PBgCwvfM4rG6A/IU1UC3GoiH1t7eMhS0HqPxnYg0hTxicd8cXGqmsaCWDvKVGuIr2YeVgQDKjJSFOad/ZXPQq8Ng/DFLfwGI9RfUl21hUtDQktD3YnrWIibp/fe6yilsgcNSledKNAiBqaAmD8YXI7+YSGnCKHUyMN8gJPjNCdFroBt9Tpqlk1BSaa1LchuddQWjyejzJMHQOtMQ0iUdz9kJs+LKCPoeJhYs3uHnPKNncP9EQxOx0MKlLHEucp6lZcysCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAeqB1OiJmdAG+S2AEdzQMuQet6CF95drwY+k7v2XiXR4io6alMpoVcU+00R9BD0CFHHAq+DiKIVU6BZvSHFaoR/aR7SI2lDjUTAjRBJF4AjQBsQjCSgQsRPNDM9H2MLe/055nJ9Fujl7myKODXdo/r2nQ2T52438xQhO4rvu7LLG/d5JGLhRe9l8j7qIWk5qAl80LEYDGf+585eKCKxvVFUKspLwBzTSHQhaViNWpk8MQXuQL5o/AHDr0LN7INqgN17SzuXx3U1Tr655CE9RbslXk+5TBOGVmsu00R4izi4HsopP07BlADGByzf28dXhdYcLer15mJGzvaLhKW79Tqg=="
            ],
            "x5t": "xObjFQ7NDj3twTNCoTA9wrgdy0s",
            "x5t#S256": "D3dt3m7QkOLrK2HUJeQ6mBg_x7wSXWwnMLp9PaaZwz0"
        },
        {
            "kid": "i-ucu2yj9H26Ug1kpK9Jo82sfCKzQWyusEBx9VhenOQ",
            "kty": "RSA",
            "alg": "RSA-OAEP",
            "use": "enc",
            "n": "wYoczvw_NhRpKqk888tagqtkMh1LBZ7mgSWrRVJ-cun1zcGEtgpv-wnWbobRGhSw95O80hXixEkeBR8E1m4T8nbHiEWM5S2GartDX9QncC0IYIKWmvSr0MEGtFQkYrDM5R-Wmb7clNOBOCLcLWp_C-Q-K_Wk0Y28umT_pAFBiXPK6a5sx52ZjDMEX6NHuG2zY3edr03CZviqJCzEc9uxE3EP25MVVoNSM7HMSsykjlXO8IYVg4Pcq7BI9wU4-ETQD1NkncSTN5lwyvH2dshYVI_gsug3IbCTBRnY5GO_yVSc_inAQR6a5l6L6HKAnDE4tOHr4S1NgBt9mSvarrDBPQ",
            "e": "AQAB",
            "x5c": [
                "MIICnTCCAYUCBgGEcDIcHzANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdteXJlYWxtMB4XDTIyMTExMzA4NTIyM1oXDTMyMTExMzA4NTQwM1owEjEQMA4GA1UEAwwHbXlyZWFsbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMGKHM78PzYUaSqpPPPLWoKrZDIdSwWe5oElq0VSfnLp9c3BhLYKb/sJ1m6G0RoUsPeTvNIV4sRJHgUfBNZuE/J2x4hFjOUthmq7Q1/UJ3AtCGCClpr0q9DBBrRUJGKwzOUflpm+3JTTgTgi3C1qfwvkPiv1pNGNvLpk/6QBQYlzyumubMedmYwzBF+jR7hts2N3na9Nwmb4qiQsxHPbsRNxD9uTFVaDUjOxzErMpI5VzvCGFYOD3KuwSPcFOPhE0A9TZJ3EkzeZcMrx9nbIWFSP4LLoNyGwkwUZ2ORjv8lUnP4pwEEemuZei+hygJwxOLTh6+EtTYAbfZkr2q6wwT0CAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAmNf5fZ4fA9+KSF8uVgEGs6Fh6P2Tpqk+aX3ywyLiUhpUAciEArsg1lh9DtbjhA6AeECwyb8BjKXDrqMNw7rNni3vLnbMJE5tGoHB/tGHpHgJXzGrDmjLUomPhyOttisX4Z4JHLt6BEXlYkXfThBVl+ZdBCBN0eaeiit/VKfi2nPxabeYHjwawP3MbOlwxWTkNWMq8lXLSy2/n2iEAGhHI0I9ec52iu0YnB9waDsgRy0K5Rvu8oUyIHlHF/V9XWT1gTT/EoJk8tdREXLoAEsnjBqIYAXR5lYF417j4x2sYFTI0A/A3XOeTEnmTw2g6U22LCyVr6H2cCHVR583cgcL+A=="
            ],
            "x5t": "ly-9SAXK9UgD5um-v44QNCAbZNg",
            "x5t#S256": "pxBk2ensKFaOL-kascj5kIKLDuEHkE-Kxu640XTZDdI"
        }
    ]
}
```
