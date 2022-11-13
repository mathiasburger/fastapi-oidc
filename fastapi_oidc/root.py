import logging
from dataclasses import dataclass
from typing import Any, Dict, List

from fastapi import Depends, FastAPI
from fastapi.security import OpenIdConnect

from fastapi_oidc.oidc_access_token_verification import verify_token
from fastapi_oidc.oidc_configuration import get_oidc_idp_configuration

oidc = OpenIdConnect(
    openIdConnectUrl="http://localhost:8080/realms/myrealm/.well-known/openid-configuration"
)


@dataclass
class User:
    username: str
    groups: List[str]


def get_authorized_user(token: str = Depends(oidc)) -> User:  # noqa: B008
    # noinspection PyUnresolvedReferences
    verification_configuration = get_oidc_idp_configuration(oidc.model.openIdConnectUrl)  # type: ignore
    token_info = verify_token(
        token,
        verification_configuration,
        authorized_party="myclient",
        audience="myservice",
        scopes={"myservice"},
        log_fn=lambda msg, exc: logging.getLogger("authorization").error(
            msg, exc_info=exc
        ),
    )
    return User(token_info.username, token_info.groups)


app = FastAPI(
    swagger_ui_init_oauth={
        "clientId": "myclient",
        "appName": "My Client",
        "usePkceWithAuthorizationCodeGrant": True,
        "scopes": "openid profile roles microprofile-jwt myservice",
    }
)


@app.get("/")
async def root() -> Dict[str, Any]:
    return {"message": "Hello World"}


@app.get("/protected")
async def protected(user: User = Depends(get_authorized_user)) -> User:  # noqa: B008
    return user
