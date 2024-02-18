# -*- coding: utf-8 -*-
# Copyright (c) 2024 Benedikt Priller & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for NanoPi NEO Core 3 board with/without Mini Shield
(see https://wiki.friendlyelec.com/wiki/index.php/NanoPi_NEO3#Layout)

Usage:

.. code:: python
   import nanopi.neo3
   from OPi_GPIO.OPi import GPIO

   GPIO.setmode(nanopi.neo3.BOARD)
"""

# GPIOx_yz; x = group_number, y = letter, z = pin_number
# pin number = group_number * 32 + (letter * pin_number) + letter - 1
# Example: GPIO2_A2 = 2 * 32 + 7 = 39

# NanoPi NEO 3 physical board pin to GPIO pin
BOARD = {
    7:   66,    # GPIO2_A2/IR_RX - M21
    8:  100,    # GPIO3_A4/UART1_TX - E2
    10: 102,    # GPIO3_A6/UART1_RX - F2
    11: 79,     # GPIO2_B7/I2S1_MCLK - N18
    12: 83,     # GPIO2_C3/I2S1_SDI - U16
    13: 81,     # GPIO2_C1/I2S1_LRCK_TX - P18
    15: 82,     # GPIO2_C2/I2S1_SCLK - R18
    16: 101,    # GPIO3_A5/UART1_RTSN - D1
    18: 103,    # GPIO3_A7/UART1_CTSN - F1
    19: 97,     # GPIO3_A1/SPI_TXD - D2
    21: 98,     # GPIO3_A2/SPI_RXD - E1
    22: 87,     # GPIO2_C7/I2S1_SDO - N17
    23: 96,     # GPIO3_A0/SPI_CLK - E3
    24: 104,    # GPIO3_B0/SPI_CSN0 - F3
    26: 27,     # GPIO0_D3/SPDIF_TX - V9
}
