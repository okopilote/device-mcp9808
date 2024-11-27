# okopilote-devices-mcp9808

`okopilote-devices-mcp9808` provides a module to interface `okopilote-room`
software with the [MCP9808 I2C temperature sensor](https://www.adafruit.com/product/1782).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

### FUTUR: install packages from PyPi

```console
# Install sensor module as an optional dependency of okopilote-room
pip install okopilote-room[mcp9808]

# Or install it separately
pip install okopilote-devices-mcp9808
```

### PRESENT: build and install packages

Install package and dependencies from distribution files:

```console
pip install okopilote_devices_mcp9808-a.b.c-py3-none-any.whl
pip install okopilote_devices_common-d.e.f-py3-none-any.whl
```

## Usage

In the `devices.conf` file of `okopilote-room`, add a sensor section:
```ini
[sensor_1]
module = okopilote.devices.mcp9808
# Address on the I2C bus
address = 0x18
```

Senor may now be used in `rooms.conf` file of `okopilote-room`:
```ini
[room1]
label = Yannick's room
temperatur_sensor_device = sensor_1
```

## License

`okopilote-devices-mcp9808` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
