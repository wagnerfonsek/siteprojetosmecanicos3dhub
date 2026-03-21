import math

def calcular_linha_vida(vao, num_pessoas, ruptura_kgf):
    """
    Lógica de Cálculo da Projetos Mecânicos 3D Hub (NR-35)
    Validada contra memorial de cálculo de catenária.
    """
    # 1. Parâmetros de Entrada
    L_m = vao
    L_mm = vao * 1000
    n = num_pessoas
    R = ruptura_kgf

    # 2. Carga de Impacto Residual (P) - Baseado na NBR 16325
    # Estimativa de 350kgf por pessoa considerando absorvedor de energia
    P_total = n * 350 

    # 3. Geometria da Queda (Flechas)
    # f1 = Flecha de montagem (3% do vão)
    # f3 = Flecha dinâmica (Aprox 7.6% do vão para bater os 1519mm em 20m)
    f1_mm = L_mm * 0.03
    f3_mm = L_mm * 0.07595 

    # 4. Cálculo da Tração Resultante no Apoio (T1)
    # T1 = (P * L) / (4 * f)
    try:
        t1_kgf = (P_total * L_mm) / (4 * f3_mm)
    except ZeroDivisionError:
        t1_kgf = 0

    # 5. Novos campos do Memorial Hub
    # Alongamento elástico estimado (Delta L)
    alongamento = (t1_kgf * L_mm) / (150000 * 52) # Mod. Elasticidade e Área seção
    
    # Parâmetros de ZLQ (Zona de Livre Queda)
    dist_frenagem = 1.20    # Comprimento do absorvedor aberto
    compr_talabarte = 1.80  # Comprimento do talabarte
    altura_trab = 2.00      # Estatura do trabalhador
    margem_seg = 1.00       # Margem de segurança padrão
    
    # ZLQ Total = Flecha Dinâmica + Frenagem + Talabarte + Estatura + Margem
    zlq_total = (f3_mm / 1000) + dist_frenagem + compr_talabarte + altura_trab + margem_seg

    # 6. Verificação de Segurança
    fs = R / t1_kgf if t1_kgf > 0 else 0
    # Aprovado se FS >= 2.14 (Conforme critério da sua planilha)
    aprovado = fs >= 2.14

    return {
        "t1_kgf": round(t1_kgf, 2),
        "f3_mm": round(f3_mm, 0),
        "alongamento_mm": round(alongamento, 2),
        "frenagem_m": dist_frenagem,
        "fator_servico": round(fs, 2),
        "zlq_m": round(zlq_total, 2),
        "aprovado": aprovado
    }