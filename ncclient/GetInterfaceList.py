import os
import sys
from ncclient import manager
import xmltodict
import xml.dom.minidom


# Create an XML filter for targeted NETCONF queries
netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface></interface>
  </interfaces>
</filter>"""

print("Opening NETCONF Connection to {}"
      .format("host: AirborneRouter-192.168.100.133"))

# Open a connection to the network device using ncclient
with manager.connect(
        host="192.168.100.133",
        port=830,
        username="COMET_admin",
        password="admin",
        hostkey_verify=False
        ) as m:

    print("Sending a <get-config> operation to the device.\n")
    # Make a NETCONF <get-config> query using the filter
    netconf_reply = m.get_config(source = 'running', filter = netconf_filter)

print("Here is the raw XML data returned from the device.\n")
# Print out the raw XML that returned
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
print("")

# Parse the returned XML to an Ordered Dictionary
netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

# Create a list of interfaces
interfaces = netconf_data["interfaces"]["interface"]

print("The interface status of the device is: ")
# Loop over interfaces and report status
for interface in interfaces:
    print("Interface {} enabled status is {}".format(
            interface["name"],
            interface["enabled"]
            )
        )
print("\n")