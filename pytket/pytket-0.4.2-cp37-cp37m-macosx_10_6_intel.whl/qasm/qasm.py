# Copyright 2019 Cambridge Quantum Computing
#
# Licensed under a Non-Commercial Use Software Licence (the "Licence");
# you may not use this file except in compliance with the Licence.
# You may obtain a copy of the Licence in the LICENCE file accompanying
# these documents or at:
#
#     https://cqcl.github.io/pytket/build/html/licence.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the Licence is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Licence for the specific language governing permissions and
# limitations under the Licence, but note it is strictly for non-commercial use.

# TODO: Output custom gates
# TODO: Figure out nice way to make these class methods of Circuit
import os
import io
from pytket import Circuit, OpType, UnitID
from pytket.circuit import CustomGateDef
from sympy import sympify, pi

NOPARAM_COMMANDS = {
    "CX": OpType.CX,  # built-in gate equivalent to "cx"
    "cx": OpType.CX,
    "x": OpType.X,
    "y": OpType.Y,
    "z": OpType.Z,
    "h": OpType.H,
    "s": OpType.S,
    "sdg": OpType.Sdg,
    "t": OpType.T,
    "tdg": OpType.Tdg,
    "cz": OpType.CZ,
    "cy": OpType.CY,
    "ch": OpType.CH,
    "ccx": OpType.CCX,
    "ZZ": OpType.ZZMax,
    "measure": OpType.Measure,
    "id": OpType.noop,
    "barrier": OpType.Barrier,
}

PARAM_COMMANDS = {
    "U": OpType.U3,  # built-in gate equivalent to "u3"
    "u3": OpType.U3,
    "u2": OpType.U2,
    "u1": OpType.U1,
    "rx": OpType.Rx,
    "ry": OpType.Ry,
    "rz": OpType.Rz,
    "Rz": OpType.Rz,
    "U1q": OpType.PhasedX,
    "crz": OpType.CRz,
    "cu1": OpType.CU1,
    "cu3": OpType.CU3,
}

included_gates = {
    "qelib1": set(
        (
            "CX",
            "cx",
            "x",
            "y",
            "z",
            "h",
            "s",
            "sdg",
            "t",
            "tdg",
            "cz",
            "cy",
            "ch",
            "ccx",
            "measure",
            "id",
            "barrier",
            "U",
            "u3",
            "u2",
            "u1",
            "rx",
            "ry",
            "rz",
            "crz",
            "cu1",
            "cu3",
        )
    )
}
included_gates["hqslib1"] = included_gates["qelib1"].copy()
included_gates["hqslib1"].update(("U1q", "rz", "ZZ"))
_tk_to_qasm_noparams = dict((reversed(item) for item in NOPARAM_COMMANDS.items()))
_tk_to_qasm_noparams[OpType.CX] = "cx"  # prefer "cx" to "CX"
_tk_to_qasm_params = dict((reversed(item) for item in PARAM_COMMANDS.items()))
_tk_to_qasm_params[OpType.U3] = "u3"  # prefer "u3" to "U"
_tk_to_qasm_params[OpType.Rz] = "rz"  # prefer "rz" to "Rz"


