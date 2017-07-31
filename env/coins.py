class Monacoin(Coin):
    NAME = "Monacoin"
    SHORTNAME = "MONA"
    NET = "mainnet"
    XPUB_VERBYTES = bytes.fromhex("0488b21e")
    XPRV_VERBYTES = bytes.fromhex("0488ade4")
    P2PKH_VERBYTE = bytes.fromhex("32")
    P2SH_VERBYTES = [bytes.fromhex("37"), bytes.fromhex("05")]
    WIF_BYTE = bytes.fromhex("B2")
    GENESIS_HASH = ('ff9f1c0116d19de7c9963845e129f9ed'
                    '1bfc0b376eb54fd7afa42e0d418c8bb6')
    DESERIALIZER = DeserializerSegWit
    TX_COUNT = 2568580
    TX_COUNT_HEIGHT = 1029766
    TX_PER_BLOCK = 2
    RPC_PORT = 9402
    REORG_LIMIT = 1000


class Zaobi(Coin):
    NAME = "Zaobi"
    SHORTNAME = "ZB"
    NET = "mainnet"
    XPUB_VERBYTES = bytes.fromhex("0488B21E")
    XPRV_VERBYTES = bytes.fromhex("0488ADE4")
    P2PKH_VERBYTE = bytes.fromhex("36")
    P2SH_VERBYTES = [bytes.fromhex("08")]
    WIF_BYTE = bytes.fromhex("99")
    GENESIS_HASH = ('00060070755e09d835e3627a000d7064'
                    '662a91c3d2c297a2acb46124e1402511')
    DESERIALIZER = DeserializerTxTime
    DAEMON = LegacyRPCDaemon
    TX_COUNT = 34999
    TX_COUNT_HEIGHT = 30070
    TX_PER_BLOCK = 1
    IRC_PREFIX = "E_"
    IRC_CHANNEL = "#electrum-blk"
    RPC_PORT = 7294
    REORG_LIMIT = 5000
    HEADER_HASH = None

    @classmethod
    def header_hash(cls, header):
        '''Given a header return the hash.'''
        if cls.HEADER_HASH is None:
            import scrypt
            cls.HEADER_HASH = lambda x: scrypt.hash(x, x, 1024, 1, 1, 32)

        version, = struct.unpack('<I', header[:4])
        if version > 6:
            return super().header_hash(header)
        else:
            return cls.HEADER_HASH(header);


