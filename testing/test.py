#!/usr/bin/python3



from jk_testing import Assert

from jk_bincontainer import BinContainer





BYTE_BLOCKS = {
	"abcd": b"\x01\x02\x03",
	"defg": b"\x02\x03\x04",
	"yyyy": b"\x03\x04" * 123,
	"xxxx": b"\x03\x04" * 1024 * 512,
}



bc = BinContainer()
for k, v in BYTE_BLOCKS.items():
	bc.addBinaryBlock(k, v)
raw = bc.toBytes()

#print(raw)

bc2 = BinContainer()
bc2.loadFromData(raw)
bc2.dump()


for k, v in BYTE_BLOCKS.items():
	blockType, blockData = bc2.getBlockByKeyE(k)
	Assert.isEqual(v, blockData)






