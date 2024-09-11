import requests
import os
from requests.exceptions import HTTPError

SOLARIANCE_USER    = os.environ.get("SOLARIANCE_USER")
SOLARIANCE_PWD     = os.environ.get("SOLARIANCE_PWD")
SYSTEM_ID          = os.environ.get("SYSTEM_ID")

SOLARIANCE_API_V1  = "https://api.solariance.de/v1"
USER_AUTH_WITH_PWD = "user/auth/pw"
FORECAST_POWER     = "forecast/power"
PV_SYSTEM_VIEW     = "system/view"


def solariance_api_call(method: str, endpoint: str, headers: dict, body: dict, params: dict) -> dict:
    """
    Makes an API call to the Solariance API.

    Args:
        method (str): The HTTP method to use for the API call.
        endpoint (str): The API endpoint to call.
        headers (dict): The headers to include in the API request.
        body (dict): The JSON body to include in the API request.
        params (dict): The query parameters to include in the API request.

    Returns:
        dict: The JSON response from the API call.

    Raises:
        HTTPError: If an HTTP error occurs during the API call.
        InvalidJSONError: If the JSON body is invalid.
        TypeError: If there is a type error while processing the API call.
        RequestException: If any other error occurs during the API call.
    """
    url = f"{SOLARIANCE_API_V1}/{endpoint}"
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=body,
            params=params
        )
        response.raise_for_status()
        return response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    return {}


def get_user_jwt_token(user: str, pwd: str) -> str:
    """
    Retrieves a JWT token for the specified user.

    Args:
        user (str): The username of the user.
        pwd (str): The password of the user.

    Returns:
        str: The JWT token obtained from the Solariance API.
    """

    response = solariance_api_call(
        method="POST",
        endpoint=USER_AUTH_WITH_PWD,
        headers={},
        body={
            "identity": user,
            "password": pwd
        },
        params={})

    return response.get("data").get("token")


def get_forecast_power(token: str, system_id: str) -> dict:
    """
    Retrieves the forecast power for a given system ID.

    Args:
        token (str): The authorization token.
        system_id (str): The ID of the system.

    Returns:
        dict: The forecast power response.
    """

    response = solariance_api_call(
        method="GET",
        endpoint=FORECAST_POWER,
        headers={
            "Authorization": token
        },
        body={},
        params={
            "system_id": system_id
        })

    return response


def get_system_view(token: str, system_id: str) -> dict:
    """
    Retrieves information about a PV system.

    Args:
        token (str): The authorization token for the API.
        system_id (str): The ID of the PV system.

    Returns:
        dict: The response containing information about the PV system.
    """

    response = solariance_api_call(
        method="GET",
        endpoint=PV_SYSTEM_VIEW,
        headers={
            "Authorization": token
        },
        body={},
        params={
            "system_id": system_id
        })

    return response


def main():
    """
    This is the main function that shows an example to get a user JWT token, 
    fetch information about the pv system and the forecasted power, and prints it.
    """
    token = get_user_jwt_token(SOLARIANCE_USER, SOLARIANCE_PWD)
    pv_system = get_system_view(token, SYSTEM_ID)
    print(f"View PV System {SYSTEM_ID}: {pv_system}\n")
    forecast_power = get_forecast_power(token, SYSTEM_ID)
    # Print the forecasted power for the first time period on the first day
    print(
        f"PV Power Forecast for {SYSTEM_ID}: {forecast_power.get('data').get('forecast')[0][0]}")


if __name__ == "__main__":
    main()
