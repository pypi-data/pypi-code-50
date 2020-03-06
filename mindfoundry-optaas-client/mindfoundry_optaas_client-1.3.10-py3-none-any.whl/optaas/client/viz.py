import copy
from typing import Dict, Tuple, Any
import numpy as np
import pandas as pd
import holoviews as hv

from mindfoundry.optaas.client.client import OPTaaSClient
from mindfoundry.optaas.client.task import Task


class SurrogateViz:
    def __init__(self, client: OPTaaSClient, task: Task) -> None:
        self.client = client
        self.task = task
        self.continuous_vars: Dict[str, hv.Dimension] = {
            param["name"]: hv.Dimension(
                param["name"], range=(param["minimum"], param["maximum"])
            )
            for param in task.parameters
            if param["type"] == "number"
        }
        self.categorical_vars: Dict[str, hv.Dimension] = {
            param["name"]: hv.Dimension(param["name"], values=param["enum"])
            for param in task.parameters
            if param["type"] == "categorical"
        }

        self.grid_size: int = 30

    def plot_surrogate_mean_and_std(
            self,
            x_var: str,
            y_var: str,
            z_range: Tuple[float, float],
            fig_width: int = 600,
            fig_height: int = 600,
        ) -> hv.DynamicMap:
        if not x_var in self.continuous_vars:
            raise KeyError(f"Must choose one of {self.continuous_vars}.\n Got {x_var}")
        if not y_var in self.continuous_vars:
            raise KeyError(f"Must choose one of {self.continuous_vars}.\n Got {y_var}")

        k_dims = [dim for dim in self.categorical_vars.values()] + [
            dim
            for dim in self.continuous_vars.values()
            if dim.name not in (x_var, y_var)
        ]

        def make_surface(*args, **kwargs) -> hv.Layout:
            # Dangerous, assume the args are in the same order as in k_dims
            kwargs = {dim.name: value for dim, value in zip(k_dims, args)}

            _, _, mean, variance = self._predict_at_slice(
                x_var=x_var, y_var=y_var, fixed_vars=kwargs
            )
            bounds = (
                self.continuous_vars[x_var].range[0],
                self.continuous_vars[y_var].range[0],
                self.continuous_vars[x_var].range[1],
                self.continuous_vars[y_var].range[1],
            )
            mean_surface = hv.Surface(mean, bounds=bounds).opts(
                title="Surrogate Mean", xlabel=x_var, ylabel=y_var, zlabel="Value"
            )
            std_surface = hv.Surface(np.sqrt(variance), bounds=bounds).opts(
                title="Surrogate Standard Deviation",
                xlabel=x_var,
                ylabel=y_var,
                zlabel="Value",
            )
            layout = mean_surface + std_surface
            layout.cols(1)
            return layout

        dmap = (
            hv.DynamicMap(make_surface, kdims=k_dims)
            .opts(width=fig_width, height=fig_height)
            .redim.range(z=z_range)
        )
        return dmap

    def plot_surrogate_with_uncertainties(
            self,
            x_var: str,
            y_var: str,
            z_range: Tuple[float, float],
            fig_width: int = 600,
            fig_height: int = 600,
        ) -> hv.DynamicMap:
        if not x_var in self.continuous_vars:
            raise KeyError(f"Must choose one of {self.continuous_vars}.\n Got {x_var}")
        if not y_var in self.continuous_vars:
            raise KeyError(f"Must choose one of {self.continuous_vars}.\n Got {y_var}")

        k_dims = [dim for dim in self.categorical_vars.values()] + [
            dim
            for dim in self.continuous_vars.values()
            if dim.name not in (x_var, y_var)
        ]

        def make_surface(*args, **kwargs) -> hv.Layout:
            # Dangerous, assume the args are in the same order as in k_dims
            kwargs = {dim.name: value for dim, value in zip(k_dims, args)}

            _, _, mean, variance = self._predict_at_slice(
                x_var=x_var, y_var=y_var, fixed_vars=kwargs
            )
            bounds = (
                self.continuous_vars[x_var].range[0],
                self.continuous_vars[y_var].range[0],
                self.continuous_vars[x_var].range[1],
                self.continuous_vars[y_var].range[1],
            )

            mean_surface = hv.Surface(mean, bounds=bounds)
            upper_surface = hv.Surface(
                mean + 2 * np.sqrt(variance), bounds=bounds
            ).options(alpha=0.4, cmap=["blue", "blue"])
            lower_surface = hv.Surface(
                mean - 2 * np.sqrt(variance), bounds=bounds
            ).options(alpha=0.4, cmap=["blue", "blue"])
            layout = (
                mean_surface
                * upper_surface
                * lower_surface.opts(
                    title="Surrogate Mean +- 2 std",
                    xlabel=x_var,
                    ylabel=y_var,
                    zlabel="Value",
                )
            )
            return layout

        dmap = (
            hv.DynamicMap(make_surface, kdims=k_dims)
            .opts(width=fig_width, height=fig_height)
            .redim.range(z=z_range)
        )
        return dmap

    def _predict_at_slice(self, x_var: str, y_var: str, fixed_vars: Dict[str, Any]):
        var_dict = copy.copy(fixed_vars)
        x_grid, y_grid = self._make_grid(x_var=x_var, y_var=y_var)
        var_dict[x_var], var_dict[y_var] = x_grid.ravel(), y_grid.ravel()
        query_df = pd.DataFrame(data=var_dict)
        prediction = self._query_surrogate(data=query_df)

        return (
            x_grid,
            y_grid,
            prediction["mean"].values.reshape(x_grid.shape),
            prediction["variance"].values.reshape(y_grid.shape),
        )

    def _make_grid(self, x_var: str, y_var: str) -> Tuple[np.ndarray, np.ndarray]:
        x_range = np.linspace(
            self.continuous_vars[x_var].range[0],
            self.continuous_vars[x_var].range[1],
            self.grid_size,
        )
        y_range = np.linspace(
            self.continuous_vars[y_var].range[0],
            self.continuous_vars[y_var].range[1],
            self.grid_size,
        )
        x_grid, y_grid = np.meshgrid(x_range, y_range)
        return x_grid, y_grid

    def _query_surrogate(self, data: pd.DataFrame) -> pd.DataFrame:
        query = data.to_dict(orient="records")
        predictions = self.task.get_surrogate_predictions(query)
        raw_mean, raw_variance = zip(
            *[(pred.mean, pred.variance) for pred in predictions]
        )
        result = pd.DataFrame(
            index=data.index, data={"mean": raw_mean, "variance": raw_variance}
        )
        return result
