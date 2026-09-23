# 🏦 Sistema Bancário em Python (POO)

> Um sistema de simulação de contas bancárias desenvolvido em Python com foco em **Programação Orientada a Objetos (POO)**, modelando regras de negócio reais como saques, depósitos, transferências e emissão de extratos.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.12.8**
* Conceitos de **Programação Orientada a Objetos (POO)**:
  * Classes e Objetos
  * Método Construtor (`__init__`)
  * Atributos de Instância e Métodos de Comportamento
  * Interação entre Objetos

---

## ⚙️ Funcionalidades da Classe

A classe `ContaBancaria` gerencia as seguintes operações para cada conta criada:
1. **Depósito:** Adiciona fundos à conta de forma validada e registra a movimentação.
2. **Saque:** Realiza retiradas verificando se o valor é positivo e se há saldo suficiente.
3. **Transferência:** Move valores de uma conta de origem para uma conta de destino, atualizando o saldo e gerando lançamentos nos extratos de ambas as partes.
4. **Consulta de Saldo:** Exibe as informações resumidas do titular e o saldo atual formatado.
5. **Emissão de Extrato:** Lista todas as movimentações financeiras realizadas e exibe o saldo final.

---

## 🛠️ Como Executar o Projeto Localmente

### Pré-requisitos
* Ter o **Python** instalado na sua máquina.

### 1. Clonar o repositório
```bash
git clone [https://github.com/SEU_USUARIO/nome-do-repositorio.git](https://github.com/SEU_USUARIO/nome-do-repositorio.git)
cd nome-do-repositorio
