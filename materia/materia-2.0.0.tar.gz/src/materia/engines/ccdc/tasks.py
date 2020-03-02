from __future__ import annotations
import os
import materia
import textwrap
from typing import Iterable, Optional

from ...workflow.tasks.task import Task

__all__ = ["CCDCUnitCellStructure"]


class CCDCUnitCellStructure(Task):
    def __init__(
        self,
        input_name: str,
        molecule_name: str,
        engine: materia.CCDCEngine,
        handlers: Optional[Iterable[materia.Handler]] = None,
        name: Optional[str] = None,
    ) -> None:
        self.input_name = input_name
        self.engine = engine
        name = "'" + molecule_name + "'"
        self.input_string = textwrap.dedent(
            f"""\
                    import numpy as np
                    import ccdc.search
                    tns = ccdc.search.TextNumericSearch()
                    tns.add_compound_name({name})
                    try:
                        hit = next(hit for hit in tns.search() if hit.entry.chemical_name == {name})
                        print('atomic_symbols: {{0}}\\n'.format(tuple(a.atomic_symbol for a in hit.molecule.atoms)))
                        print('coordinates: {{0}}\\n'.format(np.vstack([a.coordinates for a in hit.molecule.atoms])))
                        print('spacegroup_number_and_setting: {{0}}\\n'.format(hit.crystal.spacegroup_number_and_setting))
                        print('cell_lengths: {{0}}\\n'.format(np.array(hit.crystal.cell_lengths)))
                        print('cell_angles: {{0}}\\n'.format(np.array(hit.crystal.cell_angles)))
                    except StopIteration:
                        pass
                    """
        )

    def run(self):
        # FIXME: catch StopIteration in CCDC code
        # FIXME: generalize past 2019 version of CCDC code
        # FIXME: add more rigorous/better checking for CCDC crystal matches

        # FIXME: where does input_path come from? must include self.input_name but also must include engine.work_dir...
        materia.CCDCInput(ccdc_script=self.input_string).write(self.input_path)

        self.engine.execute(input_path=self.input_path)
