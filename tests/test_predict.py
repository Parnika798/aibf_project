"""
test_predict.py
----------------
Basic unit tests for src/predict.py.

Run with:  pytest tests/
Note: requires model/clf_pipeline1.pkl and model/label_encoder1.pkl to be
present (see README for where to get them).
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import pytest
from src.predict import get_classifier


@pytest.fixture(scope="module")
def classifier():
    return get_classifier()


def test_model_loads(classifier):
    assert classifier is not None
    assert classifier.pipeline is not None
    assert classifier.label_encoder is not None


def test_predict_returns_known_label(classifier):
    label = classifier.predict("My debit card was charged twice for the same transaction")
    assert isinstance(label, str)
    assert label != ""


def test_predict_empty_string_returns_unknown(classifier):
    assert classifier.predict("") == "Unknown"
    assert classifier.predict(None) == "Unknown"


def test_predict_batch(classifier):
    texts = [
        "Unauthorized transaction on my account",
        "Loan application was rejected without explanation",
    ]
    results = classifier.predict_batch(texts)
    assert len(results) == 2
    assert all(isinstance(r, str) for r in results)


def test_predict_with_confidence(classifier):
    label, confidence = classifier.predict_with_confidence("Account was blocked without notice")
    assert isinstance(label, str)
    assert confidence is None or 0.0 <= confidence <= 1.0
