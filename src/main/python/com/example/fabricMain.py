# import the fabric api for mod initialization
from net.fabricmc.api import ModInitializer
from net.minecraft.client import MinecraftClient
from com.mojang.authlib import GameProfile
from org.slf4j import LoggerFactory
from org.slf4j import Logger
from pythonvm.api import implements

@implements(ModInitializer)
class ExampleMod:
    def on_initialize(self):
        print("Hello Fabric world!")

        client: MinecraftClient = MinecraftClient.getInstance()
        game_profile: GameProfile = client.getGameProfile()
        name: str = game_profile.getName()

        # logger: Logger = LoggerFactory.getLogger("fabric")
        # logger.info("Hello {}", name)

        print("Hello", name)
