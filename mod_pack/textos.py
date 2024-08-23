from rich import print

# Tratamento de erros para saída de textos, apenas strings (números, espaços ou outros valores, não é permitido)


class Strings:
    def __init__(self, str_txt):
        self.str_txt = str_txt

    def str_txt(txt):
        while True:
            try:
                s = str(input(txt)).capitalize().strip()
                if s.isnumeric():
                    print(f"Erro! '{s}' O valor digitado não é permitido!")
                elif s == "":
                    print(f"Erro! '{s}' O valor digitado não é permitido!")
                else:
                    return s
            except Exception as e:
                print(f"Erro! '{txt}' O valor digitado não é permitido!")


# firulas de textos
class Cor:
    def __init__(self, azul, vermelho, verde, preto) -> None:
        self.azul = azul
        self.vermelho = vermelho
        self.verde = verde
        self.preto = preto

    def azul(txt):
        cor = f"[blue]{txt}[/]"
        return cor

    def vermelho(txt):
        cor = f"[red]{txt}[/]"
        return cor

    def verde(txt):
        cor = f"[green]{txt}[/]"
        return cor

    def preto(txt):
        cor = f"[black]{txt}[/]"
        return cor


class Texto:
    def __init__(self, italico, sublinhado, negrito) -> None:
        self.italico = italico
        self.sublinhado = sublinhado
        self.negrito = negrito

    def italico(txt):
        tx = f"[italic]{txt}[/]"
        return tx

    def sublinhado(txt):
        tx = f"[underline]{txt}[/]"
        return tx

    def negrito(txt):
        tx = f"[bold]{txt}[/]"
        return tx


class Separadores:
    def __init__(self, linha, titulo) -> None:
        self.linha = linha
        self.titulo = titulo

    def linha():
        tx = print(f"{'-':-^100}")
        return tx

    def titulo(txt):
        Separadores.linha()
        tx = str(print(f"{txt:^100}")).strip()
        Separadores.linha()
        return tx
