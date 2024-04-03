from pydantic import BaseModel, ValidationError

class VeiculoBase(BaseModel):
    valor: str
    marca: str
    modelo: str
    anoModelo: int


    
veiculo_data = {
    "valor": "R$ 9.235,00",
    "marca": "Fiat",
    "modelo": "Palio EX 1.0 mpi 2p",
    "anoModelo": "Ano Modelo 2000",
    "combustivel": "Gasolina",
    "codigoFipe": "001004-9",
    "mesReferencia": "abril de 2024 ",
    "tipoVeiculo": 1,
    "siglaCombustivel": "G",
    "dataConsulta": "terça-feira, 2 de abril de 2024 16:51"
}
        
try:
    veiculo = VeiculoBase(**veiculo_data)
    print("Dados Válidos!")
except ValidationError as e:
    print("Dados Inválidos!")
    print(e)
