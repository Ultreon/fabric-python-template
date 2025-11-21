#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A Python-based Minecraft Fabric mod example demonstrating block registration and initialization.

This module serves as an example of how to initialize and register custom blocks in a Minecraft
mod using Fabric API with Python. It includes an initialization process with logging for
verification of successful mod load and a greeting narrated by the player's in-game profile.

Classes:
    - TutorialBlocks: A simple class to hold references to custom registered blocks.

Functions:
    - register: Handles the registration of custom blocks within the game.
    - init: Initializes the mod, registers an example block, and sets up logging.
    - onInitialize: Entry point for mod initialization, handling the Minecraft client instance,
      logging, and error management.
"""
from typing import Callable

from java.util.function import Function

try:
    import sys
    from java.lang import Class
    from java.util.function import Function
    from com.mojang.authlib import GameProfile
    from net.minecraft.client import Minecraft
    from net.minecraft.core import Registry
    from net.minecraft.core.registries import Registries, BuiltInRegistries
    from net.minecraft.resources import Identifier, ResourceKey
    from net.minecraft.world.item import Item, BlockItem
    from net.minecraft.world.level.block import Block
    from net.minecraft.world.level.block.state import BlockBehaviour
    from org.slf4j import LoggerFactory

    LOGGER = LoggerFactory.getLogger("example:py")


    class TutorialBlocks:
        example_block = None


    def key_of_block(name: str) -> ResourceKey:
        return ResourceKey.create(Registries.BLOCK, Identifier.fromNamespaceAndPath("example", name))


    def key_of_item(name: str) -> ResourceKey:
        return ResourceKey.create(Registries.ITEM, Identifier.fromNamespaceAndPath("example", name))


    def register_item(name: str, item_factory: Callable[[Item.Properties], Item], settings: Item.Properties) -> Item:
        item_key = key_of_item(name)
        item = item_factory(settings.setId(item_key))
        return Registry.register(BuiltInRegistries.ITEM, item_key, item)


    def register(path: str, factory: Function, settings, should_register_item: bool = True) -> Block:
        block_key = key_of_block(path)
        block = factory(settings.setId(block_key))

        if should_register_item:
            item_key = key_of_item(path)
            block_item = BlockItem(block, Item.Properties().setId(item_key).useBlockDescriptionPrefix())
            Registry.register(BuiltInRegistries.ITEM, item_key, block_item)

        return Registry.register(BuiltInRegistries.BLOCK, block_key, block)


    def init():
        LOGGER.info("Hello from Fabric on Python!")

        # TutorialBlocks.example_block = register("example_block", lambda props: Block(props), BlockBehaviour.Properties.of().strength(4.0))
        register_item("suspicious_substance", lambda props: Item(props), Item.Properties())


    def onInitialize() -> None:
        try:
            client = Minecraft.getInstance()
            game_profile: GameProfile = client.getGameProfile()
            name: str = game_profile.name()

            LOGGER.info("Hello {}!", name)

            init()
        except Exception as e:
            print("Example mod failed to load!", file=sys.stderr)
            import traceback
            for line in "".join(traceback.format_exception(e)).splitlines():
                LOGGER.error(line)
            raise e
except BaseException as e:
    import traceback

    traceback.print_exception(e, file=sys.stderr)
    raise e
