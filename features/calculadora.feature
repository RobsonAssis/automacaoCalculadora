Feature: Abrir a caculadora cientifica

    @CP01
    Scenario: Abrir a calculadora e fazer uma conta
    Given que a calcudadora esteja aberta 
    When pesquiso a caculadora cientifica
    Then a caculadora cientifica sera aberta

    @CP02
    Scenario: Fazer conta simples na calculadora cientifica
    Given que a calculadora cientifica esteja aberta
    When calcular os valores
    Then o resultado da conta ira aparecer
