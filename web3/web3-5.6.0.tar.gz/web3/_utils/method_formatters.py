import codecs
import operator
from typing import (
    Any,
    Callable,
    Collection,
    Dict,
    Iterable,
    Union,
)

from eth_utils.curried import (
    apply_formatter_at_index,
    apply_formatter_if,
    apply_formatter_to_array,
    apply_formatters_to_dict,
    apply_formatters_to_sequence,
    apply_one_of_formatters,
    is_address,
    is_bytes,
    is_dict,
    is_integer,
    is_null,
    is_string,
    remove_0x_prefix,
    text_if_str,
    to_checksum_address,
    to_list,
    to_tuple,
)
from eth_utils.toolz import (
    complement,
    compose,
    curried,
    curry,
    partial,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.abi import (
    is_length,
)
from web3._utils.encoding import (
    hexstr_if_str,
    to_hex,
)
from web3._utils.formatters import (
    hex_to_integer,
    integer_to_hex,
    is_array_of_dicts,
    is_array_of_strings,
    remove_key_if,
)
from web3._utils.normalizers import (
    abi_address_to_hex,
    abi_bytes_to_hex,
    abi_int_to_hex,
    abi_string_to_hex,
)
from web3._utils.rpc_abi import (
    RPC,
    RPC_ABIS,
    abi_request_formatters,
)
from web3.datastructures import (
    AttributeDict,
)
from web3.types import (
    RPCEndpoint,
    TReturn,
)


def bytes_to_ascii(value: bytes) -> str:
    return codecs.decode(value, 'ascii')


to_ascii_if_bytes = apply_formatter_if(is_bytes, bytes_to_ascii)
to_integer_if_hex = apply_formatter_if(is_string, hex_to_integer)
block_number_formatter = apply_formatter_if(is_integer, integer_to_hex)


is_false = partial(operator.is_, False)

is_not_false = complement(is_false)
is_not_null = complement(is_null)


@curry
def to_hexbytes(
    num_bytes: int, val: Union[str, int, bytes], variable_length: bool=False
) -> HexBytes:
    if isinstance(val, (str, int, bytes)):
        result = HexBytes(val)
    else:
        raise TypeError("Cannot convert %r to HexBytes" % val)

    extra_bytes = len(result) - num_bytes
    if extra_bytes == 0 or (variable_length and extra_bytes < 0):
        return result
    elif all(byte == 0 for byte in result[:extra_bytes]):
        return HexBytes(result[extra_bytes:])
    else:
        raise ValueError(
            "The value %r is %d bytes, but should be %d" % (
                result, len(result), num_bytes
            )
        )


def is_attrdict(val: Any) -> bool:
    return isinstance(val, AttributeDict)


not_attrdict = complement(is_attrdict)


TRANSACTION_FORMATTERS = {
    'blockHash': apply_formatter_if(is_not_null, to_hexbytes(32)),
    'blockNumber': apply_formatter_if(is_not_null, to_integer_if_hex),
    'transactionIndex': apply_formatter_if(is_not_null, to_integer_if_hex),
    'nonce': to_integer_if_hex,
    'gas': to_integer_if_hex,
    'gasPrice': to_integer_if_hex,
    'value': to_integer_if_hex,
    'from': to_checksum_address,
    'publicKey': apply_formatter_if(is_not_null, to_hexbytes(64)),
    'r': apply_formatter_if(is_not_null, to_hexbytes(32, variable_length=True)),
    'raw': HexBytes,
    's': apply_formatter_if(is_not_null, to_hexbytes(32, variable_length=True)),
    'to': apply_formatter_if(is_address, to_checksum_address),
    'hash': to_hexbytes(32),
    'v': apply_formatter_if(is_not_null, to_integer_if_hex),
    'standardV': apply_formatter_if(is_not_null, to_integer_if_hex),
}


transaction_formatter = apply_formatters_to_dict(TRANSACTION_FORMATTERS)


WHISPER_LOG_FORMATTERS = {
    'sig': to_hexbytes(130),
    'topic': to_hexbytes(8),
    'payload': HexBytes,
    'padding': apply_formatter_if(is_not_null, HexBytes),
    'hash': to_hexbytes(64),
    'recipientPublicKey': apply_formatter_if(is_not_null, to_hexbytes(130)),
}


whisper_log_formatter = apply_formatters_to_dict(WHISPER_LOG_FORMATTERS)


def apply_list_to_array_formatter(formatter: Any) -> Callable[..., Any]:
    return to_list(apply_formatter_to_array(formatter))


LOG_ENTRY_FORMATTERS = {
    'blockHash': apply_formatter_if(is_not_null, to_hexbytes(32)),
    'blockNumber': apply_formatter_if(is_not_null, to_integer_if_hex),
    'transactionIndex': apply_formatter_if(is_not_null, to_integer_if_hex),
    'transactionHash': apply_formatter_if(is_not_null, to_hexbytes(32)),
    'logIndex': to_integer_if_hex,
    'address': to_checksum_address,
    'topics': apply_list_to_array_formatter(to_hexbytes(32)),
    'data': to_ascii_if_bytes,
}


log_entry_formatter = apply_formatters_to_dict(LOG_ENTRY_FORMATTERS)


RECEIPT_FORMATTERS = {
    'blockHash': apply_formatter_if(is_not_null, to_hexbytes(32)),
    'blockNumber': apply_formatter_if(is_not_null, to_integer_if_hex),
    'transactionIndex': apply_formatter_if(is_not_null, to_integer_if_hex),
    'transactionHash': to_hexbytes(32),
    'cumulativeGasUsed': to_integer_if_hex,
    'status': to_integer_if_hex,
    'gasUsed': to_integer_if_hex,
    'contractAddress': apply_formatter_if(is_not_null, to_checksum_address),
    'logs': apply_list_to_array_formatter(log_entry_formatter),
    'logsBloom': to_hexbytes(256),
    'from': apply_formatter_if(is_not_null, to_checksum_address),
    'to': apply_formatter_if(is_address, to_checksum_address),
}


receipt_formatter = apply_formatters_to_dict(RECEIPT_FORMATTERS)

BLOCK_FORMATTERS = {
    'extraData': to_hexbytes(32, variable_length=True),
    'gasLimit': to_integer_if_hex,
    'gasUsed': to_integer_if_hex,
    'size': to_integer_if_hex,
    'timestamp': to_integer_if_hex,
    'hash': apply_formatter_if(is_not_null, to_hexbytes(32)),
    'logsBloom': apply_formatter_if(is_not_null, to_hexbytes(256)),
    'miner': apply_formatter_if(is_not_null, to_checksum_address),
    'mixHash': to_hexbytes(32),
    'nonce': apply_formatter_if(is_not_null, to_hexbytes(8, variable_length=True)),
    'number': apply_formatter_if(is_not_null, to_integer_if_hex),
    'parentHash': apply_formatter_if(is_not_null, to_hexbytes(32)),
    'sha3Uncles': apply_formatter_if(is_not_null, to_hexbytes(32)),
    'uncles': apply_list_to_array_formatter(to_hexbytes(32)),
    'difficulty': to_integer_if_hex,
    'receiptsRoot': to_hexbytes(32),
    'stateRoot': to_hexbytes(32),
    'totalDifficulty': to_integer_if_hex,
    'transactions': apply_one_of_formatters((
        (is_array_of_dicts, apply_list_to_array_formatter(transaction_formatter)),
        (is_array_of_strings, apply_list_to_array_formatter(to_hexbytes(32))),
    )),
    'transactionsRoot': to_hexbytes(32),
}


block_formatter = apply_formatters_to_dict(BLOCK_FORMATTERS)


SYNCING_FORMATTERS = {
    'startingBlock': to_integer_if_hex,
    'currentBlock': to_integer_if_hex,
    'highestBlock': to_integer_if_hex,
    'knownStates': to_integer_if_hex,
    'pulledStates': to_integer_if_hex,
}


syncing_formatter = apply_formatters_to_dict(SYNCING_FORMATTERS)


TRANSACTION_POOL_CONTENT_FORMATTERS = {
    'pending': compose(
        curried.keymap(to_ascii_if_bytes),
        curried.valmap(transaction_formatter),
    ),
    'queued': compose(
        curried.keymap(to_ascii_if_bytes),
        curried.valmap(transaction_formatter),
    ),
}


transaction_pool_content_formatter = apply_formatters_to_dict(
    TRANSACTION_POOL_CONTENT_FORMATTERS
)


TRANSACTION_POOL_INSPECT_FORMATTERS = {
    'pending': curried.keymap(to_ascii_if_bytes),
    'queued': curried.keymap(to_ascii_if_bytes),
}


transaction_pool_inspect_formatter = apply_formatters_to_dict(
    TRANSACTION_POOL_INSPECT_FORMATTERS
)

STORAGE_PROOF_FORMATTERS = {
    'key': HexBytes,
    'value': HexBytes,
    'proof': apply_list_to_array_formatter(HexBytes),
}

ACCOUNT_PROOF_FORMATTERS = {
    'address': to_checksum_address,
    'accountProof': apply_list_to_array_formatter(HexBytes),
    'balance': to_integer_if_hex,
    'codeHash': to_hexbytes(32),
    'nonce': to_integer_if_hex,
    'storageHash': to_hexbytes(32),
    'storageProof': apply_list_to_array_formatter(
        apply_formatters_to_dict(STORAGE_PROOF_FORMATTERS)
    )
}

proof_formatter = apply_formatters_to_dict(ACCOUNT_PROOF_FORMATTERS)

FILTER_PARAMS_FORMATTERS = {
    'fromBlock': apply_formatter_if(is_integer, integer_to_hex),
    'toBlock': apply_formatter_if(is_integer, integer_to_hex),
}


filter_params_formatter = apply_formatters_to_dict(FILTER_PARAMS_FORMATTERS)


filter_result_formatter = apply_one_of_formatters((
    (is_array_of_dicts, apply_list_to_array_formatter(log_entry_formatter)),
    (is_array_of_strings, apply_list_to_array_formatter(to_hexbytes(32))),
))


transaction_param_formatter = compose(
    remove_key_if('to', lambda txn: txn['to'] in {'', b'', None}),
)


estimate_gas_without_block_id = apply_formatter_at_index(transaction_param_formatter, 0)
estimate_gas_with_block_id = apply_formatters_to_sequence([
    transaction_param_formatter,
    block_number_formatter,
])

SIGNED_TX_FORMATTER = {
    'raw': HexBytes,
    'tx': transaction_formatter,
}

signed_tx_formatter = apply_formatters_to_dict(SIGNED_TX_FORMATTER)

FILTER_PARAM_NORMALIZERS = apply_formatters_to_dict({
    'address': apply_formatter_if(is_string, lambda x: [x])
})

PYTHONIC_REQUEST_FORMATTERS: Dict[RPCEndpoint, Callable[..., Any]] = {
    # Eth
    RPC.eth_getBalance: apply_formatter_at_index(block_number_formatter, 1),
    RPC.eth_getBlockByNumber: apply_formatter_at_index(block_number_formatter, 0),
    RPC.eth_getBlockTransactionCountByNumber: apply_formatter_at_index(
        block_number_formatter,
        0,
    ),
    RPC.eth_getCode: apply_formatter_at_index(block_number_formatter, 1),
    RPC.eth_getStorageAt: apply_formatter_at_index(block_number_formatter, 2),
    RPC.eth_getTransactionByBlockNumberAndIndex: compose(
        apply_formatter_at_index(block_number_formatter, 0),
        apply_formatter_at_index(integer_to_hex, 1),
    ),
    RPC.eth_getTransactionCount: apply_formatter_at_index(block_number_formatter, 1),
    RPC.eth_getUncleCountByBlockNumber: apply_formatter_at_index(block_number_formatter, 0),
    RPC.eth_getUncleByBlockNumberAndIndex: compose(
        apply_formatter_at_index(block_number_formatter, 0),
        apply_formatter_at_index(integer_to_hex, 1),
    ),
    RPC.eth_getUncleByBlockHashAndIndex: apply_formatter_at_index(integer_to_hex, 1),
    RPC.eth_newFilter: apply_formatter_at_index(filter_params_formatter, 0),
    RPC.eth_getLogs: apply_formatter_at_index(filter_params_formatter, 0),
    RPC.eth_call: apply_formatters_to_sequence([
        transaction_param_formatter,
        block_number_formatter,
    ]),
    RPC.eth_estimateGas: apply_one_of_formatters((
        (is_length(1), estimate_gas_without_block_id),
        (is_length(2), estimate_gas_with_block_id),
    )),
    RPC.eth_sendTransaction: apply_formatter_at_index(transaction_param_formatter, 0),
    RPC.eth_getProof: apply_formatter_at_index(block_number_formatter, 2),
    # personal
    RPC.personal_importRawKey: apply_formatter_at_index(
        compose(remove_0x_prefix, hexstr_if_str(to_hex)),
        0,
    ),
    RPC.personal_sign: apply_formatter_at_index(text_if_str(to_hex), 0),
    RPC.personal_ecRecover: apply_formatter_at_index(text_if_str(to_hex), 0),
    RPC.personal_sendTransaction: apply_formatter_at_index(transaction_param_formatter, 0),
    # Snapshot and Revert
    RPC.evm_revert: apply_formatter_at_index(integer_to_hex, 0),
    RPC.trace_replayBlockTransactions: apply_formatter_at_index(block_number_formatter, 0),
    RPC.trace_block: apply_formatter_at_index(block_number_formatter, 0),
    RPC.trace_call: compose(
        apply_formatter_at_index(transaction_param_formatter, 0),
        apply_formatter_at_index(block_number_formatter, 2)
    ),
}


PYTHONIC_RESULT_FORMATTERS: Dict[RPCEndpoint, Callable[..., Any]] = {
    # Eth
    RPC.eth_accounts: apply_list_to_array_formatter(to_checksum_address),
    RPC.eth_blockNumber: to_integer_if_hex,
    RPC.eth_chainId: to_integer_if_hex,
    RPC.eth_coinbase: to_checksum_address,
    RPC.eth_estimateGas: to_integer_if_hex,
    RPC.eth_gasPrice: to_integer_if_hex,
    RPC.eth_getBalance: to_integer_if_hex,
    RPC.eth_getBlockByHash: apply_formatter_if(is_not_null, block_formatter),
    RPC.eth_getBlockByNumber: apply_formatter_if(is_not_null, block_formatter),
    RPC.eth_getBlockTransactionCountByHash: to_integer_if_hex,
    RPC.eth_getBlockTransactionCountByNumber: to_integer_if_hex,
    RPC.eth_getCode: HexBytes,
    RPC.eth_getFilterChanges: filter_result_formatter,
    RPC.eth_getFilterLogs: filter_result_formatter,
    RPC.eth_getLogs: filter_result_formatter,
    RPC.eth_getProof: apply_formatter_if(is_not_null, proof_formatter),
    RPC.eth_getStorageAt: HexBytes,
    RPC.eth_getTransactionByBlockHashAndIndex: apply_formatter_if(
        is_not_null,
        transaction_formatter,
    ),
    RPC.eth_getTransactionByBlockNumberAndIndex: apply_formatter_if(
        is_not_null,
        transaction_formatter,
    ),
    RPC.eth_getTransactionByHash: apply_formatter_if(is_not_null, transaction_formatter),
    RPC.eth_getTransactionCount: to_integer_if_hex,
    RPC.eth_getTransactionReceipt: apply_formatter_if(
        is_not_null,
        receipt_formatter,
    ),
    RPC.eth_getUncleCountByBlockHash: to_integer_if_hex,
    RPC.eth_getUncleCountByBlockNumber: to_integer_if_hex,
    RPC.eth_hashrate: to_integer_if_hex,
    RPC.eth_protocolVersion: compose(
        apply_formatter_if(is_integer, str),
        to_integer_if_hex,
    ),
    RPC.eth_sendRawTransaction: to_hexbytes(32),
    RPC.eth_sendTransaction: to_hexbytes(32),
    RPC.eth_sign: HexBytes,
    RPC.eth_signTransaction: apply_formatter_if(is_not_null, signed_tx_formatter),
    RPC.eth_signTypedData: HexBytes,
    RPC.eth_syncing: apply_formatter_if(is_not_false, syncing_formatter),
    # personal
    RPC.personal_importRawKey: to_checksum_address,
    RPC.personal_listAccounts: apply_list_to_array_formatter(to_checksum_address),
    RPC.personal_newAccount: to_checksum_address,
    RPC.personal_sendTransaction: to_hexbytes(32),
    RPC.personal_signTypedData: HexBytes,
    # SHH
    RPC.shh_getFilterMessages: apply_list_to_array_formatter(whisper_log_formatter),
    # Transaction Pool
    RPC.txpool_content: transaction_pool_content_formatter,
    RPC.txpool_inspect: transaction_pool_inspect_formatter,
    # Snapshot and Revert
    RPC.evm_snapshot: hex_to_integer,
    # Net
    RPC.net_peerCount: to_integer_if_hex,
}


ATTRDICT_FORMATTER = {
    '*': apply_formatter_if(is_dict and not_attrdict, AttributeDict.recursive)
}

METHOD_NORMALIZERS: Dict[RPCEndpoint, Callable[..., Any]] = {
    RPC.eth_getLogs: apply_formatter_at_index(FILTER_PARAM_NORMALIZERS, 0),
    RPC.eth_newFilter: apply_formatter_at_index(FILTER_PARAM_NORMALIZERS, 0)
}

STANDARD_NORMALIZERS = [
    abi_bytes_to_hex,
    abi_int_to_hex,
    abi_string_to_hex,
    abi_address_to_hex,
]


ABI_REQUEST_FORMATTERS = abi_request_formatters(STANDARD_NORMALIZERS, RPC_ABIS)


@to_tuple
def combine_formatters(
    formatter_maps: Collection[Dict[RPCEndpoint, Callable[..., TReturn]]], method_name: RPCEndpoint
) -> Iterable[Callable[..., TReturn]]:
    for formatter_map in formatter_maps:
        if method_name in formatter_map:
            yield formatter_map[method_name]


def get_request_formatters(
    method_name: Union[RPCEndpoint, Callable[..., RPCEndpoint]]
) -> Dict[str, Callable[..., Any]]:
    request_formatter_maps = (
        METHOD_NORMALIZERS,
        PYTHONIC_REQUEST_FORMATTERS,
        ABI_REQUEST_FORMATTERS
    )
    formatters = combine_formatters(request_formatter_maps, method_name)
    return compose(*formatters)


def get_result_formatters(
    method_name: Union[RPCEndpoint, Callable[..., RPCEndpoint]]
) -> Dict[str, Callable[..., Any]]:
    formatters = combine_formatters(
        (PYTHONIC_RESULT_FORMATTERS,),
        method_name
    )
    attrdict_formatter = apply_formatter_if(is_dict and not_attrdict, AttributeDict.recursive)

    return compose(*formatters, attrdict_formatter)


def get_error_formatters(
    method_name: Union[RPCEndpoint, Callable[..., RPCEndpoint]]
) -> Dict[str, Callable[..., Any]]:
    #  Note error formatters work on the full response dict
    # TODO - test this function
    error_formatter_maps = ()
    formatters = combine_formatters(error_formatter_maps, method_name)

    return compose(*formatters)
