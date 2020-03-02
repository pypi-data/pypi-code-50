from __future__ import annotations
from typing import Any, Iterable, Optional, Union

import cclib
import copy
import os
import materia as mtr
import subprocess

from ...workflow.tasks.task import Task

__all__ = [
    #    "ComputeKoopmanError",
    #    "ExecuteQChem",
    "QChemAIMD",
    "QChemLRTDDFT",
    "QChemOptimize",
    #   "QChemOptimizeRangeSeparationParameter",
    "QChemPolarizability",
    #    "QChemRTTDDFT",
    "QChemSinglePoint",
    "QChemSinglePointFrontier",
    "WriteQChemInput",
    "WriteQChemInputGeometryRelaxation",
    "WriteQChemInputLRTDDFT",
    "WriteQChemInputPolarizability",
    "WriteQChemInputSinglePoint",
    #    "WriteQChemTDSCF",
]


class QChemBaseTask(Task):
    def __init__(
        self,
        engine: mtr.QChemEngine,
        io: mtr.IOParams,
        handlers: Optional[Iterable[mtr.Handler]] = None,
        name: Optional[str] = None,
    ) -> None:
        super().__init__(handlers=handlers, name=name)
        self.engine = engine
        # self.log_name = log_name
        self.io = io

    def set_defaults(self, settings: mtr.Settings) -> mtr.Settings:
        raise NotImplementedError

    def parse(self, output: str) -> Any:
        raise NotImplementedError

    def run(
        self,
        structure: Union[mtr.QChemStructure, mtr.QChemFragments, mtr.Structure],
        settings: Optional[mtr.Settings] = None,
    ) -> Any:
        s = mtr.Settings() if settings is None else copy.deepcopy(settings)

        # FIXME: this is essentially a hotpatch to handle fragments - come up with something more elegant/sensible ASAP
        inp = mtr.QChemInput(
            molecule=structure
            if isinstance(structure, mtr.Structure)
            or isinstance(structure, mtr.QChemStructure)
            else mtr.QChemFragments(structures=structure),
            settings=self.set_defaults(s),
        )

        with self.io() as io:
            inp.write(io.inp)

            self.engine.execute(io.inp, io.out)

            return self.parse(io.out)


# class QChemOptimizeRangeSeparationParameter(QChemBaseTask):
#     def run(
#         self,
#         structure: Union[mtr.QChemStructure, mtr.QChemFragments, mtr.Structure],
#         settings: Optional[mtr.Settings] = None,
#     ) -> Any:
#         for x in np.linspace(0,1,5):


# evals = {}
# np.polynomial.polynomial.Polynomial.fit(x2,y2,2).deriv().roots()
# def f(x):
#     if x in evals:
#         return evals[x]
#     else:
#         s = copy.deepcopy(settings)
#         s['rem','omega'] = s['rem','omega2'] = x
#         input_structure = mtr.InputTask(value=structure)
#         input_settings = mtr.InputTask(value=settings)
#         sp = QChemSinglePoint(self.engine,self.io)
#         sp.requires(structure=input_structure,settings=input_settings)
#         raise mtr.ActionSignal(actions=mtr.InsertTasks(input_structure,input_settings,sp))
#         mtr.QChemInput(settings=settings["input"]).write(
#             filepath=settings["input_path"]
#         )

# f(0.5)

# FIXME: get output and save result to self.function_evals
# FIXME: maybe this shouldn't run the jobs but instead should be the successor to three jobs (gs, cation, anion - links = {0:[3],1:[3],2:[3],3:[]}) and should gather their results to compute and save the HOMO-LUMO / IP-EA error
#        then a handler is attached to this job which adds three parent tasks with modified omega/omega2 if the error is insufficiently small?


# class ComputeKoopmanError(Task):
#     def run(self, omega, gs, cation_energy, anion_energy) -> None:
#         # FIXME: if ea is negative, don't use it?
#         gs_energy, homo, lumo = gs
#         ip = cation_energy - gs_energy
#         ea = gs_energy - anion_energy
#         return (homo.convert(mtr.eV) + ip) ** 2 + (lumo.convert(mtr.eV) + ea) ** 2


# class ExecuteQChem(QChemBaseTask):
#     def run(self) -> Any:
#         with self.io() as io:
#             self.engine.execute(io.inp, io.out)


