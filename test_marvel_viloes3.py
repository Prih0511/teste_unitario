from marvel_viloes import Marvel_viloes

billy = Marvel_viloes("Billy", ["latido super_sonico", "mordida sem dó"], 3)

def test_set_nome():
    billy.set_nome("Billy")
    assert billy.nome == "Billy"

def test_get_nome():
    assert billy.get_nome() == "Billy"

def test_get_poder():
    assert billy.get_poder() == ["latido super_sonico", "mordida sem dó"]

def test_set_poder():
    billy.set_poder(["latido super_sonico", "mordida sem dó", "rosnado raivoso"])
    assert billy.poderes == ["latido super_sonico", "mordida sem dó", "rosnado raivoso"]

def test_get_perigo():
    assert billy.get_perigo() == 3

def test_set_perigo():
    billy.set_perigo(4)
    assert billy.perigo == 4

def test_dominar_mundo():
    nivel = billy.dominar_mundo(billy.perigo)
    if billy.perigo <= 2:
        assert nivel == "Vilão Morto"
        
    elif billy.perigo > 2 and billy.perigo < 5:
        assert nivel == "Vilão Preso"

    else:
        assert nivel == "Vilão Dominou o Mundo"