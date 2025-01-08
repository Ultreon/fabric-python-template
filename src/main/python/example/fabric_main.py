from com.mojang.authlib import GameProfile
from net.fabricmc.api import ModInitializer
from net.minecraft.client import MinecraftClient
from org.slf4j import LoggerFactory

LOGGER = LoggerFactory.getLogger("example:py")


### TODO Add an example block to the registry


class ExampleMod(ModInitializer):
    def onInitialize(self):
        print("Hello Fabric world!")

        client = MinecraftClient.getInstance()
        game_profile: GameProfile = client.getGameProfile()
        name = game_profile.getName()

        print("Hello {}!", name)

        # TODO Add this when we actually can create and register a block
        # init()
