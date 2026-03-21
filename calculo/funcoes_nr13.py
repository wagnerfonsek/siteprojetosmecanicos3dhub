import math

def calcular_volume_cilindro(diametro, altura):
    """Calcula volume do casco (m³)"""
    raio = diametro / 2
    return math.pi * (raio**2) * altura

def calcular_volume_tampo(tipo, diametro):
    """
    Calcula volume dos tampos (m³) baseado no seu Excel.
    """
    if tipo == "toriesferico_6":
        # Constante h2 = 0.169*D do seu Excel
        return 0.0809 * (diametro**3)
    
    elif tipo == "toriesferico_10":
        # Constante h2 = 0.194*D do seu Excel
        return 0.1009 * (diametro**3)
    
    elif tipo == "eliptico":
        # h2 = 0.25 * D
        h2 = 0.25 * diametro
        return (2/3) * math.pi * ((diametro/2)**2) * h2
    
    elif tipo == "hemisferico":
        return (2/3) * math.pi * ((diametro/2)**3)
    
    return 0

def calcular_pv_nr13(pressao_kgf, volume_m3, classe_fluido):
    """
    Calcula o P.V e a Categoria conforme a NR-13.
    """
    pv = pressao_kgf * volume_m3
    
    categoria = "V"
    if classe_fluido == 'A':
        if pv >= 100: categoria = "I"
        elif pv >= 30: categoria = "II"
        else: categoria = "III"
    elif classe_fluido == 'B':
        if pv >= 100: categoria = "I"
        elif pv >= 30: categoria = "II"
        elif pv >= 2.5: categoria = "III"
        else: categoria = "IV"
    elif classe_fluido in ['C', 'D']:
        if pv >= 100: categoria = "II"
        elif pv >= 30: categoria = "III"
        elif pv >= 2.5: categoria = "IV"
        else: categoria = "V"
        
    return round(pv, 2), categoria