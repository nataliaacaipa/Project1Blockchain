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