class QASMParser(object):
    """Class for parsing OpenQASM files into CQC t|ket> Circuits."""

    def __init__(self):
        self.circuit = Circuit()
        self.gate_dict = dict()
        self.reg_map = dict()
        self.include = ""

    def parse_qasm(self, qasm):
        lines = qasm.splitlines()
        rows = []

        # first, get rid of comments and whitespace lines
        for l in lines:
            i = l.find("//")
            if i != -1:
                s = l[0:i].strip()
            else:
                s = l.strip()
            if s:
                rows.append(s)

        # now, throw away OPENQASM descriptor etc.
        if not (
            rows[0].startswith("OPENQASM 2.0")
            and rows[1].startswith('include "')
            and rows[1].endswith('.inc";')
        ):
            raise TypeError("File must declare OPENQASM version and its includes.")
        self.include = rows[1][len('include "') : -len('".inc;')]
        if self.include not in ("qelib1", "hqslib1"):
            raise ValueError("Header {}.inc not recognised".format(self.include))
        data = "\n".join(rows[2:])

        # now, separate out the custom gates to deal with elsewhere
        while True:
            i = data.find("gate ")
            if i == -1:
                break
            j = data.find("}", i)
            if j == -1:
                raise TypeError("Custom gate definition is invalid.")
            self.parse_custom_gate(data[i : j + 1])  # TODO: deal with custom gate
            data = data[:i] + data[j + 1 :]

        # now, parse the regular instructions
        instructions = [s.strip() for s in data.split(";") if s.strip()]
        for i in instructions:
            self.parse_instruction(i, self.circuit, self.reg_map)
        return self.circuit

    def parse_custom_gate(self, data):
        signature, rest = data.split("{", 1)
        _, signature = signature.split(" ", 1)  # ignore "gate"
        if signature.find("(") != -1:
            gatename, other = signature.split("(")
            symbol_list, arg_list = other.split(")")
        else:
            gatename, arg_list = signature.split(" ", 1)
            symbol_list = ""
        gatename = gatename.strip()
        symbols = [sympify(s.strip()) for s in symbol_list.split(",")]
        args = [a.strip() for a in arg_list.split(",")]
        rename_map = {}
        qb_map = {}
        circ = Circuit()
        for i, a in enumerate(args):
            circ.add_qubit(UnitID(a))
            rename_map.update({UnitID(a): UnitID("q", i)})
            qb_map[a] = [UnitID(a)]
        command_block, _ = rest.split("}", 1)
        commands = [c.strip() for c in command_block.split(";") if c.strip()]
        for com in commands:
            self.parse_instruction(com, circ, qb_map)
        circ.rename_units(rename_map)
        symbol_map = {sym: sym * pi for sym in symbols}
        circ.symbol_substitution(symbol_map)  # qasm arguments are given in radians
        self.gate_dict[gatename] = CustomGateDef.define(gatename, circ, symbols)

    def parse_instruction(self, instruction, circuit, reg_map):
        if instruction.find("->") != -1:
            ###handle measure gates
            ###currently assumes that there is just 1 qb being read to 1 bit
            name_and_qbs, bits = instruction.split("->", 1)
            if name_and_qbs.find("measure") == -1:
                raise Exception(
                    "Error in parsing: cannot accept a non-Measure gate writing to classical register"
                )
            name_and_qbs = name_and_qbs.replace("measure", "")
            name_and_qbs = name_and_qbs.replace(" ", "")

            name_and_qbs.strip()
            if "[" in name_and_qbs:
                qregname, qbindex = name_and_qbs.split("[")
                qbindex, _ = qbindex.split("]")
                qbindex = int(qbindex)
                qubits = [UnitID(qregname, qbindex)]
            else:
                qubits = reg_map[name_and_qbs]

            bits = bits.replace(" ", "")
            if "[" in bits:
                bitreg, bitindex = bits.split("[")
                bitindex, _ = bitindex.split("]")
                bitindex = int(bitindex)
                bits = [UnitID(bitreg, bitindex)]
            else:
                bits = reg_map[bits]

            for q, b in zip(qubits, bits):
                circuit.Measure(q, b)

            return

        index = _find_respecting_brackets(instruction, " ")
        name = instruction[:index]
        rest = instruction[index + 1 :]
        args = [s.strip() for s in rest.split(",") if s.strip()]

        # deal with qubit register declarations
        if name == "qreg" or name == "creg":
            regname, size = args[0].split("[", 1)
            regname.strip()
            size = int(size[:-1])
            if name == "qreg":
                dict_map = circuit.add_q_register(regname, size)
            else:
                dict_map = circuit.add_c_register(regname, size)
            reg_map[regname] = [dict_map[i] for i in range(size)]
            return

        # get qubits to append operation to
        qubits = []
        for a in args:
            if "[" in a:
                regname, val = a.split("[", 1)
                val = int(val[:-1])
                qubits.append([UnitID(regname, val)])
            else:
                qubits.append(reg_map[a])

        # if the gate is parameterised, get these parameters
        if name.find("(") != -1:
            name, params = name.split("(", 1)
            params = params[:-1]  # cut off final close bracket
            angle_start = 0
            angle_end = _find_respecting_brackets(params, ",")
            angles = []
            while angle_end != -1:
                angles.append(params[angle_start:angle_end].strip())
                angle_start = angle_end + 1
                angle_end = _find_respecting_brackets(params, ",", angle_start)
            angles.append(params[angle_start:].strip())
            halfturn_angles = []
            for ang in angles:
                try:
                    halfturns = sympify(ang) / pi
                    halfturn_angles.append(halfturns)
                except:
                    raise TypeError("Cannot parse angle: {}".format(ang))
            if name in PARAM_COMMANDS:
                if (
                    self.include != "hqslib1"
                    and name in included_gates["hqslib1"]
                    and name not in included_gates["qelib1"]
                ):
                    raise TypeError(
                        "Gate of type {} is not defined in header {}.inc".format(
                            name, self.include
                        )
                    )
                for qbs in zip(*qubits):
                    circuit.add_gate(
                        PARAM_COMMANDS[name], halfturn_angles, list(qbs), []
                    )
            elif name in self.gate_dict:
                for qbs in zip(*qubits):
                    circuit.add_custom_gate(
                        self.gate_dict[name], halfturn_angles, list(qbs)
                    )
            else:
                raise TypeError("Cannot parse gate of type: {}".format(name))

        else:
            if name == "barrier":
                circuit.add_gate(
                    OpType.Barrier, [], [q for qbs in qubits for q in qbs], []
                )
            elif name in NOPARAM_COMMANDS:
                if (
                    self.include != "hqslib1"
                    and name in included_gates["hqslib1"]
                    and name not in included_gates["qelib1"]
                ):
                    raise TypeError(
                        "Gate of type {} is not defined in header {}.inc".format(
                            name, self.include
                        )
                    )

                for qbs in zip(*qubits):
                    circuit.add_gate(NOPARAM_COMMANDS[name], [], list(qbs), [])
            elif name in self.gate_dict:
                for qbs in zip(*qubits):
                    circuit.add_custom_gate(self.gate_dict[name], [], list(qbs))
            else:
                raise TypeError("Cannot parse gate of type: {}".format(name))


