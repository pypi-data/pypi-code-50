import pytest
from pytket.circuit import Circuit
from pytket.backends.honeywell import HoneywellBackend
import os


@pytest.mark.skipif(
    os.getenv("HQS_AUTH") is None,
    reason="requires environment variable HQS_AUTH to be a valid Honeywell credential",
)
def test_honeywell():
    # Run a circuit on the noisy simulator.
    token = os.getenv("HQS_AUTH")
    b = HoneywellBackend(token, device_name="HQS-LT-1.0-APIVAL", label="test 1")
    c = Circuit(4, 4)
    c.H(0)
    c.CX(0, 1)
    c.Rz(0.3, 2)
    c.CSWAP(0, 1, 2)
    c.CRz(0.4, 2, 3)
    c.CY(1, 3)
    c.ZZPhase(0.1, 2, 0)
    c.Tdg(3)
    c.measure_all()
    b.compile_circuit(c)
    n_shots = 10
    jid = b.process_circuits([c], n_shots)[0]
    shots = b.get_shots(jid, n_shots, seed=1, remove_from_cache=False)
    counts = b.get_counts(jid, n_shots)
    assert len(shots) == n_shots
    assert sum(counts.values()) == n_shots


@pytest.mark.skipif(
    os.getenv("HQS_AUTH") is None,
reason="requires environment variable HQS_AUTH to be a valid Honeywell credential",
)
def test_bell():
    # On the noiseless simulator, we should always get Bell states here.
    token = os.getenv("HQS_AUTH")
    b = HoneywellBackend(token, device_name="HQS-LT-1.0-APIVAL", label="test 2")
    c = Circuit(2, 2)
    c.H(0)
    c.CX(0, 1)
    b.compile_circuit(c)
    n_shots = 10
    jid = b.process_circuits([c], n_shots)[0]
    counts = b.get_shots(jid, n_shots)
    print(counts)
    assert all(q[0] == q[1] for q in counts)