class QChemAIMD(QChemBaseTask):
    def parse(self, output: str) -> Any:
        with open(output, "r") as f:
            return "".join(f.readlines())

    def set_defaults(self, settings: mtr.Settings) -> mtr.Settings:
        if ("rem", "exchange") not in settings and ("rem", "method",) not in settings:
            settings["rem", "exchange"] = "HF"
        if ("rem", "basis") not in settings:
            settings["rem", "basis"] = "3-21G"
        if ("rem", "jobtype") not in settings:
            settings["rem", "jobtype"] = "aimd"
        if ("rem", "time_step") not in settings:
            settings["rem", "time_step"] = 1
        if ("rem", "aimd_steps") not in settings:
            settings["rem", "aimd_steps"] = 10
        if ("velocity",) not in settings and (
            "rem",
            "aimd_init_veloc",
        ) not in settings:
            settings["rem", "aimd_init_veloc"] = "thermal"
        if (
            ("rem", "aimd_init_veloc") in settings
            and settings["rem", "aimd_init_veloc"].lower().strip() == "thermal"
            and ("rem", "aimd_temp") not in settings
        ):
            settings["rem", "aimd_temp"] = 300

        return settings


class QChemLRTDDFT(QChemBaseTask):
    def parse(self, output: str) -> Any:
        # FIXME: implement using cclib
        raise NotImplementedError

    def set_defaults(self, settings: mtr.Settings) -> mtr.Settings:
        if ("rem", "exchange") not in settings and ("rem", "method",) not in settings:
            settings["rem", "exchange"] = "HF"
        if ("rem", "basis") not in settings:
            settings["rem", "basis"] = "3-21G"
        if ("rem", "cis_n_roots") not in settings:
            settings["rem", "cis_n_roots"] = 1
        if ("rem", "cis_singlets") not in settings:
            settings["rem", "cis_singlets"] = True
        if ("rem", "cis_triplets") not in settings:
            settings["rem", "cis_triplets"] = False
        if ("rem", "rpa") not in settings:
            settings["rem", "rpa"] = False

        return settings


class QChemOptimize(QChemBaseTask):
    def parse(self, output: str) -> Any:
        try:
            parsed = cclib.io.ccread(output)
            # FIXME: is this the correct unit?
            coords = mtr.Qty(value=parsed.atomcoords, unit=mtr.angstrom)[-1, :, :]
            zs = parsed.atomnos
        except AttributeError:
            return None
        # FIXME: is this the correct unit?
        atoms = (
            mtr.Atom(element=Z, position=mtr.Qty(value=p, unit=mtr.angstrom))
            for Z, p in zip(zs, coords)
        )
        return mtr.Structure(atoms=atoms)

    def set_defaults(self, settings: mtr.Settings) -> mtr.Settings:
        if ("rem", "exchange") not in settings and ("rem", "method",) not in settings:
            settings["rem", "exchange"] = "HF"
        if ("rem", "basis") not in settings:
            settings["rem", "basis"] = "3-21G"
        if ("rem", "jobtype") not in settings:
            settings["rem", "jobtype"] = "opt"

        return settings


class QChemPolarizability(QChemBaseTask):
    def parse(self, output: str) -> Any:
        try:
            polarizability = mtr.Qty(
                value=cclib.io.ccread(output).polarizabilities, unit=mtr.au_volume,
            )
        except AttributeError:
            polarizability = None

        return polarizability

    def set_defaults(self, settings: mtr.Settings) -> mtr.Settings:
        if ("rem", "exchange") not in settings and ("rem", "method",) not in settings:
            settings["rem", "exchange"] = "HF"
        if ("rem", "basis") not in settings:
            settings["rem", "basis"] = "3-21G"
        if ("rem", "jobtype") not in settings:
            settings["rem", "jobtype"] = "polarizability"

        return settings

    def run(
        self,
        structure: Union[mtr.QChemStructure, mtr.QChemFragments, mtr.Structure],
        settings: Optional[mtr.Settings] = None,
    ) -> Any:
        # NOTE: bug workaround for parallel polarizability calculation in Q-Chem 5.2.1
        os.environ["QCINFILEBASE"] = "0"
        return super().run(structure, settings)


