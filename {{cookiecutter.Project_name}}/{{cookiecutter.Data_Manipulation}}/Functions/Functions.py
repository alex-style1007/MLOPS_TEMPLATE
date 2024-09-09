import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data(path):
    """Carga un conjunto de datos desde un archivo CSV.

    Args:
        path (str): Ruta al archivo CSV.

    Returns:
        pandas.DataFrame: DataFrame con los datos cargados.
    """

    df = pd.read_csv(path)
    return df

def preprocess_data(df):
    """Realiza el preprocesamiento de los datos.

    Args:
        df (pandas.DataFrame): DataFrame con los datos sin procesar.

    Returns:
        pandas.DataFrame: DataFrame con los datos preprocesados.
    """

    # Selección de características
    selected_features = ['feature1', 'feature2', 'feature3']
    df = df[selected_features]

    # Manejo de valores faltantes
    df.fillna(df.mean(), inplace=True)

    # Escalamiento de características
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)

    return df_scaled

def split_data(df, target_column):
    """Divide los datos en conjuntos de entrenamiento y prueba.

    Args:
        df (pandas.DataFrame): DataFrame con los datos.
        target_column (str): Nombre de la columna que contiene la variable objetivo.

    Returns:
        tuple: Tupla con los conjuntos de entrenamiento y prueba (X_train, X_test, y_train, y_test).
    """

    X = df.drop(target_column, axis=1)
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """Entrena un modelo de clasificación.

    Args:
        X_train (pandas.DataFrame): Conjunto de entrenamiento.
        y_train (pandas.Series): Etiquetas del conjunto de entrenamiento.

    Returns:
        sklearn.pipeline.Pipeline: Pipeline con el modelo entrenado.
    """

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier())
    ])

    pipeline.fit(X_train, y_train)

    return pipeline

def evaluate_model(model, X_test, y_test):
    """Evalúa el desempeño del modelo.

    Args:
        model (sklearn.pipeline.Pipeline): Modelo entrenado.
        X_test (pandas.DataFrame): Conjunto de prueba.
        y_test (pandas.Series): Etiquetas del conjunto de prueba.
    """

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")

# Ejemplo de uso
data_path = "data/my_dataset.csv"
df = load_data(data_path)
df_processed = preprocess_data(df)
X_train, X_test, y_train, y_test = split_data(df_processed, "target")
model = train_model(X_train, y_train)
evaluate_model(model, X_test, y_test)