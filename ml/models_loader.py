import os
import joblib
from gensim.models import Word2Vec

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODELS_DIR = os.path.join(BASE_DIR, 'ml', 'models')

columns = joblib.load(os.path.join(MODELS_DIR, 'feature_columns.pkl'))
linear_model = joblib.load(os.path.join(MODELS_DIR, 'linear_model.pkl'))
tfidf = joblib.load(os.path.join(MODELS_DIR, 'tfidf_vectorizer.pkl'))
w2v = Word2Vec.load(os.path.join(MODELS_DIR, 'w2v_skills.model'))