from os import path
import platform
import subprocess
from typing import Dict

from .objects import *
from .connection import start_connection, CustomConnection

HOST_IP = '127.0.0.1'
HOST_PORT = 47982

DEV_MODE = False

DEV_PROXY_FOLDER = "/home/dani/hass-integration/proxy/cmake-build-debug"
PROXY_FOLDER = path.join(path.dirname(path.realpath(__file__)), "bin") if not DEV_MODE else DEV_PROXY_FOLDER
PROXY_NAME = "proxy-arm" if "arm" in platform.machine() else "proxy-x86-64"
PROXY_BIN = path.join(PROXY_FOLDER, PROXY_NAME)


class IngeniumAPI:
    _user: str
    _pass: str
    _host: str

    _is_knx: bool
    _objects: List[IngObject] = []
    _connection: CustomConnection
    _proxy: subprocess.Popen

    def __init__(self, data: Dict[str, str]):
        self._user = data["username"].strip() if "username" in data else None
        self._pass = data["password"].strip() if "password" in data else None
        self._host = data["host"].strip() if "host" in data else None

    def login(self):
        if self._host is not None:
            params = [PROXY_BIN, "login", self._host]
        else:
            params = [PROXY_BIN, "login", self._user, self._pass]

        p = subprocess.Popen(params, cwd=PROXY_FOLDER, universal_newlines=True)
        return p.wait()

    async def load(self, saved_contents: str):
        if self._host is not None:
            params = [PROXY_BIN, "proxy", self._host]
        else:
            params = [PROXY_BIN, "proxy", self._user, self._pass]

        self._proxy = subprocess.Popen(params, cwd=PROXY_FOLDER, universal_newlines=True)

        await asyncio.sleep(5)
        self._parse_instal(path.join(PROXY_FOLDER, "Instal.dat"))

        await start_connection(self, HOST_IP, HOST_PORT)
        return saved_contents

    @property
    def is_remote(self) -> bool:
        return self._host is None

    @property
    def is_knx(self) -> bool:
        return self._is_knx

    @property
    def objects(self) -> List[IngObject]:
        return self._objects

    @property
    def connection(self) -> CustomConnection:
        return self._connection

    async def send(self, p: Package):
        return await self.connection.send(p)

    def close(self):
        self.connection.close()
        self._proxy.terminate()

    def _parse_instal(self, file_name: str):
        self._objects = []

        comp = IngComponent()
        line_number = 0
        self._is_knx = False  # 0-busing, 1-knx

        component_error = False

        with open(file_name) as file:
            for line in file:
                line = line.strip()
                if len(line) == 0:
                    continue

                if line_number == 0 and "KNX" in line:
                    self._is_knx = True
                    line_number += 1
                    continue

                if not self._is_knx:  # busing
                    line_mod = line_number % 8

                    if line_mod == 0:
                        # comp = {'map': int(line)}
                        comp = IngComponent()
                        component_error = False
                    elif line_mod == 1:
                        comp.label = line
                    elif line_mod == 2:
                        pass  # comp.pos_x = int(line)
                    elif line_mod == 3:
                        pass  # comp.pos_y = int(line)
                    elif line_mod == 4:
                        try:
                            comp.address = int(line)
                        except ValueError:
                            comp.real1 = float(line)
                    elif line_mod == 5:
                        comp.output = int(line)
                    elif line_mod == 6:
                        try:
                            comp.type = IngComponentType(int(line))
                        except ValueError:
                            component_error = True

                    elif line_mod == 7:
                        if not component_error:
                            comp.icon = int(line)
                            self.insert_component(comp)

                else:  # knx
                    pass

                line_number += 1

        # Filter repeated objects
        for o in self._objects:
            o.components = list(dict.fromkeys(o.components))

    def insert_component(self, comp: IngComponent):
        exists = False
        for obj in self._objects:
            if obj.address == comp.address and obj.type == comp.type:
                exists = True
                obj.components.append(comp)

        """
        if comp.address == 0 and comp.type.isCodKAFermax():
            intrusionType = FERMAX
            return
        """

        if not exists:
            if comp.type.is_actuator():
                self._objects.append(IngActuator(self, self._is_knx, comp.address, comp.type, [comp]))
            elif comp.type.is_meterbus():
                self._objects.append(IngMeterBus(self, self._is_knx, comp.address, comp.type, [comp]))
            elif comp.type.is_tsif():
                self._objects.append(IngSif(self, self._is_knx, comp.address, comp.type, [comp]))
            elif comp.type.is_busing_regulator():
                self._objects.append(IngBusingRegulator(self, self._is_knx, comp.address, comp.type, [comp]))
            elif comp.type.is_thermostat():
                self._objects.append(IngThermostat(self, self._is_knx, comp.address, comp.type, [comp]))
