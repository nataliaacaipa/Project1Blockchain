from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2         # fill this in! #C 4 OP_2DUP OP_ADD 10 op_equalverify OP_SUB 8 OP_EQUAL

Q2a_txout_scriptPubKey = [OP_2DUP, OP_ADD, 16, OP_EQUALVERIFY, OP_SUB, 8, OP_EQUAL]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0012 - 0.0003 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '460fbb9794b98c103b003db30903c4ec80427b6c8ec11b6f16a6d7b296be8eae')
    utxo_index = 2 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)

"""
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "63a6898434e2de2cb06635804432023b7783060fcc73ea9162f0a1a16e1eba17",
    "addresses": [
      "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
    ],
    "total": 90000,
    "fees": 30000,
    "size": 173,
    "vsize": 173,
    "preference": "high",
    "relayed_by": "88.12.12.38",
    "received": "2022-10-24T08:13:37.573209099Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "460fbb9794b98c103b003db30903c4ec80427b6c8ec11b6f16a6d7b296be8eae",
        "output_index": 2,
        "script": "473044022049412444e7fc3db5261049232702198a20456b4c0ac35cb612af0f7c4147a846022062c929d97ee0859910c31e83648c6cc70e7a124c3754350401010c74f456ed06012103e561edcc7ae5f86a6ecc1f289bb762895877b9f1af138b65a90110e41dea39a9",
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
        "script": "6e936088945887",
        "addresses": null,
        "script_type": "unknown"
      }
    ]
  }
}

"""