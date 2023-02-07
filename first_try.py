import redfish

try:
    REDFISH_OBJ = redfish.redfish_client(base_url="https://sandboxdnac2.cisco.com", username="devnetuser", \
                      password="Cisco123")

except SyntaxError:
    pass

REDFISH_OBJ.login(auth="basic")

response = REDFISH_OBJ.get("/redfish/v1", None)