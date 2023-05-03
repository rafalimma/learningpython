"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 99  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_carro_passou_radar = velocidade > RADAR_1
carro_passou_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
if carro_passou_radar:
    print('carro passou pelo radar')

if velocidade_carro_passou_radar:
    print('aviso de velocidade')

if carro_passou_radar and velocidade_carro_passou_radar:
    print('carro multado em radar')
