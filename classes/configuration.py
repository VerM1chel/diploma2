
class Configuration:
    cpu = None
    cooler = None
    motherboard = None
    ram = None
    gpu = None
    ssd = None
    hdd = None
    power = None
    casePC = None
    def __init__(self, cpu=None, cooler=None, motherboard=None, ram=None, gpu=None, ssd=None, hdd=None, power=None, casePC=None):
        self.cpu = cpu
        if (cooler) is not None:
            self.cooler = cooler
        self.motherboard = motherboard
        self.ram = ram
        if (gpu) is not None:
            self.gpu = gpu
        self.ssd = ssd
        if (hdd) is not None:
            self.hdd = hdd
        if (power) is not None:
            self.power = power
        self.casePC = casePC