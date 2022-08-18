from django.test import Client


# client is a fixture provided by django.test. It emulates HTTP requests so it is not necessary to use real requests
def test_status_code(client: Client):
    # Now, we use a call of GET type to call our VIEW.PY, which is based inside app root folder
    # use '/' to address ROOT
    resp = client.get('/')
    return resp.status_code == 200  # Code 200 refers to a successful result
