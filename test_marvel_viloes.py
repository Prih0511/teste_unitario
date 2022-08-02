from marvel_viloes import Marvel_viloes
#gangue da Sky
sky = Marvel_viloes("Skyrim", ["arranhado do mau", "muito fofinha"], 4)

def test_set_nome():
    sky.set_nome("Sky")
    assert sky.nome == "Sky"

def test_get_nome():
    assert sky.get_nome() == "Sky"

def test_get_poder():
    assert sky.get_poder() == ["arranhado do mau", "muito fofinha"]

def test_set_poder():
    sky.set_poder(["arranhado do mau", "muito fofinha", "mordida duida"])
    assert sky.poderes == ["arranhado do mau", "muito fofinha", "mordida duida"]

def test_get_perigo():
    assert sky.get_perigo() == 4

def test_set_perigo():
    sky.set_perigo(5)
    assert sky.perigo == 5

def test_dominar_mundo():
    nivel = sky.dominar_mundo(sky.perigo)
    if sky.perigo <= 2:
        assert nivel == "Vilão Morto"
        
    elif sky.perigo > 2 and sky.perigo < 5:
        assert nivel == "Vilão Preso"

    else:
        assert nivel == "Vilão Dominou o Mundo"