# class QChemRTTDDFT(Task):
#     def __init__(
#         self,
#         structure,
#         input_name,
#         output_name,
#         scratch_directory,
#         settings=None,
#         tdscf_settings=None,
#         executable="qchem",
#         work_directory=".",
#         num_cores=1,
#         parallel=False,
#         handlers=None,
#         name=None,
#     ):
#         super().__init__(handlers=handlers, name=name)
#         self.work_directory = mtr.expand(work_directory)
#         self.input_path = mtr.expand(os.path.join(work_directory, input_name))
#         self.output_path = mtr.expand(os.path.join(work_directory, output_name))
#         self.scratch_directory = mtr.expand(scratch_directory)
#         self.executable = executable
#         self.num_cores = num_cores
#         self.parallel = parallel
#         try:
#             os.makedirs(mtr.expand(work_directory))
#         except FileExistsError:
#             pass
#         settings = settings or mtr.Settings()
#         settings["molecule", "structure"] = structure
#         if ("rem", "exchange") not in settings and ("rem", "method",) not in settings:
#             settings["rem", "exchange"] = "HF"
#         if ("rem", "basis") not in settings:
#             settings["rem", "basis"] = "3-21G"
#         if ("rem", "rttddft") not in settings:
#             settings["rem", "rttddft"] = 1
#         self.tdscf_settings = tdscf_settings or mtr.Settings()

#     def run(self):
#         tdscf_input_path = mtr.expand(os.path.join(self.work_directory, "TDSCF.prm"))
#         keys = tuple(str(next(iter(k))) for k in self.tdscf_settings)
#         max_length = max(len(k) for k in keys)
#         with open(mtr.expand(tdscf_input_path), "w") as f:
#             f.write(
#                 "\n".join(
#                     k + " " * (max_length - len(k) + 1) + str(self.tdscf_settings[k])
#                     for k in keys
#                 )
#             )
#         mtr.QChemInput(settings=settings).write(filepath=self.input_path)
#         try:
#             os.makedirs(mtr.expand(os.path.join(self.work_directory, "logs")))
#         except FileExistsError:
#             pass
#         os.environ["QCSCRATCH"] = self.scratch_directory
#         with open(self.output_path, "w") as f:
#             if self.parallel:
#                 subprocess.call(
#                     [self.executable, "-nt", str(self.num_cores), self.input_path],
#                     stdout=f,
#                     stderr=subprocess.STDOUT,
#                 )
#             else:
#                 subprocess.call([self.executable, self.input_path], stdout=f)

#         # FIXME: finish with output


class QChemSinglePoint(QChemBaseTask):
    def parse(self, output: str) -> Any:
        try:
            energy = mtr.Qty(cclib.io.ccread(output).scfenergies, mtr.eV)
        except AttributeError:
            energy = None

        return energy

    def set_defaults(self, settings: mtr.Settings) -> mtr.Settings:
        if ("rem", "exchange") not in settings and ("rem", "method",) not in settings:
            settings["rem", "exchange"] = "HF"
        if ("rem", "basis") not in settings:
            settings["rem", "basis"] = "3-21G"
        if ("rem", "jobtype") not in settings:
            settings["rem", "jobtype"] = "sp"

        return settings


class QChemSinglePointFrontier(QChemBaseTask):
    def parse(self, output: str) -> Any:
        try:
            out = cclib.io.ccread(output)
            energy = mtr.Qty(out.scfenergies, mtr.eV)
            moenergies = out.moenergies
            homo_indices = out.homos

            homos = []
            lumos = []

            for moe, h in zip(moenergies, homo_indices):
                homo, lumo = moe[h : h + 2]
                homos.append(homo)
                lumos.append(lumo)
            # alpha_occ, beta_occ, alpha_unocc, beta_unocc = mtr.QChemOutput(output).get(
            #     "orbital_energies"
            # )
            homo = mtr.Qty(max(homos), mtr.eV)
            lumo = mtr.Qty(min(lumos), mtr.eV)
        except AttributeError:
            energy = None
            homo = None
            lumo = None

        return energy, homo, lumo

    def set_defaults(self, settings: mtr.Settings) -> mtr.Settings:
        if ("rem", "exchange") not in settings and ("rem", "method",) not in settings:
            settings["rem", "exchange"] = "HF"
        if ("rem", "basis") not in settings:
            settings["rem", "basis"] = "3-21G"
        if ("rem", "jobtype") not in settings:
            settings["rem", "jobtype"] = "sp"

        return settings


