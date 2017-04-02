# Nibe Downlink
Get variables from Nibe Uplink

# Requirements
Your heatpump should be registered in Nibe Uplink. This module fetches data from Nibe Uplink

# Installation

    pip install git+https://github.com/yozik04/nibe_downlink.git

# Usage

``` python
from pprint import pprint

from nibe_downlink import NibeDownlink

NIBE_UPLINK_CONF = {
  'username': "example@example.com",
  'password': "nibe_uplink_pass",
  "hpid": "99999", # heat pump id
  'variables': [47011,48132,47041,40008,40012,40015,40016,43005,43416,43420,43424,43136,43439,43437,40004,40013,10069] # variables you want to fetch
}

nd = NibeDownlink(**NIBE_UPLINK_CONF)

online, values = nd.getValues()

print "Is online: %s" % str(online)
pprint(values)
```

### Heat Pump ID: hpid
Get your **hpid** from Nibe Uplink web site. Open a heatpump and it's id will be in your address bar:
https://www.nibeuplink.com/System/**99999**/Status/Overview

### Variable IDs
See https://github.com/openhab/openhab1-addons/wiki/Nibe-Heat-Pump-Binding

# Examples

Copy *examples/config.py.dist* to *examples/config.py* and change settings inside the file

### Nibe Uplink -> MQTT bridge service

See *examples/mqtt.py*
