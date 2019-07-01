#CP01
@given(u'que a calcudadora esteja aberta')
def step_impl(context):
    context.calc.valida_abertura()

@when(u'pesquiso a caculadora cientifica')
def step_impl(context):
    context.calc.abrir_cientifica()



@then(u'a caculadora cientifica sera aberta')
def step_impl(context):
    context.calc.valida_cientifica()


#CP02
@given(u'que a calculadora cientifica esteja aberta')
def step_impl(context):
    context.calc.valida_cientifica()

@when(u'calcular os valores')
def step_impl(context):
    context.calc.calcular(valor1='9',operacao='multiplicacao', valor2='2')

@then(u'o resultado da conta ira aparecer')
def step_impl(context):
    context.calc.valida_valor()