class WriteQChemInput(Task):
    def __init__(
        self,
        io: mtr.IOParams,
        handlers: Optional[Iterable[mtr.Handler]] = None,
        name: str = None,
    ) -> None:
        super().__init__(handlers=handlers, name=name)
        self.io = io

    def set_defaults(self, settings: mtr.Settings) -> mtr.Settings:
        return settings

    def run(
        self,
        structure: Union[mtr.QChemStructure, mtr.QChemFragments, mtr.Structure],
        settings: Optional[mtr.Settings] = None,
    ) -> None:
        s = mtr.Settings() if settings is None else copy.deepcopy(settings)
        # FIXME: this is essentially a hotpatch to handle fragments - come up with something more elegant/sensible ASAP
        inp = mtr.QChemInput(
            molecule=structure
            if isinstance(structure, mtr.Structure)
            or isinstance(structure, mtr.QChemStructure)
            else mtr.QChemFragments(structures=structure),
            settings=self.set_defaults(s),
        )

        with self.io() as io:
            inp.write(io.inp)


class WriteQChemInputGeometryRelaxation(WriteQChemInput):
    def set_defaults(self, settings: mtr.Settings) -> mtr.Settings:
        if ("rem", "exchange") not in settings and ("rem", "method",) not in settings:
            settings["rem", "exchange"] = "HF"
        if ("rem", "basis") not in settings:
            settings["rem", "basis"] = "3-21G"
        if ("rem", "jobtype") not in settings:
            settings["rem", "jobtype"] = "opt"

        return settings


class WriteQChemInputLRTDDFT(WriteQChemInput):
    def set_defaults(self, settings: mtr.Settings) -> mtr.Settings:
        if ("rem", "exchange") not in settings and ("rem", "method",) not in settings:
            settings["rem", "exchange"] = "HF"
        if ("rem", "basis") not in settings:
            settings["rem", "basis"] = "3-21G"
        if ("rem", "cis_n_roots") not in settings:
            settings["rem", "cis_n_roots"] = 1
        if ("rem", "cis_singlets") not in settings:
            settings["rem", "cis_singlets"] = True
        if ("rem", "cis_triplets") not in settings:
            settings["rem", "cis_triplets"] = False
        if ("rem", "rpa") not in settings:
            settings["rem", "rpa"] = False

        return settings


class WriteQChemInputPolarizability(WriteQChemInput):
    def set_defaults(self, settings: mtr.Settings) -> mtr.Settings:
        if ("rem", "exchange") not in settings and ("rem", "method",) not in settings:
            settings["rem", "exchange"] = "HF"
        if ("rem", "basis") not in settings:
            settings["rem", "basis"] = "3-21G"
        if ("rem", "jobtype") not in settings:
            settings["rem", "jobtype"] = "polarizability"

        return settings


class WriteQChemInputSinglePoint(WriteQChemInput):
    def set_defaults(self, settings: mtr.Settings) -> mtr.Settings:
        if ("rem", "exchange") not in settings and ("rem", "method",) not in settings:
            settings["rem", "exchange"] = "HF"
        if ("rem", "basis") not in settings:
            settings["rem", "basis"] = "3-21G"

        return settings


# class WriteQChemTDSCF(Task):
#     def __init__(
#         self,
#         settings: Optional[mtr.Settings] = None,
#         work_directory: str = ".",
#         handlers: Optional[Iterable[mtr.Handler]] = None,
#         name: str = None,
#     ):
#         super().__init__(handlers=handlers, name=name)
#         self.work_directory = mtr.expand(work_directory)
#         settings = settings

#         try:
#             os.makedirs(mtr.expand(work_directory))
#         except FileExistsError:
#             pass

#     def run(self) -> None:
#         input_path = mtr.expand(os.path.join(self.work_directory, "TDSCF.prm"))

#         keys = tuple(str(next(iter(k))) for k in settings)
#         max_length = max(len(k) for k in keys)

#         with open(mtr.expand(input_path), "w") as f:
#             f.write(
#                 "\n".join(
#                     k + " " * (max_length - len(k) + 1) + str(settings[k]) for k in keys
#                 )
#             )
