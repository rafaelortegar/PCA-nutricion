import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def backward_elimination(data, target, significance_level):
    """
    Función que realiza el proceso de backward_elimination para elegir las variables significativas a 
    utilizar en las regresiones. 
    """
    features = data.columns.tolist()
    while(len(features)>0):
        features_with_constant = sm.add_constant(data[features])
        p_values = sm.OLS(target, features_with_constant).fit().pvalues[1:]
        max_p_value = p_values.max()
        if(max_p_value >= significance_level):
            excluded_feature = p_values.idxmax()
            features.remove(excluded_feature)
        else:
            break 
    return features

def backward_elimination_datos(pval):
    """
    Función que realiza el proceso de backward_elimination usando como variable dependiente hmat y hlec.
    """
    print("\t-> Importando los datos")
    #df = pd.read_csv('../../data/datos_limpios.csv')
    df = pd.read_csv('../data/datos_limpios.csv')
    print("\t-> Seleccionando variables para incluir en la regresión")
    data = df.reindex(columns=['p1','p2','p6','p7','p8','p10','p11','p12','p13','p14','p15',
                           'p16','p17','p18','p19','p20','p21','p22','p23','p24','p25',
                           'p26','p27','p28','p29','p30','p31','p32','p33','p34','p35',
                           'p36','p37','p38','p39','p40','p41','p42','p43','p44','p45',
                           'p46','p47','p48','p49','p50','p51','p52','p53','p54','p55',
                           'p56','p57','p58','p59','p60','p61','p62','p63','p64','p65',
                           'p66','p68','p69','p71','p72','p73','p75','p76','p77','p78',
                           'p79','p80','p81','p82','p83','p84','p85','p86','p87','p88',
                           'p89','p90','p91','p92','p93','p94','p95','p96','p97','p98',
                           'p99','p100','p101','p102','p103','p104','p105','p106','p107',
                           'p108','p109','p110','p111','p112','p113','p114','p115','p116',
                           'p117','p118','p119','p120','p121','p122','p123','p124','p125',
                           'p126','p127','p128','p129','p130','p131','p132','p133','p134',
                           'p135','p136','p137','p138','p139','p140','p141','p142','p143',
                           'p144','p145','p146','p147','p148','p149','p150','p151','p152',
                           'p153','p154','nom_ent_aguascalientes','nom_ent_baja_california',
                           'nom_ent_baja_california_sur','nom_ent_campeche','nom_ent_chiapas',
                           'nom_ent_chihuahua','nom_ent_coahuila','nom_ent_colima',
                           'nom_ent_durango','nom_ent_estado_de_mexico','nom_ent_guanajuato',
                           'nom_ent_guerrero','nom_ent_hidalgo','nom_ent_jalisco',
                           'nom_ent_michoacan','nom_ent_morelos','nom_ent_nayarit',
                           'nom_ent_nuevo_leon','nom_ent_oaxaca','nom_ent_puebla',
                           'nom_ent_queretaro','nom_ent_quintana_roo','nom_ent_san_luis_potosi',
                           'nom_ent_sinaloa','nom_ent_sonora','nom_ent_tabasco','nom_ent_tamaulipas',
                           'nom_ent_tlaxcala','nom_ent_veracruz','nom_ent_yucatan','nom_ent_zacatecas',
                           'modalidad_bachillerato_tecnologico','modalidad_tecnico_profesional',
                           'sost_autonomas','sost_federal','sost_particulares',
                           'subsist_bach_estatal_dge-cge','subsist_bachillerato_autonomo',
                           'subsist_cecyte','subsist_cobach','subsist_colbach/otros_federales',
                           'subsist_conalep','subsist_dgeti','subsist_telebach/emsad','p3_B',
                           'p3_C','p4_A','p4_C','p5_A','p5_C','p9_B','p9_C','p9_D','p9_E',
                           'p9_F','p9_G','p67_B','p67_C','p67_D','p67_E','p70_B','p70_C',
                           'p70_D','p70_E','p70_F','p70_G','p70_H','p74_B','p74_C','p74_D',
                           'p74_E','p74_F'])
    t_hmat = np.asarray(df.reindex(columns=['hmat']))
    t_hlec = np.asarray(df.reindex(columns=['hlec']))
    print("\t-> Haciendo backward_elimination para hmat")
    significativas_hmat = backward_elimination(data, t_hmat, pval)
    print("\t-> Haciendo backward_elimination para hlec")
    significativas_hlec = backward_elimination(data, t_hlec, pval)
    return data, significativas_hmat, significativas_hlec