def circuit_from_qasm(input_file: str) -> Circuit:
    """A method to generate a tket Circuit from a qasm file"""
    ext = os.path.splitext(input_file)[-1]
    if ext != ".qasm":
        raise TypeError("Can only convert .qasm files")
    p = QASMParser()
    with open(input_file, "r") as f:
        circ = p.parse_qasm(f.read())
    return circ


def circuit_from_qasm_str(qasm_str: str) -> Circuit:
    """A method to generate a tket Circuit from a qasm str"""
    return circuit_from_qasm_io(io.StringIO(qasm_str))


def circuit_from_qasm_io(stream_in: io.TextIOBase) -> Circuit:
    """A method to generate a tket Circuit from a qasm text stream"""
    p = QASMParser()
    return p.parse_qasm(stream_in.read())


def circuit_to_qasm(circ: Circuit, output_file: str, header: str = "qelib1"):
    """A method to generate a qasm file from a tket Circuit"""
    with open(output_file, "w") as out:
        circuit_to_qasm_io(circ, out)


def circuit_to_qasm_str(circ: Circuit, header: str = "qelib1") -> str:
    """A method to generate a qasm str from a tket Circuit"""
    buffer = io.StringIO()
    circuit_to_qasm_io(circ, buffer)
    return buffer.getvalue()


