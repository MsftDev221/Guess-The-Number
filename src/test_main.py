from main import evaluate


def test_evaluate_less() -> None:
    result = evaluate(1, 2)[1]
    assert result == False


def test_evaluate_more() -> None:
    result = evaluate(2, 1)[1]
    assert result == False


def test_evaluate_equal() -> None:
    result = evaluate(1, 1)[1]
    assert result == True
