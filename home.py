import pandas as pd
import streamlit as st
from joblib import load
from notebooks.src.config import DADOS_TRATADOS, MODELO_FINAL

@st.cache_data
def carregar_dados():
    return pd.read_parquet(DADOS_TRATADOS)

@st.cache_resource
def carregar_modelo():
    return load(MODELO_FINAL)

df = carregar_dados()
modelo = carregar_modelo()

niveis_educacionais_texto = {
    1: "Below College",
    2: "College",
    3: "Bachelor",
    4: "Master",
    5: "PhD"  
}

niveis_satisfacao_texto = {
    1: "Low",
    2: "Medium",
    3: "High",
    4: "Very High"
}

niveis_vida_trabalho_texto = {
    1: "Bad",
    2: "Good",
    3: "Better",
    4: "Best" 
}

generos = sorted(df["Gender"].unique())
niveis_educacionais = sorted(df["Education"].unique())
area_formacao = sorted(df["EducationField"].unique())
departamentos = sorted(df["Department"].unique())
viagem_negocios = sorted(df["BusinessTravel"].unique())
hora_extra = sorted(df["OverTime"].unique())
satisfacao_trabalho = sorted(df["JobSatisfaction"].unique())
satisfacao_colegas = sorted(df["RelationshipSatisfaction"].unique())
satisfacao_ambiente = sorted(df["EnvironmentSatisfaction"].unique())
vida_trabalho = sorted(df["WorkLifeBalance"].unique())
opcao_acoes = sorted(df["StockOptionLevel"].unique())
envolvimento_trabalho = sorted(df["JobInvolvement"].unique())

colunas_slider = [
    "DistanceFromHome",
    "MonthlyIncome",
    "NumCompaniesWorked",
    "PercentSalaryHike",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager"
]

colunas_ignoradas = (
    "Age",
    "DailyRate",
    "JobLevel",
    "HourlyRate",
    "MonthlyRate",
    "PerformanceRating"
)

mediana_colunas_ignoradas = {
    coluna: df[coluna].median() for coluna in colunas_ignoradas
}

colunas_slider_min_max = {
    coluna: {"min_value": df[coluna].min(), "max_value": df[coluna].max()}
    for coluna in colunas_slider
}

st.title("Previsão de Atrito")

with st.container(border=True):
    st.write("### Informações Pessoais")

    widget_genero = st.radio("Genero", generos)
    widget_distancia_casa = st.slider(
        "Distância de casa (KM)", **colunas_slider_min_max["DistanceFromHome"]
    )
    widget_nivel_educacional = st.selectbox(
        "Nível Educacional",
        niveis_educacionais,
        format_func = lambda numero: niveis_educacionais_texto[numero]
    )
    widget_area_formacao = st.selectbox("Área de formação", area_formacao)

with st.container(border=True):
    st.write("### Rotina na Empresa")

    coluna_esquerda, coluna_direita = st.columns(2)

    with coluna_esquerda:
        widget_departamento = st.selectbox("Departamento", departamentos)
        widget_viagem_negocios = st.selectbox("Viagem Negócios", viagem_negocios)

    with coluna_direita:
        widget_cargo = st.selectbox(
            "Cargo",
            sorted(df[df["Department"] == widget_departamento]["JobRole"].unique())
        )
        widget_horas_extras = st.radio("Horas Extras", hora_extra)
        
    widget_salario_mensal = st.slider(
                "Salário Mensal",
                **colunas_slider_min_max["MonthlyIncome"]
            )

with st.container(border=True):
    st.write("### Experiência Profissional")

    coluna_esquerda, coluna_direita = st.columns(2)

    with coluna_esquerda:
        widget_empresas_trabalhadas = st.slider(
            "Empresas Trabalhadas",
            **colunas_slider_min_max["NumCompaniesWorked"]
        )
        widget_anos_trabalhados = st.slider(
            "Anos Trabalhados",
            **colunas_slider_min_max["TotalWorkingYears"]
        )
        widget_anos_empresa= st.slider(
            "Anos na Empresa",
            **colunas_slider_min_max["YearsAtCompany"]
        )

    with coluna_direita:
        widget_anos_cargo_atual= st.slider(
            "Anos no Cargo Atual",
            **colunas_slider_min_max["YearsInCurrentRole"]
        )
        widget_anos_mesmo_gerente= st.slider(
            "Anos com o Mesmo Gerente",
            **colunas_slider_min_max["YearsWithCurrManager"]
        )
        widget_anos_ultima_promocao= st.slider(
            "Anos Desde a Última Promoção",
            **colunas_slider_min_max["YearsSinceLastPromotion"]
        )

