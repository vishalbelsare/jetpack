"""Tests for the signals module."""

from jetplot import signals
import numpy as np


def test_stable_rank():

    U, _ = np.linalg.qr(np.random.randn(32, 32))
    V, _ = np.linalg.qr(np.random.randn(32, 32))
    S = np.random.randn(32)

    X = U @ np.diag(S) @ V.T
    expected = (S ** 2).sum() / (S ** 2).max()
    computed = signals.stable_rank(X)
    print(expected)
    print(computed)

    assert np.allclose(expected, computed)


def test_participation_ratio():

    def _random_matrix(evals):
        dim = evals.size
        Q, _ = np.linalg.qr(np.random.randn(dim, dim))
        return Q @ np.diag(evals) @ Q.T
    
    C = _random_matrix(np.array([1., 0., 0.]))
    assert np.allclose(signals.participation_ratio(C), 1.0)

    C = _random_matrix(np.array([1., 1., 1.]))
    assert np.allclose(signals.participation_ratio(C), 3.0)


def test_smooth():
    pass


def test_cca():
    pass


def test_normalize():

    X = np.random.randn(10, 3)
    expected = np.stack([x / np.linalg.norm(x) for x in X])
    computed = signals.normalize(X)
    assert np.allclose(expected, computed)

    X = np.random.rand(4, 6)
    expected = np.stack([x / np.linalg.norm(x) for x in X.T]).T
    computed = signals.normalize(X, axis=0)
    assert np.allclose(expected, computed)
