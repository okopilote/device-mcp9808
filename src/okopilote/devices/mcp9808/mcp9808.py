import board
import logging

import adafruit_mcp9808
import busio

from okopilote.devices.common.abstract import AbstractTemperatureSensor

logger = logging.getLogger(__name__)


def from_conf(conf):
    conf.setdefault("address", "0x18")
    addr = conf.get("address")
    if len(addr) > 2 and addr[0:2] == "0x":
        return MCP9808(address=int(addr, base=16))
    else:
        return MCP9808(address=int(addr))


class MCP9808(AbstractTemperatureSensor):

    def __init__(self, address=0x18):
        self.address = address
        self._dev = None

    def _init_dev(self):

        i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
        self._dev = adafruit_mcp9808.MCP9808(i2c, self.address)

    @property
    def temperature(self):
        """Read temperature in °C"""
        try:
            if not self._dev:
                self._init_dev()
            return self._dev.temperature
        except Exception as e:
            logger.exception(e)
            self._dev = None
            raise
