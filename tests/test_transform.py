import sys
import os
import pytest
import json
from datetime import date
# Adds the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import transform as t

def test_none_case():
    assert t.treat_neo_data(None) == None

def test_treat():
    path = os.path.dirname(os.path.abspath(__file__))
    with open(path+'/dump.json','r',encoding='utf-8') as f:
        try:
            data = json.load(f)
        except(ValueError,json.JSONDecodeError) as e:
            pytest.fail(f"Treat 0: {e}")
    a,c = t.treat_neo_data(data)
    assert isinstance(a,list) and isinstance(c,list), "Treat 1: A saída deve retornar 2 listas."
    assert a and c, "Treat 2: Listas não podem estar vazias."
    assert isinstance(a[0],tuple) and isinstance(c[0],tuple), "Treat 3: o conteúdo das listas devem ser tuplas."
    assert (len(a[0]) == 6),"Treat 4: asteroids devem ter 6 campos."
    assert isinstance(a[0][2],float),"Treat 4: asteroid[2] deve ser float."
    assert isinstance(a[0][3],bool),"Treat 4: asteroid[3] deve ser float."
    assert isinstance(a[0][4],float),"Treat 4: asteroid[4] deve ser float."
    assert isinstance(a[0][5],float),"Treat 4: asteroid[5] deve ser float."
    assert (len(c[0]) == 5),"Treat 5: close_approaches devem ter 5 campos."
    assert isinstance(c[0][1],date),"Treat 4: close_approache[2] deve ser Date."
    assert isinstance(c[0][2],float),"Treat 4: close_approache[3] deve ser float."
    assert isinstance(c[0][3],float),"Treat 4: close_approache[4] deve ser float."

