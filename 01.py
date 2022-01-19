#!/usr/bin/env python
# coding: utf-8

# In[2]:


nome = 'Nome'
sobrenome = 'Sobrenome'
idade = 'Idade'
peso = 'Peso'

print(nome + ' ' + sobrenome + ', ' + idade + ', ' + peso + '.')

qtde_vendas_suco = 400
qtde_vendas_refrigerante = 540
preco_unt_suco = 2.60
preco_unt_refrigerante = 3.00
custo_loja = 2500.00

faturamento_suco = qtde_vendas_suco * preco_unt_suco
print(faturamento_suco)

faturamento_refrigerante = qtde_vendas_refrigerante * preco_unt_refrigerante
print(faturamento_refrigerante)

faturamento = faturamento_suco + faturamento_refrigerante
lucro = faturamento - custo_loja
print(lucro)

margem = lucro / faturamento
print(margem)


# In[3]:


suco = 'BEB1300543'
refrigerante = 'BEB1300545'
vinho = 'BAC1546001'
vodka = 'BAC17675002'

#BEB = Bebida não alcoólica
#BAC = Bebida alcoólica

codigo = input('Insira o código da bebida (Insira em letra maiúscula):')
print('BAB' in codigo)


# In[ ]:




