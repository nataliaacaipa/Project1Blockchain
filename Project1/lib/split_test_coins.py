from bitcoin import SelectParams
from bitcoin.core import CMutableTransaction, x
from bitcoin.core.script import CScript, SignatureHash, SIGHASH_ALL
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH

from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from config import (my_private_key, my_public_key, my_address,
    faucet_address, network_type)

from utils import create_txin, create_txout, broadcast_transaction



def split_coins(amount_to_send, txid_to_spend, utxo_index, n, network):
    txin_scriptPubKey = address.to_scriptPubKey()
    txin = create_txin(txid_to_spend, utxo_index)
    txout_scriptPubKey = address.to_scriptPubKey()
    txout = create_txout(amount_to_send / n, txout_scriptPubKey)
    tx = CMutableTransaction([txin], [txout]*n)
    sighash = SignatureHash(txin_scriptPubKey, tx,
                            0, SIGHASH_ALL)
    txin.scriptSig = CScript([private_key.sign(sighash) + bytes([SIGHASH_ALL]),
                              public_key])
    VerifyScript(txin.scriptSig, txin_scriptPubKey,
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    response = broadcast_transaction(tx, network)
    print(response.status_code, response.reason)
    print(response.text)

if __name__ == '__main__':
    SelectParams('testnet')

    ######################################################################
    # TODO: set these parameters correctly
    private_key = CBitcoinSecret("cPywRZPjvBHAvB8aZw71J1hPF8tL3arqJhBsneRuEhQi5fc2tNgd")
    public_key = private_key.pub
    address = P2PKHBitcoinAddress.from_pubkey(public_key)

    amount_to_send = 0.01268228 - 0.00068228 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '2a2f865e412bc331c1305bd3ca89035d121cc6b1dd7907d8f08a25d6e789e97f')
    utxo_index = 0  # index of the output you are spending, indices start at 0
    n = 10  # number of outputs to split the input into
    # For n, choose a number larger than what you immediately need, 
    # in case you make mistakes.
    ######################################################################

    split_coins(amount_to_send, txid_to_spend, utxo_index, n, network_type)

"""
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "460fbb9794b98c103b003db30903c4ec80427b6c8ec11b6f16a6d7b296be8eae",
    "addresses": [
      "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
    ],
    "total": 1200000,
    "fees": 58228,
    "size": 497,
    "vsize": 497,
    "preference": "high",
    "relayed_by": "88.12.12.38",
    "received": "2022-10-20T10:09:41.601983115Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 10,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "2a2f865e412bc331c1305bd3ca89035d121cc6b1dd7907d8f08a25d6e789e97f",
        "output_index": 0,
        "script": "4730440220546032a6fe0d1636761152500e0a5077a91ebf3f06d194d8a09b6bd4a8309f8602204d13799a61122c865b5868790b7cd397d103d6b5cd1cc2be6263e116f4df0a58012103e561edcc7ae5f86a6ecc1f289bb762895877b9f1af138b65a90110e41dea39a9",
        "output_value": 1258228,
        "sequence": 4294967295,
        "addresses": [
          "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 2377422
      }
    ],
    "outputs": [
      {
        "value": 120000,
        "script": "76a9149b85c4d84f713a34a7e8a17c9b577e2c7320bc2588ac",
        "addresses": [
          "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
        ],
        "script_type": "pay-to-pubkey-hash"
      },
      {
        "value": 120000,
        "script": "76a9149b85c4d84f713a34a7e8a17c9b577e2c7320bc2588ac",
        "addresses": [
          "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
        ],
        "script_type": "pay-to-pubkey-hash"
      },
      {
        "value": 120000,
        "script": "76a9149b85c4d84f713a34a7e8a17c9b577e2c7320bc2588ac",
        "addresses": [
          "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
        ],
        "script_type": "pay-to-pubkey-hash"
      },
      {
        "value": 120000,
        "script": "76a9149b85c4d84f713a34a7e8a17c9b577e2c7320bc2588ac",
        "addresses": [
          "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
        ],
        "script_type": "pay-to-pubkey-hash"
      },
      {
        "value": 120000,
        "script": "76a9149b85c4d84f713a34a7e8a17c9b577e2c7320bc2588ac",
        "addresses": [
          "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
        ],
        "script_type": "pay-to-pubkey-hash"
      },
      {
        "value": 120000,
        "script": "76a9149b85c4d84f713a34a7e8a17c9b577e2c7320bc2588ac",
        "addresses": [
          "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
        ],
        "script_type": "pay-to-pubkey-hash"
      },
      {
        "value": 120000,
        "script": "76a9149b85c4d84f713a34a7e8a17c9b577e2c7320bc2588ac",
        "addresses": [
          "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
        ],
        "script_type": "pay-to-pubkey-hash"
      },
      {
        "value": 120000,
        "script": "76a9149b85c4d84f713a34a7e8a17c9b577e2c7320bc2588ac",
        "addresses": [
          "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
        ],
        "script_type": "pay-to-pubkey-hash"
      },
      {
        "value": 120000,
        "script": "76a9149b85c4d84f713a34a7e8a17c9b577e2c7320bc2588ac",
        "addresses": [
          "muhHHDTdvgUXbjPa3LLScQ4yjQTf2hDCuX"
        ],
        "script_type": "pay-to-pubkey-hash"
      },
      {
        "value": 120000,
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