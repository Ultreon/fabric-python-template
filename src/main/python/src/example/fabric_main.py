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
import sys
from typing import Callable, override

from com.mojang.authlib import GameProfile
from java.util.function import Function
from net.minecraft.client import Minecraft
from net.minecraft.core import Registry, BlockPos
from net.minecraft.core.registries import Registries, BuiltInRegistries
from net.minecraft.resources import Identifier, ResourceKey
from net.minecraft.sounds import SoundSource, SoundEvents
from net.minecraft.world import InteractionResult
from net.minecraft.world.entity.player import Player
from net.minecraft.world.item import Item, BlockItem
from net.minecraft.world.level import Level
from net.minecraft.world.level.block import Block, SoundType
from net.minecraft.world.level.block.state import BlockState, BlockBehaviour, StateDefinition
from net.minecraft.world.level.block.state.properties import BooleanProperty
from net.minecraft.world.phys import BlockHitResult
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
    Registry.register(BuiltInRegistries.ITEM, item_key, item)
    return item


class CustomBlock(Block):
    ACTIVATED = BooleanProperty.create("activated")

    def __init__(self, settings: BlockBehaviour.Properties):
        super().__init__(settings)

        self.registerDefaultState(self.defaultBlockState().setValue(CustomBlock.ACTIVATED, False))

    @override
    def createBlockStateDefinition(self, builder: StateDefinition.Builder) -> StateDefinition.Builder:
        return super().createBlockStateDefinition(builder.add(CustomBlock.ACTIVATED))

    # noinspection PyUnusedLocal
    @override
    def useWithoutItem(self, state: BlockState, world: Level, pos: BlockPos, player: Player,
                       hit: BlockHitResult) -> InteractionResult:
        if not player.getAbilities().mayBuild:
            return InteractionResult.PASS
        else:
            activated = state.getValue(CustomBlock.ACTIVATED)
            world.setBlockAndUpdate(pos, state.setValue(CustomBlock.ACTIVATED, not activated))
            world.playSound(player, pos, SoundEvents.COMPARATOR_CLICK, SoundSource.BLOCKS, 1.0, 1.0)
            return InteractionResult.SUCCESS


def register_block(path: str, factory: Callable[[BlockBehaviour.Properties], Block], settings: Block.Properties, should_register_item: bool = True) -> Block:
    block_key = key_of_block(path)
    block = factory(settings.setId(block_key))

    if should_register_item:
        item_key = key_of_item(path)
        block_item = BlockItem(block, Item.Properties().setId(item_key).useBlockDescriptionPrefix())
        Registry.register(BuiltInRegistries.ITEM, item_key, block_item)

    Registry.register(BuiltInRegistries.BLOCK, block_key, block)
    return block


def init():
    LOGGER.info("Hello from Fabric on Python!")

    # TutorialBlocks.example_block = register("example_block", lambda props: Block(props), BlockBehaviour.Properties.of().strength(4.0))
    register_item("suspicious_substance", lambda props: Item(props), Item.Properties())
    of = Block.Properties.of()
    register_block("prismarine_lamp", lambda props: CustomBlock(props), of.sound(SoundType.GLASS))


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
