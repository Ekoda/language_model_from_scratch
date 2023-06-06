import numpy as np
import pytest
from utils.math_utils import sigmoid_activation, sigmoid_derivative, tanh_activation, tanh_derivative, softmax


def test_sigmoid_activation():
    assert sigmoid_activation(1) == pytest.approx(0.73105857863, rel=1e-9)
    assert sigmoid_activation(-1) == pytest.approx(0.26894142137, rel=1e-9)
    assert sigmoid_activation(0) == 0.5

def test_sigmoid_derivative():
    assert sigmoid_derivative(sigmoid_activation(1)) == pytest.approx(0.19661193324, rel=1e-9)
    assert sigmoid_derivative(sigmoid_activation(-1)) == pytest.approx(0.19661193324, rel=1e-9)
    assert sigmoid_derivative(sigmoid_activation(0)) == 0.25

def test_tanh_activation():
    assert tanh_activation(0) == pytest.approx(0, rel=1e-9)
    assert tanh_activation(1) == pytest.approx(0.7615941559557649, rel=1e-9)
    assert tanh_activation(-1) == pytest.approx(-0.7615941559557649, rel=1e-9)

def test_tanh_derivative():
    assert tanh_derivative(tanh_activation(0)) == pytest.approx(1, rel=1e-9)
    assert tanh_derivative(tanh_activation(1)) == pytest.approx(0.41997434161402603, rel=1e-9)
    assert tanh_derivative(tanh_activation(-1)) == pytest.approx(0.41997434161402603, rel=1e-9)


def test_softmax():
    x = np.array([1, 2, 3, 4, 5])
    s_x = softmax(x)

    assert s_x.shape == x.shape
    assert np.isclose(np.sum(s_x), 1.0)

    x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    s_x = softmax(x, axis=1)
    
    assert s_x.shape == x.shape
    assert np.all(np.isclose(np.sum(s_x, axis=1), np.ones(2)))
    assert np.all(np.argmax(s_x, axis=1) == np.argmax(x, axis=1))