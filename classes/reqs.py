import re

class Requirements:
    program_name=""
    cpu=""
    ram=""
    gpu=""
    keywords=""
    ssd=""

    def __init__(self, program_name="", cpu="", ram="", gpu="", ssd="", keywords=""):
        program_name = re.sub(r'[™®]', '', program_name)
        self.program_name = program_name.lower().strip()
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.ssd = ssd
        keywords = re.sub('\n', ',', keywords)
        keywords = re.sub('\.', '', keywords)
        keywords = re.sub(r'[™®]', '', keywords)
        keywords = [kword.strip() for kword in keywords.lower().split(",")]
        self.keywords = [kword for kword in keywords if kword != ""]