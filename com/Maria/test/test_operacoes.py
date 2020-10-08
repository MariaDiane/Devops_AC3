def feminicidio(pct):
    if int(pct)==1:        
        return "Agressão"
    else:
        return "Tortura"

def test_agressao():
    assert feminicidio(1) == 'Agressão'

def test_tortura():
    assert feminicidio(2) == 'Tortura'
