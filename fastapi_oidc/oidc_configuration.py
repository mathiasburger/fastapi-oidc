import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List

import requests


@dataclass
class OidcIdpConfiguration:
    keys: List[Dict[str, Any]]
    algorithms: List[str]
    issuer: str

    @classmethod
    def from_dict(cls, data: dict) -> "OidcIdpConfiguration":
        return OidcIdpConfiguration(**data)

    @classmethod
    def from_file(cls, file: Path) -> "OidcIdpConfiguration":
        return cls.from_dict(json.loads(file.read_text(encoding="UTF-8")))


def get_oidc_idp_configuration(well_known_url: str) -> OidcIdpConfiguration:
    well_known_request = requests.get(well_known_url)
    well_known_request.raise_for_status()
    well_known = well_known_request.json()

    jwks_url = well_known["jwks_uri"]
    jwks_request = requests.get(jwks_url)
    jwks_request.raise_for_status()
    jwks = jwks_request.json()

    keys = jwks["keys"]
    algorithms = well_known["id_token_signing_alg_values_supported"]
    issuer = well_known["issuer"]

    return OidcIdpConfiguration(keys, algorithms, issuer)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--well_known_url",
        help="URL to the well known info endpoint describing the OIDC configuration",
        type=str,
        required=False,
        default="http://localhost:8080/realms/myrealm/.well-known/openid-configuration",
    )
    args = parser.parse_args()

    well_known_url = args.well_known_url
    configuration = get_oidc_idp_configuration(well_known_url)

    print(json.dumps(asdict(configuration), indent=2))  # noqa: T201
