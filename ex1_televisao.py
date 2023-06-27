class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 32
        self.marca = 'Samsung'


tv = Televisao()
# print(tv.ligada)
# print(tv.canal)

tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 4
# print(tv.canal)
# print(tv_sala.canal)


# Exercício de fixação
tv_quarto = Televisao()
tv_quarto.marca = 'LG'
tv_quarto.tamanho = 42
print(tv_quarto.marca, tv_quarto.tamanho)
print()

tv_cazinha = Televisao()
print(tv_cazinha.marca)
print(tv_cazinha.tamanho)
