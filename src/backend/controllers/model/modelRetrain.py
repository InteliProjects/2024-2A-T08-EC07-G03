from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from controllers.datalake import upload_file
from controllers.DataWarehouse.file_manager_warehouse import download_file_warehouse
from routers.crud import insert_model
from pydantic import BaseModel
from datetime import datetime
import pandas as pd
import numpy as np
from io import StringIO
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix



class ModelTraining(BaseModel):
    model_name: str
    training_accuracy: float
    date: str 

async def retrainModel(name_file: str):
    try:
        
        file_content = await download_file_warehouse(name_file)
        
        csv_content = file_content['content']
            
        # Tranformar em um dataframe
        df = pd.read_csv(StringIO(csv_content))
        
        # Selecionar apenas as colunas numéricas para normalização
        colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns

        # Instanciar o MinMaxScaler
        scaler = MinMaxScaler()

        # Aplicar o scaler para as colunas numéricas
        df[colunas_numericas] = scaler.fit_transform(df[colunas_numericas])
                
        # Definir X como todas as colunas, exceto 'temFalha' e 'KNR'
        X = df.drop(['temFalha', 'KNR'], axis=1).values

        # Definir Y como a coluna 'temFalha'
        Y = df['temFalha'].values

        X = np.expand_dims(X, axis=1)  # Adicionando uma dimensão de tempo
        
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        
        X_train = np.array(X_train, dtype=np.float32)
        
        # Modelo
        
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50, return_sequences=False))
        model.add(Dropout(0.2))
        model.add(Dense(units=1, activation='sigmoid'))
        
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        # Treinando o modelo
        model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
        
        loss, accuracy = model.evaluate(X_test, y_test)
        print(f'Test Accuracy: {accuracy:.2f}')

        # Previsões
        predictions = model.predict(X_test)
        
        predictions_binary = (predictions > 0.05).astype(int)
        
        # Calculando métricas
        precision = precision_score(y_test, predictions_binary)
        recall = recall_score(y_test, predictions_binary)
        f1 = f1_score(y_test, predictions_binary)
        conf_matrix = confusion_matrix(y_test, predictions_binary)

        # Exibindo as métricas
        print(f'Precision: {precision:.2f}')
        print(f'Recall: {recall:.2f}')
        print(f'F1-Score: {f1:.2f}')
        print('Confusion Matrix:')
        print(conf_matrix)
                        
        # Formatar o nome do modelo com a data
        model_name = f'model_{datetime.now().strftime("%Y-%m-%d")}'
        
        model.save(f'{model_name}.h5')

        model_data = ModelTraining(model_name=model_name, training_accuracy=accuracy, date=datetime.now().strftime("%Y-%m-%d"))
        
        await insert_model(model_data)
        
        # # Salvar os dados no datalake
        # await upload_file(csv_file)
        
        return {"message": "Modelo treinado com sucesso"}
    
    except Exception as e:
        return {"message": f"Erro ao treinar o modelo: {str(e)}"}
    


    
    
        

    