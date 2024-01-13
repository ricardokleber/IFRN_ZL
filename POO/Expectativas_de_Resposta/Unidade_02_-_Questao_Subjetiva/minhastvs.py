from eletrodomesticos import Televisao

tv_sala = Televisao()
tv_sala.nome = "tv_sala"
tv_sala.tamanho = 32
tv_sala.marca = "Felipys"

tv_quarto = Televisao()
tv_quarto.nome = "tv_quarto"
tv_quarto.ligada = True
tv_quarto.marca = "Xilco"

if tv_sala.ligada == True:
    ligada = 'S'
else:
    ligada = 'N'
print(f'{tv_sala.nome} | {tv_sala.canal} | {tv_sala.tamanho} | {tv_sala.marca} | Ligada ({ligada})')

if tv_quarto.ligada == True:
    ligada = 'S'
else:
    ligada = 'N'
print(f'{tv_quarto.nome} | {tv_quarto.canal} | {tv_quarto.tamanho} | {tv_quarto.marca} | Ligada ({ligada})')