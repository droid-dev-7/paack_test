import pytest
import sys, os
sys.path.append(os.path.abspath(".."))
from app.eltiempo import ElTiempo

city = "Gavà"
city_out_of_province = "Alicante"

def test_today(monkeypatch):
    eltiempo = ElTiempo()
    monkeypatch.setattr("sys.argv", ["eltiempo.py", "--today", city])
    output = ElTiempo.main(eltiempo, sys.argv)
    assert "The current temperature" in output

def test_av_max(monkeypatch):
    eltiempo = ElTiempo()
    monkeypatch.setattr("sys.argv", ["eltiempo.py", "--av_max", city])
    output = ElTiempo.main(eltiempo, sys.argv)
    assert "The weekly average max temperature" in output

def test_av_min(monkeypatch):
    eltiempo = ElTiempo()
    monkeypatch.setattr("sys.argv", ["eltiempo.py", "--av_min", city])
    output = ElTiempo.main(eltiempo, sys.argv)
    assert "The weekly average min temperature in" in output

def test_today_wrong_city(monkeypatch):
    eltiempo = ElTiempo()
    monkeypatch.setattr("sys.argv", ["eltiempo.py", "--today", city_out_of_province])
    with pytest.raises(SystemExit):
        assert ElTiempo.main(eltiempo, sys.argv)

def test_av_max_wrong(monkeypatch):
    eltiempo = ElTiempo()
    monkeypatch.setattr("sys.argv", ["eltiempo.py", "--av_max", city_out_of_province])
    with pytest.raises(SystemExit):
        assert ElTiempo.main(eltiempo, sys.argv) 

def test_av_min_wrong(monkeypatch):
    eltiempo = ElTiempo()
    monkeypatch.setattr("sys.argv", ["eltiempo.py", "--av_min", city_out_of_province])
    with pytest.raises(SystemExit):
        assert ElTiempo.main(eltiempo, sys.argv)  

def test_wrong_input_arg(monkeypatch):
    eltiempo = ElTiempo()
    monkeypatch.setattr("sys.argv", ["eltiempo.py", "--wrong_arg", city])
    with pytest.raises(SystemExit):
        assert ElTiempo.main(eltiempo, sys.argv)

def test_city_not_informed(monkeypatch):
    eltiempo = ElTiempo()
    monkeypatch.setattr("sys.argv", ["eltiempo.py", "--today", ""])
    with pytest.raises(SystemExit):
        assert ElTiempo.main(eltiempo, sys.argv)