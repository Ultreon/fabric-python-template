from net.fabricmc.api import ClientModInitializer
from pythonvm.api import implements


@implements(ClientModInitializer)
class ExampleModClient:
    def onInitializeClient(self):
        print("Hello Fabric world!")