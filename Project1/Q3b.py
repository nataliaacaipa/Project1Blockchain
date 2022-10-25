from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import P2PKH_scriptPubKey
from Q3a import (Q3a_txout_scriptPubKey, cust1_private_key, cust2_private_key,
                  cust3_private_key)


def multisig_scriptSig(txin, txout, txin_scriptPubKey):
    bank_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    cust1_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust1_private_key)
    cust2_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust2_private_key)
    cust3_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust3_private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was locked in the
    # multisig transaction created in Exercise 3a.
    return [
        OP_0, bank_sig, cust1_sig
    ]
    ######################################################################


def send_from_multisig_transaction(amount_to_send, txid_to_spend, utxo_index,
                                   txin_scriptPubKey, txout_scriptPubKey, network):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = multisig_scriptSig(txin, txout, txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0009 -  0.00003 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '60369564e29626262d93bf36c6253f6550a3c36ec79dbe6f659b904fa9ab709d')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txin_scriptPubKey = Q3a_txout_scriptPubKey
    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

    response = send_from_multisig_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txout_scriptPubKey, network_type)
    print(response.status_code, response.reason)
    print(response.text)

"""
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "d7185d23a3c68eb97e1f36929c60a71a195320b27c49d1012fc7631dfdfea23e",
    "addresses": [
      "zLD6yJ5mtVur5wYz9CwGNTgpsmJ2MXSrzg",
      "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
    ],
    "total": 87000,
    "fees": 3000,
    "size": 159,
    "vsize": 159,
    "preference": "low",
    "relayed_by": "88.12.12.38",
    "received": "2022-10-24T10:05:56.174771859Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "39389e988a07b447316de43f42ce8c8b9e535a9d1c5d93fdf57e00d9fed0f41f",
        "output_index": 0,
        "script": "00483045022100d5931ae1285c1d0f026b26059def5a90526303928232ca6229fd2ffc33c1b7160220558b2d294a0d31e73ffbb1cfc7cf46414418c3c349f62127040fa833e59f77f901",
        "output_value": 90000,
        "sequence": 4294967295,
        "addresses": [
          "zLD6yJ5mtVur5wYz9CwGNTgpsmJ2MXSrzg"
        ],
        "script_type": "pay-to-multi-pubkey-hash",
        "age": 2377967
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
 460fbb9794b98c103b003db30903c4ec80427b6c8ec11b6f16a6d7b296be8eae referenced by input 0 of dbc0dded60492526ad8065c8a89b77d3b4bcd3480e82ad93061d9d0a379b82d2 has already been spent.."}
nataliaacaipa@natalia-HP-Laptop:~/Downloads/Project1$ /bin/python3.9 /home/nataliaacaipa/Downloads/Project1/Project1/Q3a.py
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "60369564e29626262d93bf36c6253f6550a3c36ec79dbe6f659b904fa9ab709d",
    "addresses": [
      "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX",
      "zXbCvft4LbogSPZFRoJRpgmLhbj7H2nrGx"
    ],
    "total": 90000,
    "fees": 30000,
    "size": 305,
    "vsize": 305,
    "preference": "high",
    "relayed_by": "88.12.12.38",
    "received": "2022-10-24T11:00:26.099049766Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "460fbb9794b98c103b003db30903c4ec80427b6c8ec11b6f16a6d7b296be8eae",
        "output_index": 6,
        "script": "4730440220754b630cc354349934ab98735b99027de31153fcbceafdf8b177a131d71fbf0302200fe7478720aa2e3a19d83840f162f38667fc92d2e6155a686cef19fa078f591a012103e561edcc7ae5f86a6ecc1f289bb762895877b9f1af138b65a90110e41dea39a9",
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
        "script": "522103e561edcc7ae5f86a6ecc1f289bb762895877b9f1af138b65a90110e41dea39a921022828521c75f6331b2971bf6c80b18c465f504af571489c1a1259204a1f75e50721033672fe024dce94f9075745ff8e6193bc1a04472862726d85127daf5ca322bd052102828f4f45b0f6a63b921d6cb2f8fbea24d6f94d2ee2c78822109f8073adaf140d54ae",
        "addresses": [
          "zXbCvft4LbogSPZFRoJRpgmLhbj7H2nrGx"
        ],
        "script_type": "pay-to-multi-pubkey-hash"
      }
    ]
  }
}




201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "e5e0bf792554f912b5e96433b6e44d375dd5d77c6f64f66eb4800af52b39cb3e",
    "addresses": [
      "zXbCvft4LbogSPZFRoJRpgmLhbj7H2nrGx",
      "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
    ],
    "total": 87000,
    "fees": 3000,
    "size": 232,
    "vsize": 232,
    "preference": "low",
    "relayed_by": "88.12.12.38",
    "received": "2022-10-24T11:01:02.393726446Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "60369564e29626262d93bf36c6253f6550a3c36ec79dbe6f659b904fa9ab709d",
        "output_index": 0,
        "script": "00483045022100c5f7e0b59690da0598f7def1393ee8468654d8a22954392042cd9e3f333a142f02205e39cbb3187d3c2e855412ba13aa7e1398abc1bf8c624e6f08c7c27805c9713b01483045022100f8417b530b9b99a5d23a659a7c132da621d2a2471bb15488d2b9a321eee1fd210220291b125121e1a62ce3b452529e504682a26791087cfad6e5ee26b42b10ec09fa01",
        "output_value": 90000,
        "sequence": 4294967295,
        "addresses": [
          "zXbCvft4LbogSPZFRoJRpgmLhbj7H2nrGx"
        ],
        "script_type": "pay-to-multi-pubkey-hash",
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