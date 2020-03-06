import typing
from .utils import cartesian_product


class R3D3Experiment(typing.NamedTuple):
    config: typing.Dict
    binary: str

    def get_config_with_binary(self) -> typing.Dict:
        return {**self.config, "binary": self.binary}


class R3D3ExperimentPlan(typing.NamedTuple):
    experiments: typing.List[R3D3Experiment]
    max_nb_processes: int
    db_path: str
    debug: bool = False

    @classmethod
    def from_cartesian_space(
        cls, db_path: str, configs: typing.Dict, binary: str, max_nb_processes: int
    ) -> "R3D3ExperimentPlan":

        experiments = [
            R3D3Experiment(binary=binary, config=config)
            for config in cartesian_product(configs)
        ]

        return cls(
            experiments=experiments, max_nb_processes=max_nb_processes, db_path=db_path
        )

    @classmethod
    def from_multiple_plans(cls, experiment_plans: typing.List["R3D3ExperimentPlan"]):
        max_nb_processes = min([plan.max_nb_processes for plan in experiment_plans])
        db_path = experiment_plans[0].db_path
        experiments = sum([plan.experiments for plan in experiment_plans], [])

        return cls(
            experiments=experiments, max_nb_processes=max_nb_processes, db_path=db_path
        )
