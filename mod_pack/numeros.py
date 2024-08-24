# tratamento de erros para números
class Numbers:
    def __init__(self, n_int_range, n_int, num_float, cpf):
        self.n_int_range = n_int_range
        self.n_int = n_int
        self.num_float = num_float
        self.cpf = cpf

    def n_int(num):
        while True:
            try:
                n = int(input(num))
                return n
            except Exception as e:
                print("Erro! Apenas números inteiros!\n", type(e), ":", e)

    def n_int_range(num, i=1, f=3):
        """
        Tratamento de erro para números inteiros, com range

        Args:
            num (int): apenas numeros inteiros de i=inicio até o f=fim
            i (int, optional): valor inicial aceitável. Defaults to 1.
            f (int, optional): valor final aceitáveç. Defaults to 3.

        Returns:
            n: retorna o número digitado
        """
        while True:
            try:
                n = int(input(num))
                if n < i or n > f:
                    print(f"Erro! Digite um valor entre as opções acima {i} / {f}")
                else:
                    return n
            except Exception as e:
                print(f"Erro! Digite um valor entre as opções acima {i} / {f}\n", e)

    def num_float(num):
        while True:
            try:
                n = float(input(num))
                return f"{n:.2f}"
            except Exception as e:
                print("Erro! Apenas números decimais!")

    def cpf(num):
        while True:
            try:
                n = str(input(num)).strip().replace(".", "").replace("-", "")
                if n.isnumeric():
                    n = n
                else:
                    print("Erro! Valor informado é inválido, digite apenas números")
            except Exception as e:
                print(
                    f"Erro! Valor informado é inválido, digite apenas números\n   {type(e)}: {e}"
                )

            n_dgt = n[:9]
            mult = 10
            soma = 0

            for i in n_dgt:
                soma += int(i) * mult
                mult -= 1
            p_dgt = soma % 11

            if p_dgt < 2:
                p_dgt = 0
            else:
                p_dgt = 11 - p_dgt

            d_dgt = str(n_dgt) + str(p_dgt)
            mult = 11
            soma = 0

            for i in d_dgt:
                soma += int(i) * mult
                mult -= 1
            s_dgt = soma % 11
            if s_dgt < 2:
                s_dgt = 0
            else:
                s_dgt = 11 - s_dgt

            comparador1 = str(p_dgt) + str(s_dgt)
            comparador2 = n[9:]

            if comparador1 == comparador2:
                print("CPF Válido!")
                return n
            else:
                print("CPF Inálido!")
