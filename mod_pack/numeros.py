# tratamento de erros para números
class Numbers:
    def __init__(self, n_int_range, n_int, num_float):
        self.n_int_range = n_int_range
        self.n_int = n_int
        self.num_float = num_float

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
