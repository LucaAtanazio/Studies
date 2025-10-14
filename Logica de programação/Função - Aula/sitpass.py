def calcular_gasto_diario(passagem, viagens_d):
    """Calcula o gasto diário com passagens."""
    return passagem * viagens_d

def calcular_gasto_periodo(gasto_d, periodo):
    """Calcula o gasto total no período."""
    return gasto_d * periodo

def calcular_viagens_extras(passagem, quantidade):
    """Calcula o custo das viagens extras."""
    return passagem * quantidade

def exibir_viagens_dia(viagens_d):
    """Exibe o resumo de viagens diárias."""
    print(f"""
    Viagens no dia:
    {'-'*50}
    Trabalho : 005 --> 305
    Faculdade : 112
    Casa : 020
    {'-'*50}
    Viagens no dia: {viagens_d}
    """)

def exibir_viagens_extras(viagens_ext):
    """Exibe o resumo de viagens extras."""
    print(f"""
    Viagens extras:
    {'-'*50}
    Sitpass : 004
    Exame : 005 * 2
    {'-'*50}
    Valor total: R${viagens_ext:.2f}
    """)

def exibir_resumo(passagem, gasto_d, periodo, gasto_periodo, viagens_ext, total, viagens_d):
    """Exibe o resumo completo dos gastos."""
    print(f"\nValor da passagem: R${passagem:.2f}")
    exibir_viagens_dia(viagens_d)
    print(f"Gasto diário: R${gasto_d:.2f}")
    print(f"Período: {periodo} dias")
    print(f"Gasto no período: R${gasto_periodo:.2f}")
    exibir_viagens_extras(viagens_ext)
    print(f"\nTotal geral: R${total:.2f}")
    print(f"Total com desconto (R$181.49): R${total - 181.49:.2f}")

def main():
    # Dados de entrada
    passagem = 4.3
    viagens_d = 4
    periodo = 21
    quant_viagens_ext = 4
    
    # Cálculos
    gasto_d = calcular_gasto_diario(passagem, viagens_d)
    gasto_periodo = calcular_gasto_periodo(gasto_d, periodo)
    viagens_ext = calcular_viagens_extras(passagem, quant_viagens_ext)
    total = gasto_periodo + viagens_ext
    
    # Exibição dos resultados
    exibir_resumo(passagem, gasto_d, periodo, gasto_periodo, viagens_ext, total, viagens_d)

if __name__ == "__main__":
    main()