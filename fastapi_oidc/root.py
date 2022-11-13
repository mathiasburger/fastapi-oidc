import logging
from typing import Any, Dict

from fastapi import Depends, FastAPI
from fastapi.security import OpenIdConnect

from fastapi_oidc.oidc_access_token_verification import verify_token
from fastapi_oidc.oidc_configuration import get_oidc_idp_configuration

oidc = OpenIdConnect(
    openIdConnectUrl="http://localhost:8080/realms/myrealm/.well-known/openid-configuration"
)


def get_authorized_user(token: str = Depends(oidc)) -> str:  # noqa: B008
    # noinspection PyUnresolvedReferences
    verification_configuration = get_oidc_idp_configuration(oidc.model.openIdConnectUrl)  # type: ignore
    token_info = verify_token(
        token,
        verification_configuration,
        authorized_party="myclient",
        audience="account",  # todo: add service audience
        scopes={"profile"},  # todo: add service scope
        log_fn=lambda msg, exc: logging.getLogger("authorization").error(
            msg, exc_info=exc
        ),
    )
    return token_info.username


app = FastAPI(
    swagger_ui_init_oauth={
        "clientId": "myclient",
        "appName": "My Client",
        "usePkceWithAuthorizationCodeGrant": True,
        "scopes": "openid profile roles microprofile-jwt",
    }
)


@app.get("/")
async def root() -> Dict[str, Any]:
    return {"message": "Hello World"}


@app.get("/protected")
async def protected(user: str = Depends(get_authorized_user)) -> str:  # noqa: B008
    return user
