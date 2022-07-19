from binascii import unhexlify
import pytest
import wallycore as wally

def test_add_output():
    pset = wally.psbt_init(2, 0, 0, 0, wally.WALLY_PSBT_INIT_PSET)
    output0 = wally.tx_elements_output_init(
        unhexlify('0014b9bb6d06d82d2e4d9f9e8e6a9d23dacd715e81'),
        b'0' * 33,
        wally.tx_confidential_value_from_satoshi(1000),
    )

    len_asset_in_output = wally.tx_output_get_asset_len(output0) # = 33
    wally.psbt_add_tx_output_at(pset, 0, 0, output0) 
    len_asset_in_psbt = wally.psbt_get_output_asset_len(pset, 0) # = 0 ??
    
    assert len_asset_in_output == len_asset_in_psbt # fails
    
    b64 = wally.psbt_to_base64(pset, 0)
    print(b64)
    p = wally.psbt_from_base64(b64)
    # psbt_from_base64 raises "ValueError: Invalid argument"
    # decodepsbt elements RPC raises an error msg: "TX decode failed Output asset is required in PSET: iostream error"
    assert p is not None
