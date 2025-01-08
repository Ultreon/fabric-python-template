from com.mojang.authlib import GameProfile
from net.fabricmc.api import ModInitializer
from net.minecraft.client import MinecraftClient
from org.slf4j import LoggerFactory, Logger

LOGGER: Logger = LoggerFactory.getLogger("example")


class ExampleMod(ModInitializer):
    def onInitialize(self):
        print("Hello Fabric world!")

        client: MinecraftClient = MinecraftClient.getInstance()
        game_profile: GameProfile = client.getGameProfile()
        name: str = game_profile.getName()

        LOGGER.info("Hello {}!", name)
