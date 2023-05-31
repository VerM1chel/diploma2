
class Requirements:
    program_name=""
    cpu=""
    ram=""
    gpu=""
    ssd=""
    keywords=""

    def __init__(self, program_name="", cpu="", ram="", gpu="", ssd="", keywords=""):
        self.program_name = program_name.lower().strip()
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.ssd = ssd
        self.keywords = [kword.strip() for kword in keywords.lower().split(",")]