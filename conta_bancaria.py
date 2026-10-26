
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido.")
        else:
            self._saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor


conta = ContaBancaria("João", 100.00)

conta.depositar(50.00)
conta.sacar(30.00)

print(f"Saldo final: R$ {conta.saldo:.2f}")
