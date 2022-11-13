from dataclasses import dataclass
from typing import Any, Callable, Dict, Iterable, List, Optional, Set, Union

from fastapi import HTTPException
from jose import JWTError, jwt
from jose.exceptions import JWTClaimsError
from starlette import status

from fastapi_oidc.oidc_configuration import OidcIdpConfiguration


@dataclass
class AccessTokenInfo:
    username: str
    groups: List[str]
    raw: Dict[str, Any]


def verify_token(
    token: str,
    verification_configuration: OidcIdpConfiguration,
    audience: Optional[str] = None,
    scopes: Optional[Union[str, Iterable[str]]] = None,
    authorized_party: Optional[Union[str, Iterable[str]]] = None,
    log_fn: Optional[Callable[[str, Exception], None]] = None,
) -> AccessTokenInfo:
    scopes_ = _to_set_of_str(scopes)
    authorized_party_ = _to_set_of_str(authorized_party)

    access_token = token.removeprefix("Bearer ")
    try:
        token_info = jwt.decode(
            access_token,
            verification_configuration.keys,
            verification_configuration.algorithms,
            audience=audience,
            issuer=verification_configuration.issuer,
            options={
                "verify_signature": True,
                "verify_aud": True,
                "verify_iat": True,
                "verify_exp": True,
                "verify_nbf": True,
                "verify_iss": True,
                "verify_sub": True,
                "verify_jti": True,
                "verify_at_hash": True,
                "require_aud": True,
                "require_iat": True,
                "require_exp": True,
                "require_nbf": False,
                "require_iss": True,
                "require_sub": True,
                "require_jti": True,
                "require_at_hash": False,
            },
        )

        if "azp" not in token_info:
            raise JWTError('missing required key "azp" among claims')

        if token_info["azp"] not in authorized_party_:
            raise JWTClaimsError(f"Wrong authorized party {token_info['azp']}")

        if "scope" not in token_info:
            raise JWTError('missing required key "scopes" among claims')

        missing_scopes = scopes_.difference(set(token_info["scope"].split(" ")))
        if missing_scopes != set():
            raise JWTClaimsError(f"Missing requested scope(s): {missing_scopes}")
    except JWTError as exception:
        if log_fn is not None:
            log_fn(str(exception), exception)

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return AccessTokenInfo(
        username=token_info["upn"], groups=token_info["groups"], raw=token_info
    )


def _to_set_of_str(audience: Optional[Union[str, Iterable[str]]]) -> Set[str]:
    if audience is None:
        return set()
    elif isinstance(audience, str):
        return {audience}
    elif isinstance(audience, Iterable):
        return set(audience)
    else:
        raise ValueError(f"Incompatible type: {type(audience)}")
