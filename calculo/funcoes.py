def calcular_linha_vida(vao, num_pessoas, ruptura_kgf):
    # Lógica baseada na sua planilha Hub (NR-35)
    carga_p_kgf = 350 * num_pessoas 
    f1_mm = (vao * 1000) * 0.03
    f3_mm = f1_mm * 2.53
    t1_kgf = (carga_p_kgf * (vao * 1000)) / (4 * f3_mm)
    fator_servico = ruptura_kgf / t1_kgf
    
    return {
        "t1_kgf": round(t1_kgf, 2), 
        "fator_servico": round(fator_servico, 2), 
        "aprovado": fator_servico >= 2.0
    }