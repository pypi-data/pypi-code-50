#!/usr/bin/env python3


from importlib import import_module


# Available cryptocurrencies
available_cryptocurrencies = [
    # Bitcoin cryptocurrency names
    "bitcoin", "Bitcoin", "BITCOIN" "BTC", "btc",
    # Bytom cryptocurrency names
    "bytom", "Bytom", "BYTOM", "BTM", "btm"
]


# Types
types = [
    # FUnd names
    "Fund", "fund", "FUND",
    # Claim names
    "Claim", "claim", "CLAIM",
    # Refund names
    "Refund", "refund", "REFUND",
]


class Provider:

    def __init__(self, cryptocurrency, type):
        if cryptocurrency not in available_cryptocurrencies:
            raise NameError("invalid provider or cryptocurrency name")
        if type not in types:
            raise NameError("invalid type name")
        cryptocurrency = str(cryptocurrency).lower()
        _type = str(type).capitalize()
        if cryptocurrency == "btc":
            cryptocurrency = "bitcoin"
        elif cryptocurrency == "btm":
            cryptocurrency = "bytom"
        self.Wallet = getattr(import_module(
            ".providers.%s.wallet" % cryptocurrency), "Wallet")
        self.HTLC = getattr(import_module(
            ".providers.%s.htlc" % cryptocurrency), "HTLC")
        if _type == "Fund":
            self.FundTransaction = getattr(import_module(
                ".providers.%s.transaction" % cryptocurrency), "FundTransaction")
            self.FundSolver = getattr(import_module(
                ".providers.%s.solver" % cryptocurrency), "FundSolver")
        elif _type == "Claim":
            self.ClaimTransaction = getattr(import_module(
                ".providers.%s.transaction" % cryptocurrency), "ClaimTransaction")
            self.ClaimSolver = getattr(import_module(
                ".providers.%s.solver" % cryptocurrency), "ClaimSolver")
        elif _type == "Refund":
            self.RefundTransaction = getattr(import_module(
                ".providers.%s.transaction" % cryptocurrency), "RefundTransaction")
            self.RefundSolver = getattr(import_module(
                ".providers.%s.solver" % cryptocurrency), "RefundSolver")

    def wallet(self):
        return self

    def htlc(self):
        return self

    def transaction(self):
        return self

    def solver(self):
        return self

    def signature(self):
        return self
    
    def submit(self):
        return self
