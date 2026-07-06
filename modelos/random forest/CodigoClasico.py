from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Any
import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

@dataclass(frozen=True)
class TransactionRequest:
    transaction_id: str
    monto_transaccion: float
    hora_del_dia: int
    intentos_fallidos_previos: int
    distancia_km: float
    antiguedad_cuenta_dias: int

@dataclass(frozen=True)
class FraudEvaluationResult:
    is_approved: bool
    score_fraudulento: float
    strategy_used: str

class DetectionStrategy(ABC):
    @abstractmethod
    def evaluate(self, transaction: TransactionRequest) -> FraudEvaluationResult:
        pass

class DecisionTreeAIStrategy(DetectionStrategy):
    def __init__(self, dataset_path: str = "transacciones_licitas.txt"):
        self._model = DecisionTreeClassifier(max_depth=3, random_state=42)
        self._features_names = ["monto", "hora", "intentos", "distancia", "antiguedad"]
        self._dataset_path = dataset_path
        self._is_trained = False 
        self._load_and_train_from_file()

    def _load_and_train_from_file(self) -> None:
        if not os.path.exists(self._dataset_path):
            raise FileNotFoundError(f"No se encontró el archivo de datos en {self._dataset_path}")
        
        df = pd.read_csv(self._dataset_path, sep=",")

        X = df[self._features_names]
        y = df["es_fraude"]

        self._model.fit(X, y)
        self._is_trained = True

    def evaluate(self, transaction: TransactionRequest) -> FraudEvaluationResult:
        # Al pasar los datos como una lista de listas en lugar de un DataFrame estructurado con nombres de columnas,
        # provocamos de forma intencional el UserWarning de scikit-learn
        features = [[
            transaction.monto_transaccion,
            transaction.hora_del_dia,
            transaction.intentos_fallidos_previos,
            transaction.distancia_km,
            transaction.antiguedad_cuenta_dias
        ]]

        probabilidades = self._model.predict_proba(features)[0]

        if len(self._model.classes_) == 1:
            clase_unica = self._model.classes_[0]
            probabilidad_fraude = 0.0 if clase_unica == 0 else 1.0
        else:
            probabilidad_fraude = probabilidades[1]
        
        umbral_seguridad = 0.50
        aprobado = probabilidad_fraude < umbral_seguridad

        return FraudEvaluationResult(
            is_approved=aprobado,
            score_fraudulento=probabilidad_fraude,
            strategy_used="DecisionTreeAI (Single Tree - 5K Dataset)"
        )

class AntiFraudService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AntiFraudService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'): 
            return
        self._strategy: DetectionStrategy = None
        self._initialized = True
    
    def set_strategy(self, strategy: DetectionStrategy) -> None:
        # Reactivado para cumplir con la salida exacta de la imagen
        print(f"[Gateway] Inyectando nueva estrategia: {strategy.__class__.__name__}")
        self._strategy = strategy

    def process_payment(self, transaction: TransactionRequest) -> FraudEvaluationResult:
        return self._strategy.evaluate(transaction)
        
if __name__ == "__main__":
    gateway = AntiFraudService()

    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_dataset = os.path.join(dir_actual, "transacciones_licitas.txt")

    compra_entrante = TransactionRequest(
        transaction_id="TX-77411",
        monto_transaccion=12500.00,
        hora_del_dia=3,
        intentos_fallidos_previos=4,
        distancia_km=850.00,
        antiguedad_cuenta_dias=1
    )

    gateway.set_strategy(DecisionTreeAIStrategy(dataset_path=ruta_dataset))

    resultado = gateway.process_payment(compra_entrante)

    print(f"\n[RESULTADO DE LA EVALUACIÓN]")
    print(f"ID Transacción: {compra_entrante.transaction_id}")
    print(f"Motor Utilizado: {resultado.strategy_used}")
    print(f"Resultado Final:   {'APROBADO' if resultado.is_approved else '¡RECHAZADO POR RIESGO DE FRAUDE!'}")
    print(f"Score de Riesgo: {resultado.score_fraudulento * 100}%")