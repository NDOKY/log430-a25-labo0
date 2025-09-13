"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="
    assert my_calculator.addition(2, 3) == 5
    assert my_calculator.subtraction(6,2) == 4
    assert my_calculator.multiplication(2,2) == 4
    assert my_calculator.division(6,2) == 3
    assert my_calculator.division(6,0) == "Erreur : division par zéro"
    assert my_calculator.addition(5,6) == 43 #test renvoyant volontairement une erreur 
    
# TODO: ajoutez les tests