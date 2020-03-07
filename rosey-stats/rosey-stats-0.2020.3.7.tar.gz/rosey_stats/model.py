import warnings
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.feature_selection import f_regression, f_classif
from sklearn.exceptions import NotFittedError
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error, log_loss

try:
    from tqdm import tqdm
except ImportError:
    tqdm = False


def vec_to_array(a: np.ndarray):
    return a.reshape((len(a), 1))


# noinspection PyPep8Naming
class BairSupervisedPCA(BaseEstimator, TransformerMixin):
    """
    Supervised Principal Components Analysis
    This is the one as described by 'Prediction by Supervised Principal Components' (Eric Bair, Trevor Hastie et al)
    https://stats.stackexchange.com/a/767/91928
    NOTE -> Use sklearn LinearRegression over statsmodels OLS because it is ~3x faster.
    Example below
    >>> from sklearn.datasets import load_boston, load_breast_cancer
    >>> require_dims = 3
    >>> data, target = load_boston(True)
    >>> bspca = BairSupervisedPCA(n_components=require_dims)
    >>> trans_a = bspca.fit_transform(data, target)
    >>> trans_b = bspca.transform(data)
    >>> trans_a.ndim
    2
    >>> trans_a.shape[1]
    3
    >>> np.isclose(trans_a, trans_b).all()
    True
    >>> data, target = load_breast_cancer(True)
    >>> lspca = BairSupervisedPCA(require_dims)
    >>> trans_a = lspca.fit_transform(data, target)
    >>> trans_b = lspca.transform(data)
    >>> trans_a.ndim
    2
    >>> trans_a.shape[1]
    3
    >>> np.isclose(trans_a, trans_b).all()
    True
    >>> print('Done')
    Done
    """

    def __init__(self, n_components=None, is_regression=True, cv=5,
                 threshold_samples=25, use_pvalues=False, verbose=False):
        self.pca = PCA(n_components=n_components, whiten=True)
        self.conditioner_model_ = LinearRegression() if is_regression else LogisticRegression()
        self.cv, self.n_thres = cv, threshold_samples
        self.n_components = n_components
        self.is_regression, self.use_pvalues = is_regression, use_pvalues
        self.cv_results, self.indices, self.best = 3 * [None]
        self.verbose = verbose

        if use_pvalues:
            warnings.warn('Using p-values could select spurious features as important!')

    def _check_is_fitted(self):
        if self.indices is None or self.best is None:
            raise NotFittedError

    def plot_learning_curve(self, show_graph=False):
        import matplotlib.pyplot as graph
        try:
            from rosey_graph import plot_learning_curve as plc
        except ImportError:
            raise ImportError('You need have rosey-graph installed to call this function')
        self._check_is_fitted()

        plc(self.cv_results['mean'], self.cv_results['std'], self.cv_results['theta'], n=self.cv)
        graph.ylabel('R2 Score' if self.is_regression else 'Log loss')
        graph.xlabel(r'$\theta$')
        if show_graph:
            graph.show()

    def _univariate_regression(self, x, y):
        def model(x_i):
            lm_i = LinearRegression() if self.is_regression else LogisticRegression()
            lm_i.fit(vec_to_array(x_i), y)
            return lm_i.coef_[0]

        iterator = range(x.shape[1])
        if self.verbose and tqdm:
            iterator = tqdm(iterator, desc='Computing Coefs')
        return np.array([model(x[:, i]) for i in iterator])

    def fit(self, X, y):
        # Step 1 -> Compute (univariate) standard regression coefficient for each feature
        if self.use_pvalues:
            _, thetas = f_regression(X, y) if self.is_regression else f_classif(X, y)
            grid_sweep = np.linspace(thetas.min(), 1, self.n_thres)
        else:
            # Compute the regression coef like it says in the paper
            if self.is_regression:
                y_centered = y - np.mean(y)
                thetas = self._univariate_regression(X, y_centered)
            else:
                thetas = self._univariate_regression(X, y)
            # noinspection PyTypeChecker
            grid_sweep = np.percentile(np.abs(thetas), np.linspace(0.01, 1, self.n_thres)[::-1] * 100)

        # Step 2 -> Form a reduced data matrix
        thetas = (thetas if self.use_pvalues else np.abs(thetas)).flatten()
        cv_results = []
        for thres in grid_sweep:
            select = np.squeeze(np.argwhere(thetas <= thres) if self.use_pvalues else np.argwhere(thetas >= thres))
            x_selected = X[:, select]
            try:
                comps = float('inf') if self.n_components is None else self.n_components
                u_selected = PCA(min(x_selected.shape[1], comps), whiten=True).fit_transform(x_selected)
            except (ValueError, IndexError):
                u_selected = x_selected

            kf, scores = KFold(n_splits=self.cv, shuffle=True), []
            for train_ind, val_ind in kf.split(u_selected):
                # Split
                x_train, x_val = u_selected[train_ind], u_selected[val_ind]
                y_train, y_val = y[train_ind], y[val_ind]

                # Fit
                if x_train.ndim == 1:
                    x_train, x_val = vec_to_array(x_train), vec_to_array(x_val)

                if self.is_regression:
                    lm = LinearRegression().fit(x_train, y_train)
                else:
                    lm = LogisticRegression().fit(x_train, y_train)

                # Score
                y_hat = lm.predict(x_val)
                score = mean_squared_error(y_val, y_hat) if self.is_regression else log_loss(y_val, y_hat)

                # Test
                scores.append(score)

            # Score threshold
            scores = np.array(scores)
            cv_results.append((scores.mean(), scores.std()))
            if self.verbose:
                print(f'Theta -> {thres}', cv_results[-1])

        # Get best results
        self.cv_results = pd.DataFrame(cv_results, columns=['mean', 'std'])
        self.cv_results['theta'] = grid_sweep
        self.cv_results = self.cv_results.tail(len(self.cv_results) - 1)

        self.best = self.cv_results.sort_values(by='mean', ascending=False if self.is_regression else True).head(1)
        if self.use_pvalues:
            best_select = np.argwhere(thetas <= self.best['theta'].values)
        else:
            best_select = np.argwhere(thetas >= self.best['theta'].values)
        self.indices = np.squeeze(best_select)

        X = vec_to_array(X[:, self.indices]) if X[:, self.indices].shape[1] == 1 else X[:, self.indices]
        self.pca.fit(X)
        self.conditioner_model_.fit(self.pca.transform(X), y)

        return self

    def transform(self, X, y=None, **fit_params):
        self._check_is_fitted()

        # Step 3 -> Reduce X and then perform PCA
        x_reduced = X[:, self.indices]
        self.n_components = min(x_reduced.shape[1], float('inf') if self.n_components is None else self.n_components)
        return self.pca.transform(x_reduced)

    def fit_transform(self, X, y=None, **fit_params):
        assert y is not None
        if X.ndim == 1:
            raise ValueError('X cannot be a vector')
        elif X.shape[1] == 1:
            raise ValueError('X must have more than 1 feature')

        self.fit(X, y)
        return self.transform(X)

    def precondition(self, X):
        """
        This returns the preconditioned target variable (It predicts y from the input data)
        :param X:
        :return:
        """
        return self.conditioner_model_.predict(self.pca.transform(X[:, self.indices]))