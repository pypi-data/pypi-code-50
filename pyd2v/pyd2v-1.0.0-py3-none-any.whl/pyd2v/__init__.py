class D2V:

    def __init__(self):
        self.header = None
        self.settings = None
        self.data = None

    def parse(self, file_path):
        with open(file_path, mode="r", encoding="utf-8") as f:
            self.header = D2VHeader()
            self.header.parse(file_stream=f)
            self.settings = D2VSettings()
            self.settings.parse(file_stream=f)
            self.data = D2VData()
            self.data.parse(file_stream=f)

    def __repr__(self):
        return f"> D2V.header:\n{self.header}\n" \
               f"> D2V.settings:\n{self.settings}\n" \
               f"> D2V.data:\n(... truncated)"


class D2VHeader:

    def __init__(self):
        self.version = None
        self.videos = None

    def parse(self, file_stream):
        # Version
        self.version = file_stream.readline().strip()
        if not self.version.startswith("DGIndexProjectFile"):
            raise ValueError(f"Expected Version Header, received:\n\t{self.version}")
        self.version = self.version[18:]  # strip "DGIndexProjectFile"
        # Videos
        self.videos = []
        for n in range(int(file_stream.readline().strip())):
            self.videos.append(file_stream.readline().strip())
        # terminate
        if len(file_stream.readline().strip()) > 0:
            raise ValueError("Unexpected data after reading Header's Video List.")

    def __repr__(self):
        return f"version={self.version}\n" \
               f"videos={self.videos}"


class D2VSettings:

    def __init__(self):
        self.stream_type = None
        self.mpeg2_transport_pid = None
        self.transport_packet_size = None
        self.mpeg_type = None
        self.idct_algorithm = None
        self.yuvrgb_scale = None
        self.luminance_filter = None
        self.clipping = None
        self.aspect_ratio = None
        self.picture_size = None
        self.field_operation = None
        self.frame_rate = None
        self.location = None

    def parse(self, file_stream):
        while True:
            line = file_stream.readline().strip()
            if len(line) == 0:
                break
            line = line.split("=")
            if line[0] == "Stream_Type":
                self.stream_type = int(line[1])
            elif line[0] == "MPEG2_Transport_PID":
                line[1] = line[1].split(",")
                self.mpeg2_transport_pid = {
                    "Video": float(line[1][0]),
                    "Audio": float(line[1][1]),
                    "PCR": float(line[1][2])
                }
            elif line[0] == "Transport_Packet_Size":
                self.transport_packet_size = line[1].split(",")
            elif line[0] == "MPEG_Type":
                self.mpeg_type = int(line[1])
            elif line[0] == "iDCT_Algorithm":
                self.idct_algorithm = int(line[1])
            elif line[0] == "YUVRGB_Scale":
                self.yuvrgb_scale = int(line[1])
            elif line[0] == "Luminance_Filter":
                line[1] = line[1].split(",")
                self.luminance_filter = {
                    "Gamma": float(line[1][0]),
                    "Offset": float(line[1][1])
                }
            elif line[0] == "Clipping":
                self.clipping = [int(x) for x in line[1].split(",")]
            elif line[0] == "Aspect_Ratio":
                if "," in line[1]:
                    self.aspect_ratio = [(x if ":" in x else float(x)) for x in line[1].split(",")]
                else:
                    self.aspect_ratio = (line[1] if ":" in line[1] else float(line[1]))
            elif line[0] == "Picture_Size":
                self.picture_size = [int(x) for x in line[1].split("x")]
            elif line[0] == "Field_Operation":
                self.field_operation = int(line[1])
            elif line[0] == "Frame_Rate":
                line[1] = line[1].split(" ")
                self.frame_rate = [
                    line[1][0],
                    [int(x) for x in line[1][1].strip("()").split("/")]
                ]
            elif line[0] == "Location":
                line[1] = line[1].split(",")
                self.location = {
                    "StartFile": int(line[1][0]),
                    "StartOffset": int(line[1][1]),
                    "EndFile": int(line[1][2]),
                    "EndOffset": int(line[1][3])
                }
            else:
                raise ValueError(f"Unexpected data while reading D2V settings: {line}")

    def __repr__(self):
        return f"stream_type={self.stream_type}\n" \
               f"mpeg2_transport_pid={self.mpeg2_transport_pid}\n" \
               f"transport_packet_size={self.transport_packet_size}\n" \
               f"mpeg_type={self.mpeg_type}\n" \
               f"idct_algorithm={self.idct_algorithm}\n" \
               f"yuvrgb_scale={self.yuvrgb_scale}\n" \
               f"luminance_filter={self.luminance_filter}\n" \
               f"clipping={self.clipping}\n" \
               f"aspect_ratio={self.aspect_ratio}\n" \
               f"picture_size={self.picture_size}\n" \
               f"field_operation={self.field_operation}\n" \
               f"frame_rate={self.frame_rate}\n" \
               f"location={self.location}"


class D2VData:

    def __init__(self):
        self.frames = None
        self.data_type = None

    def parse(self, file_stream):
        self.frames = []
        while True:
            line = file_stream.readline().strip()
            if len(line) == 0:
                break
            line = line.split(" ", maxsplit=7)
            self.frames.append({
                "info": line[0],
                "matrix": line[1],
                "file": line[2],
                "position": line[3],
                "skip": line[4],
                "vob": line[5],
                "cell": line[6],
                "flags": line[7].split(" ")
            })
        self.data_type = file_stream.readline()[10:]

    def __repr__(self):
        return str(self.frames)
