""" Unit tests for the app. """

import app


class TestPredictSales:
    """Tests for the predict sales function."""

    @staticmethod
    def test_size():
        """Test predictions size."""
        for i in range(1, 6, 1):
            assert app.predict_sales(i).shape[0] == i

    @staticmethod
    def test_frequency():
        """Test predictions frequency."""
        pred = app.predict_sales(10)
        assert pred.index.freq == "W"
        assert (pred.index[1] - pred.index[0]).days == 7

    @staticmethod
    def test_magnitude():
        """Test predictions maginutede."""
        values = app.predict_sales(10).values
        assert values.max() < 5e4
        assert values.min() > 5e3
