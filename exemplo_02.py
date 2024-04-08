import pandas as pd
from pydantic import BaseModel, ValidationError

class Order(BaseModel):
    order_date: str
    order_id: int
    ship_date: str
    units_sold: int
    unit_price: float
    unit_cost: float
    total_revenue: float
    total_cost: float
    total_profit: float
    country: str
    region: str
    sales_channel: str
    order_priority: str
    item_type: str

# Carregar o CSV para um DataFrame do Pandas
df = pd.read_csv('data/sales-data.csv')

# Renomear as colunas do DataFrame
df = df.rename(columns={
    'Region': 'region',
    'Country': 'country',
    'Item Type': 'item_type',
    'Sales Channel': 'sales_channel',
    'Order Priority': 'order_priority',
    'Order Date': 'order_date',
    'Order ID': 'order_id',
    'Ship Date': 'ship_date',
    'Units Sold': 'units_sold',
    'Unit Price': 'unit_price',
    'Unit Cost': 'unit_cost',
    'Total Revenue': 'total_revenue',
    'Total Cost': 'total_cost',
    'Total Profit': 'total_profit'
})

validation_sucess_control = True

# Validar em lote
for index, row in df.iterrows():
    try:
        Order(**row)
    except ValidationError as e:
        validation_sucess_control = False
        print(f"Erro de validação na linha {index}: {e}")


if validation_sucess_control:
    print("Todos os dados foram validados com sucesso.")
else:
    print("Houve erros durante a validação dos dados.")
