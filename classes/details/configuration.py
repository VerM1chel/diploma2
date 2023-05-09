from cpu import CPU
from cooler import Cooler
from motherboard import Motherboard
from ram import Ram
from gpu import Gpu
from ssd import Ssd
from hdd import Hdd
from case_PC import Case_PC
from power import Power
from monitor import Monitor
from speakers import Speakers
from mouse import Mouse
from keyboard import Keyboard
from wifi import Wifi
from bluetooth import Bluetooth

class Configuration:
    cpu = Cpu()
    cooler = Cooler()
    motherboard = Motherboard
    ram = Ram()
    gpu = Gpu()
    ssd = Ssd()
    hdd = Hdd()
    case = Case()
    power = Power()

    def __init__(self, cpu, cooler, motherboard, ram, gpu, ssd, hdd, case, power):
        self.cpu = cpu
        self.cooler = cooler
        self.motherboard = motherboard
        self.ram = ram
        self.gpu = gpu
        self.ssd = ssd
        self.hdd = hdd
        self.case = case
        self.power = power