with st.container(border=True):
    st.write("### Incentivos e Métricas de Satisfação")

    coluna_esquerda, coluna_direita = st.columns(2)

    with coluna_esquerda:
        widget_satisfacao_trabalho = st.selectbox(
            "Satisfação com o Trabalho",
            satisfacao_trabalho,
            format_func = lambda numero: niveis_satisfacao_texto[numero]
        )
        widget_satisfacao_colegas = st.selectbox(
            "Satisfação com os Colegas",
            satisfacao_colegas,
            format_func = lambda numero: niveis_satisfacao_texto[numero]
        )
        widget_envolvimento_trabalho = st.selectbox(
            "Envolvimento com o Trabalho",
            satisfacao_ambiente,
            format_func = lambda numero: niveis_satisfacao_texto[numero]
        )

    with coluna_direita:
        widget_satisfacao_ambiente = st.selectbox(
            "Satisfação com o Ambiente",
            satisfacao_ambiente,
            format_func = lambda numero: niveis_satisfacao_texto[numero]
        ) 
        widget_balanco_vida_trabalho = st.selectbox(
            "Balanço Vida-Trabalho",
            vida_trabalho,
            format_func = lambda numero: niveis_vida_trabalho_texto[numero]
        )
        widget_opcao_acoes = st.radio("Opção de Ações", opcao_acoes)

    widget_aumento_salarial = st.slider(
        "Aumento Salarial (%)",
        **colunas_slider_min_max["PercentSalaryHike"]
    )
    widget_treinamentos_ultimo_ano = st.slider(
        "Treinamentos no Último Ano",
        **colunas_slider_min_max["TrainingTimesLastYear"]
    )

entrada_modelo = {
    "Age": mediana_colunas_ignoradas["Age"],
    "BusinessTravel": widget_viagem_negocios,
    "DailyRate": mediana_colunas_ignoradas["DailyRate"],
    "Department": widget_departamento,
    "DistanceFromHome": widget_distancia_casa,
    "Education": widget_nivel_educacional,
    "EducationField": widget_area_formacao,
    "EnvironmentSatisfaction": widget_satisfacao_ambiente,
    "Gender": widget_genero,
    "HourlyRate": mediana_colunas_ignoradas["HourlyRate"],
    "JobInvolvement": widget_envolvimento_trabalho,
    "JobLevel": mediana_colunas_ignoradas["JobLevel"],
    "JobRole": widget_cargo,
    "JobSatisfaction": widget_satisfacao_trabalho,
    "MaritalStatus": "Single",
    "MonthlyIncome": widget_salario_mensal,
    "MonthlyRate": mediana_colunas_ignoradas["MonthlyRate"],
    "NumCompaniesWorked": widget_empresas_trabalhadas,
    "PerformanceRating": mediana_colunas_ignoradas["PerformanceRating"],
    "OverTime": widget_horas_extras,
    "PercentSalaryHike": widget_aumento_salarial,
    "RelationshipSatisfaction": widget_satisfacao_colegas,
    "StockOptionLevel": widget_opcao_acoes,
    "TotalWorkingYears": widget_anos_trabalhados,
    "TrainingTimesLastYear": widget_treinamentos_ultimo_ano,
    "WorkLifeBalance": widget_balanco_vida_trabalho,
    "YearsAtCompany": widget_anos_empresa,
    "YearsInCurrentRole": widget_anos_cargo_atual,
    "YearsSinceLastPromotion": widget_anos_ultima_promocao,
    "YearsWithCurrManager": widget_anos_mesmo_gerente
}
df_entrada_modelo = pd.DataFrame([entrada_modelo])
        
botao_previsao = st.button("Prever Atrito")

if botao_previsao:
    previsao = modelo.predict(df_entrada_modelo)[0]
    probabilidade_atrito = modelo.predict_proba(df_entrada_modelo)[0][1]

    cor = ":red" if previsao == 1 else ":green"

    texto_probabilidade = (
        f"### Probabilidade de Atrito: {cor}[{probabilidade_atrito:.2f}]"
    )
    texto_atrito = f"### Atrito: {cor}[{'sim' if previsao == 1 else 'Não'}]" 
        
    st.markdown(texto_atrito)
    st.markdown(texto_probabilidade)
