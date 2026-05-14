import pandas as pd
import requests as request
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

cidade ="Sao Paulo"
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

resposta = request.get(url)
if resposta.status_code == 200:
    dados = resposta.json()
    df = pd.json_normalize([dados])
    df['weather'] = dados['weather'][0]['description']
    
    dicionario_colunas = {
        'name': 'Cidade',
        'main.temp': 'Temperatura (ºC)',
        'main.humidity': 'Umidade (%)',
        'dt': 'Data/Hora',
        'sys.sunrise': 'Nascer do Sol',
        'sys.sunset': 'Pôr do Sol',
        'weather': 'Condição Atual'
    }
    df['data_hora'] = datetime.now()

    # 1. Renomeia as colunas
    df = df.rename(columns=dicionario_colunas)

    # 2. Converte os horários uma única vez (Já ajustando para SP)
    colunas_fuso = ['Data/Hora', 'Nascer do Sol', 'Pôr do Sol']
    
    for col in colunas_fuso:
        # to_datetime converte o número Unix
        # tz_localize e tz_convert ajustam o fuso
        # strftime transforma em texto para o display final
        df[col] = pd.to_datetime(df[col], unit='s', utc=True) \
                    .dt.tz_convert('America/Sao_Paulo')
    
    # Formatação visual
    df['Data/Hora'] = df['Data/Hora'].dt.strftime('%d/%m/%Y %H:%M')
    df['Nascer do Sol'] = df['Nascer do Sol'].dt.strftime('%H:%M')
    df['Pôr do Sol'] = df['Pôr do Sol'].dt.strftime('%H:%M')

    # 3. Filtra o resultado final
    df_limpo = df[["Cidade", "Temperatura (ºC)", "Condição Atual", "Data/Hora", "Nascer do Sol", "Pôr do Sol", "Umidade (%)", "data_hora"]]
    
    print(df_limpo)

    senha = quote_plus(os.getenv("DB_PASSWORD"))
    df_limpo = df_limpo.tail(1)  # pega só a última linha

    engine = create_engine(f"postgresql://postgres:{senha}@localhost:5432/clima")
    df_limpo.to_sql(
    "dados_climaticos",
    engine,
    if_exists="replace",
    index=False
    )

    print("Dados enviados para PostgreSQL")


else:
    print(f"Erro: {resposta.status_code}")