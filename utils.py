APP_NAME = "PAK ENERGY & TECH HUB"
APP_VERSION = "1.0"



def app_information():

    return (
        f"{APP_NAME}\n"
        f"Version: {APP_VERSION}\n"
        "Petroleum Engineering Mobile Toolkit\n"
        "Developed by Paul"
    )



def is_number(value):

    try:
        float(value)
        return True

    except:
        return False