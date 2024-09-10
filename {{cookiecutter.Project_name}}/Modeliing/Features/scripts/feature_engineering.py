import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_selection import SelectKBest, chi2

def crear_features(data):
    """
    Realiza la ingeniería de características en los datos.

    Args:
        data (pandas.DataFrame): DataFrame con los datos sin procesar.

    Returns:
        pandas.DataFrame: DataFrame con las características transformadas.
    """

    # Crear nuevas características
    data['nueva_feature'] = data['feature1'] * data['feature2']

    # Codificación One-Hot para variables categóricas
    categorical_cols = ['categoria1', 'categoria2']
    encoder = OneHotEncoder()
    encoded_features = encoder.fit_transform(data[categorical_cols])
    encoded_df = pd.DataFrame(encoded_features.toarray(), columns=encoder.get_feature_names_out())
    data = pd.concat([data, encoded_df], axis=1)

    # Escalado de variables numéricas
    numerical_cols = ['feature1', 'nueva_feature']
    scaler = StandardScaler()
    data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

    # Selección de características (opcional)
    selector = SelectKBest(chi2, k=10)
    X = data.drop('target', axis=1)  # Suponiendo que 'target' es la variable objetivo
    X_new = selector.fit_transform(X, data['target'])
    selected_features = X.columns[selector.get_support()]
    data = data[selected_features]

    return data

# Cargar los datos
data = pd.read_csv('datos_preparados/data.csv')

# Crear las nuevas características
data_con_features = crear_features(data)

# Guardar los datos con las características transformadas
data_con_features.to_csv('features/data/features_train.csv', index=False)