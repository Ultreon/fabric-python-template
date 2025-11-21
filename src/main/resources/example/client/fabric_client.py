from net.fabricmc.api import ClientModInitializer
from pythonvm.api import implements


def onInitializeClient(self):
    print("Hello Fabric world!")
