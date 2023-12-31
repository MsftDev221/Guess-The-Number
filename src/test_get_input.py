from main import get_input


def test_input_decimal(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    usr_input = get_input("")
    assert usr_input == 1


def test_input_char(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "a")
    user_input = get_input("")
    assert user_input == False


def test_input_float(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1.2")
    user_input = get_input("")
    assert user_input == False
