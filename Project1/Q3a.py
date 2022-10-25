from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cTscWF1fVxHhNgTzpJ1tiiQexN972z7Q8kPphLr2XWVcssS2pkyw')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cTpkuYWKkpcAsajPS35pdpbvKBzUvKs3yu1MammReHUXwA82sS6R')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cNgJdoB6TwJUVRnG2insDL171FHNdAvW5udf4CEmVQ9RREFU8UBc')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
        OP_2, my_public_key, cust1_public_key, cust2_public_key, cust3_public_key, OP_4, OP_CHECKMULTISIG
]
#ejemplo: OP_1 04cc71eb30d653c0c3163990c47b976f3fb3f37cccdcbedb169a1dfef58bbfbfaff7d8a473e7e2e6d317b87bafe8bde97e3cf8f065dec022b51d11fcdd0d348ac4
#  0461cbdcc5409fb4b4d42b51d33381354d80e550078cb532a34bfa2fcfdeb7d76519aecc62770f5b0e4ef8551946d8a540911abe3e7854a26f39f58b25c15342af
#  OP_2 OP_CHECKMULTISIG
#Include an opcode M to indicate how many signatures are required.
#Include the public keys.
#Include another opcode N to indicate how many public keys there are.
#Put the CHECKMULTISIG opcode at the end.


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0012 - 0.0003 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '460fbb9794b98c103b003db30903c4ec80427b6c8ec11b6f16a6d7b296be8eae')
    utxo_index = 6 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)

"""
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "39389e988a07b447316de43f42ce8c8b9e535a9d1c5d93fdf57e00d9fed0f41f",
    "addresses": [
      "zLD6yJ5mtVur5wYz9CwGNTgpsmJ2MXSrzg",
      "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
    ],
    "total": 90000,
    "fees": 30000,
    "size": 271,
    "vsize": 271,
    "preference": "high",
    "relayed_by": "88.12.12.38",
    "received": "2022-10-24T09:35:55.23569693Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "460fbb9794b98c103b003db30903c4ec80427b6c8ec11b6f16a6d7b296be8eae",
        "output_index": 3,
        "script": "47304402207bfeda0ced1c8470de6ee38c93110be5521494191d9d94772486bbb044a79a1002202086ae219e39bc20002ed59fd0354772678f55775ae4102cb14709e69c8241f9012103e561edcc7ae5f86a6ecc1f289bb762895877b9f1af138b65a90110e41dea39a9",
        "output_value": 120000,
        "sequence": 4294967295,
        "addresses": [
          "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 2377433
      }
    ],
    "outputs": [
      {
        "value": 90000,
        "script": "5121022828521c75f6331b2971bf6c80b18c465f504af571489c1a1259204a1f75e50721033672fe024dce94f9075745ff8e6193bc1a04472862726d85127daf5ca322bd052102828f4f45b0f6a63b921d6cb2f8fbea24d6f94d2ee2c78822109f8073adaf140d53ae",
        "addresses": [
          "zLD6yJ5mtVur5wYz9CwGNTgpsmJ2MXSrzg"
        ],
        "script_type": "pay-to-multi-pubkey-hash"
      }
    ]
  }
}

"""