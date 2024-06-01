import time

def handle_riot_api_error(riot_object):
    """
    This function handles the error codes returned by the Riot API.
    :param riot_object: The object returned by the Riot API.
    :return: True if the error code is handled, False otherwise.
    """
    if riot_object.status_code == 429:
        print(f"The following error code has been invoked:{riot_object.status_code} sleeping for 2 minutes")
        time.sleep(120)
        return True

    if riot_object.status_code == 400 or \
            riot_object.status_code == 403 or \
            riot_object.status_code == 401 or \
            riot_object.status_code == 404 or \
            riot_object.status_code == 405 or \
            riot_object.status_code == 415:
        print(f"The following error code has been invoked:{riot_object.status_code}")
        return True

    if riot_object.status_code == 500 or \
            riot_object.status_code == 502 or \
            riot_object.status_code == 503 or \
            riot_object.status_code == 504:
        print(f"The following error code has been invoked:{riot_object.status_code} sleeping for 2 minutes")
        time.sleep(10)
        return True

    return False