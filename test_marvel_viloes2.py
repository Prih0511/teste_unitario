from marvel_viloes import Marvel_viloes

luna = Marvel_viloes("Luna", ["lambida molhadona", "abraço de urso"], 2)

def test_set_nome():
    luna.set_nome("Lulu")
    assert luna.nome == "Lulu"

def test_get_nome():
    assert luna.get_nome() == "Lulu"

def test_get_poder():
    assert luna.get_poder() == ["lambida molhadona", "abraço de urso"]

def test_set_poder():
    luna.set_poder(["lambida molhadona", "abraço de urso", "cabeçada sinistra"])
    assert luna.poderes == ["lambida molhadona", "abraço de urso", "cabeçada sinistra"]

def test_get_perigo():
    assert luna.get_perigo() == 2

def test_set_perigo():
    luna.set_perigo(3)
    assert luna.perigo == 3

def test_dominar_mundo():
    nivel = luna.dominar_mundo(luna.perigo)
    if luna.perigo <= 2:
        assert nivel == "Vilão Morto"
        
    elif luna.perigo > 2 and luna.perigo < 5:
        assert nivel == "Vilão Preso"

    else:
        assert nivel == "Vilão Dominou o Mundo"