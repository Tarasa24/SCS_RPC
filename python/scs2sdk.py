import mmap
import struct


class scssdkclient:
    def update(self):
        self.mm = mmap.mmap(0, 1024, "Local\\SimTelemetryETS2")

        self.ets2_telemetry_plugin_revision = struct.unpack("I", self.mm[8:12])[0]

        self.ets2_version_major = struct.unpack("I", self.mm[12:16])[0]

        self.ets2_version_minor = struct.unpack("I", self.mm[16:20])[0]

        self.flags = self.mm[20:24]

        self.speed = struct.unpack("f", self.mm[24:28])[0]

        self.coordinateX = struct.unpack("f", self.mm[40:44])[0]

        self.coordinateY = struct.unpack("f", self.mm[44:48])[0]

        self.coordinateZ = struct.unpack("f", self.mm[48:52])[0]

        self.trailerMass = struct.unpack("f", self.mm[168:172])[0]

        self.trailerName = self.mm[236:300].decode("utf-8").replace("\x00", "")

        self.truckMake = self.mm[676:740].decode("utf-8").replace("\x00", "")

        self.truckModel = self.mm[804:868].decode("utf-8").replace("\x00", "")

        self.routeDistance = struct.unpack("f", self.mm[872:876])[0]

        self.mm.close()