def circuit_to_qasm_io(
    circ: Circuit, stream_out: io.TextIOBase, header: str = "qelib1"
):
    """A method to generate a qasm text stream from a tket Circuit"""
    stream_out.write('OPENQASM 2.0;\ninclude "{}.inc";\n\n'.format(header))
    qreg_sizes = {}
    for qb in circ.qubits:
        if len(qb.index) != 1:
            raise NotImplementedError("Qiskit registers must use a single index")
        if (qb.reg_name not in qreg_sizes) or (qb.index[0] >= qreg_sizes[qb.reg_name]):
            qreg_sizes.update({qb.reg_name: qb.index[0] + 1})
    creg_sizes = {}
    for b in circ.bits:
        if len(b.index) != 1:
            raise NotImplementedError("Qiskit registers must use a single index")
        if (b.reg_name not in creg_sizes) or (b.index[0] >= creg_sizes[b.reg_name]):
            creg_sizes.update({b.reg_name: b.index[0] + 1})
    for reg_name, size in qreg_sizes.items():
        stream_out.write("qreg {}[{}];\n".format(reg_name, size))
    for reg_name, size in creg_sizes.items():
        stream_out.write("creg {}[{}];\n".format(reg_name, size))
    for command in circ:
        op = command.op
        optype = op.get_type()
        has_params = False
        if optype in _tk_to_qasm_noparams:
            opstr = _tk_to_qasm_noparams[optype]
        elif optype in _tk_to_qasm_params:
            has_params = True
            opstr = _tk_to_qasm_params[optype]
        else:
            raise TypeError("Cannot print command of type: {}".format(op.get_name()))
        qbs = command.qubits
        if opstr not in included_gates[header]:
            raise TypeError(
                "Gate of type {} is not defined in header {}.inc".format(opstr, header)
            )
        stream_out.write(opstr)
        if has_params:
            params = op.get_params()
            stream_out.write("(")
            for i in range(len(params)):
                reduced = True
                try:
                    p = float(params[i])
                except TypeError:
                    reduced = False
                    p = params[i]
                if i < len(params) - 1:
                    if reduced:
                        stream_out.write("{}*pi,".format(p))
                    else:
                        stream_out.write("({})*pi,".format(p))

                else:
                    if reduced:
                        stream_out.write("{}*pi)".format(p))
                    else:
                        if reduced:
                            stream_out.write("{}*pi)".format(p))
                        else:
                            stream_out.write("({})*pi)".format(p))
        stream_out.write(" ")
        for i in range(len(qbs)):
            stream_out.write(qbs[i].__repr__())
            if optype == OpType.Measure:
                stream_out.write(" -> ")
            elif i < len(qbs) - 1:
                stream_out.write(",")
            else:
                stream_out.write(";\n")
        if optype == OpType.Measure:  ###assume written to only 1 bit
            bits = command.bits
            stream_out.write("{};\n".format(bits[0].__repr__()))


def _find_respecting_brackets(full_string: str, phrase: str, start: int = 0):
    """Assuming `full_string` is well-bracketed (at no point is there a close
    without an unmatched open), returns the index of the first location of
    `phrase` in `full_string` that is not inside any pair of brackets
    """
    length = len(full_string)
    non_neg_fix = lambda x: (length if x == -1 else x)
    next_phrase = full_string.find(phrase, start)
    next_open = non_neg_fix(full_string.find("(", start))
    next_close = non_neg_fix(full_string.find(")", start))
    depth = 0
    while next_phrase != -1:
        if next_phrase < next_open and next_phrase < next_close:
            if depth == 0:
                return next_phrase  # found a match
            else:
                next_phrase = full_string.find(
                    phrase, next_phrase + 1
                )  # bad match, try next
        elif next_open < next_close:
            depth += 1
            next_open = non_neg_fix(full_string.find("(", next_open + 1))
        else:
            # there must be a close first, as length > next_phrase >= next_open >= next_close
            depth -= 1
            next_close = non_neg_fix(full_string.find(")", next_close + 1))
    return -1
