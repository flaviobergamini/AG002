from unittest import result
import pandas as pd
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

class Artificial_Intelligence(object):

    # Realizando o teste da rede usando uma rede percepetron de multicamadas
    # hidden_layer_sizes -> Representa o número de neurônios na camada  intermediária(escondida)
    mlpClassifier = MLPClassifier(hidden_layer_sizes=(100), max_iter=1000, solver='lbfgs', verbose=True, tol=0.15, random_state=0)

    
    def __init__(self, data):
        self.data = data

        # Recuperando o valor dos dados obtidos do Banco de dados 
        data = self.data

        # Separando as amostras de treino e de teste
        train_dataX=data.iloc[:, 1:-1] # Feito o iloc para splitar os valores excluindo a coluna de crédito
        train_dataY=data.iloc[:, -1] # Feito o iloc para splitar os valores escolhendo somente os valores da coluna de crédito
        
        X_train, X_test, y_train, y_test = train_test_split(train_dataX, train_dataY, test_size=0.2, random_state=0)
        
        # Apresenta a % de amostras que foi usada para cada finalidade
        #print('Amostras para treino: ', round(X_train.shape[0] / data.shape[0] * 100, 1), '%')
        #print('Amostrar para testes: ', round(X_test.shape[0] / data.shape[0] * 100, 1), '%')

        self.mlpClassifier.fit(X_train, y_train)
        #print("Treinamento realizado com sucesso")
       
        y_pred = self.mlpClassifier.predict(X_test)
        self.acuracia = accuracy_score(y_test, y_pred)

        # extra
        self.matriz_confusao = confusion_matrix(y_test, y_pred)
        

    def metricas_avaliacao(self,matriz_confusao,acc):
        matriz_confusao=self.matriz_confusao
        acc=self.acuracia
        ## IMPRIMINDO A ACURACIA DO TREINAMENTO
        print(f'Acurácia final: {acc*100:.2f}%')

        #### Gráfico da matriz de confusão ####
        print('Matriz de confusão: \n', matriz_confusao)
        # Criar gráfico para matriz de confusão
        plt.figure(figsize=(10, 10))
        plt.imshow(matriz_confusao, interpolation='nearest')
        plt.title('Matriz de confusão')
        # Setar os valores na matriz de confusão
        plt.xticks(range(2), ['O', 'X'])
        plt.yticks(range(2), ['O', 'X'])
        # Setar o valor da matriz de confusão no gráfico
        for i in range(2):
            for j in range(2):
                plt.text(j, i, matriz_confusao[i, j], ha='center', va='center', color='red', fontsize=20)

        plt.colorbar()
        plt.show()
        plt.savefig('matriz_confusao.png')

        plt.close()


    def train(self):
        self.metricas_avaliacao(self.matriz_confusao,self.acuracia)
        

    def evaluate_client(self,x):
        client_result=self.mlpClassifier.predict(x)
        
        if(client_result==1):
            print("GOOD")
        else:
            print("BAD")

        

        
