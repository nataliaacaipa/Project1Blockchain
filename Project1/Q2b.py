from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import P2PKH_scriptPubKey
from Q2a import Q2a_txout_scriptPubKey


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.0009 -  0.00003# amount of BTC in the output you're sending minus fee
txid_to_spend = (
        '63a6898434e2de2cb06635804432023b7783060fcc73ea9162f0a1a16e1eba17')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q2a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 2a.
txin_scriptSig = [
        12, 4
]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)

"""
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "feeaf37b5f575b005dfab2d9db164dfef0034da305711ef0e9e8a30386ba0381",
    "addresses": [
      "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
    ],
    "total": 87000,
    "fees": 3000,
    "size": 87,
    "vsize": 87,
    "preference": "low",
    "relayed_by": "88.12.12.38",
    "received": "2022-10-24T08:20:42.87777925Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "63a6898434e2de2cb06635804432023b7783060fcc73ea9162f0a1a16e1eba17",
        "output_index": 0,
        "script": "5c54",
        "output_value": 90000,
        "sequence": 4294967295,
        "script_type": "unknown",
        "age": 0
      }
    ],
    "outputs": [
      {
        "value": 87000,
        "script": "76a9149b85c4d84f713a34a7e8a17c9b577e2c7320bc2588ac",
        "addresses": [
          "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
        ],
        "script_type": "pay-to-pubkey-hash"
      }
    ]
  }
}

"""