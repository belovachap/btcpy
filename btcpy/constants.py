from collections import namedtuple
from decimal import Decimal


Constants = namedtuple('Constants', [
    'base58_prefixes',
    'base58_raw_prefixes',
    'bech32_net_to_hrp',
    'bech32_hrp_to_net',
    'xkeys_prefixes',
    'xpub_version',
    'xprv_version',
    'wif_prefixes',
    'decimals',
])


BitcoinMainnet = Constants(
    base58_prefixes={
        '1': 'p2pkh',
        '3': 'p2sh',
    },
    base58_raw_prefixes={
        'p2pkh': bytearray(b'\x00'),
        'p2sh': bytearray(b'\x05'),
    },
    bech32_net_to_hrp='bc',
    bech32_hrp_to_net='mainnet',
    xkeys_prefixes='x',
    xpub_version=b'\x04\x88\xb2\x1e',
    xprv_version=b'\x04\x88\xad\xe4',
    wif_prefixes=0x80,
    decimals=Decimal(8),
)


BitcoinTestnet = Constants(
    base58_prefixes={
        'm': 'p2pkh',
        'n': 'p2pkh',
        '2': 'p2sh',
    },
    base58_raw_prefixes={
        'p2pkh': bytearray(b'\x6f'),
        'p2sh': bytearray(b'\xc4'),
    },
    bech32_net_to_hrp='tb',
    bech32_hrp_to_net='testnet',
    xkeys_prefixes='t',
    xpub_version=b'\x04\x35\x87\xcf',
    xprv_version=b'\x04\x35\x83\x94',
    wif_prefixes=0xef,
    decimals=Decimal(8),
)


PeercoinMainnet = Constants(
    base58_prefixes={
        'P': 'p2pkh',
        'p': 'p2sh',
    },
    base58_raw_prefixes={
        'p2pkh': bytearray(b'\x37'),
        'p2sh': bytearray(b'\x75'),
    },
    bech32_net_to_hrp='bc',
    bech32_hrp_to_net='mainnet',
    xkeys_prefixes='x',
    xpub_version=b'\x04\x88\xb2\x1e',
    xprv_version=b'\x04\x88\xad\xe4',
    wif_prefixes=0xb7,
    decimals=Decimal('1e6'),
)


PeercoinTestnet = Constants(
    base58_prefixes={
        'm': 'p2pkh',
        'n': 'p2pkh',
    },
    base58_raw_prefixes={
        'p2pkh': bytearray(b'\x6f'),
        'p2sh': bytearray(b'\xc4'),
    },
    bech32_net_to_hrp='tb',
    bech32_hrp_to_net='testnet',
    xkeys_prefixes='t',
    xpub_version=b'\x04\x35\x87\xcf',
    xprv_version=b'\x04\x35\x83\x94',
    wif_prefixes=0xef,
    decimals=Decimal('1e6'),
)
