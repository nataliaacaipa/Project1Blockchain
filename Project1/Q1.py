from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)


def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction #OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
    return [
        OP_DUP, OP_HASH160, my_address , OP_EQUALVERIFY, OP_CHECKSIG 
    ]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction. #"<sig>,<pubKey>"
    return [
        signature, my_public_key 
    ]
    ######################################################################

def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(sender_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey,
        sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0012 - 0.0003 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '460fbb9794b98c103b003db30903c4ec80427b6c8ec11b6f16a6d7b296be8eae')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
    response = send_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        my_private_key,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)

"""
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "3bd43617c52bda11a15d19ef3b9399860adaa3bdb70c7fe8f0dca1807f8f8bff",
    "addresses": [
      "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
    ],
    "total": 90000,
    "fees": 30000,
    "size": 191,
    "vsize": 191,
    "preference": "high",
    "relayed_by": "88.12.12.38",
    "received": "2022-10-20T10:39:03.870088022Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "460fbb9794b98c103b003db30903c4ec80427b6c8ec11b6f16a6d7b296be8eae",
        "output_index": 0,
        "script": "47304402202af03b7e5f53a655d187fe267610f2be8caa121d19f44101b93c14d6f2ae3cd80220163755bcc0d47273dcc24738aa36a3c9df1ab4b015310359d1dec7cc43aafb1d012103e561edcc7ae5f86a6ecc1f289bb762895877b9f1af138b65a90110e41dea39a9",
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