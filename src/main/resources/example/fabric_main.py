from com.mojang.authlib import GameProfile
from net.minecraft.client import Minecraft
from net.minecraft.core import Registry
from net.minecraft.core.registries import Registries
from net.minecraft.resources import Identifier
from net.minecraft.world.level.block import Block
from net.minecraft.world.level.block.state import BlockBehaviour_Properties
from org.slf4j import LoggerFactory

LOGGER = LoggerFactory.getLogger("example:py")


def init():
    LOGGER.info("Hello from Fabric on Python!")

    Registry.register(Registries.BLOCK, Identifier.fromNamespaceAndPath("example", "block"), Block(BlockBehaviour_Properties()))


def onInitialize(self) -> None:
    print("Hello Fabric world!")

    client = Minecraft.getInstance()
    game_profile: GameProfile = client.getGameProfile()
    name: str = game_profile.name()

    print("Hello {}!", name)

    # TODO Add this when we actually can create and register a block
    init()
