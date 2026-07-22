import re
import ast
import numpy as np
from ml.models_loader import w2v

from pymorphy3 import MorphAnalyzer
from nltk.corpus import stopwords

morph = MorphAnalyzer()

popular_programming_languages = ['python', 'php', 'kotlin', 'swift', 'java', 'golang', 'go']
high_skill_counts = [1, 11, 13, 20, 21]

russian = stopwords.words('russian')
english = stopwords.words('english')
all_lang_stopwords = list(set(russian + english))

exp_mapping = {
    "Нет опыта": 0,
    "1-3 года": 1,
    "3-6 лет": 2,
    "6+ лет": 3
}

format_mapping = {
    "Не указано": 0,
    "Офис": 0,
    "Гибрид": 1,
    "Удалённо": 2
}

group_mapping = {
    'Системный администратор': 0,
    'Other': 1,
    'Developer/Manager': 2,
    'ML/Data': 3
}


def level_it_skills(title):
    title_lower = title.lower()
    title_list = title_lower.split(" ")

    if 'junior' in title_list:
        return 1
    elif 'middle' in title_list or 'ведущий' in title_list:
        return 2
    elif 'senior' in title_list or 'lead' in title_list:
        return 3
    else:
        return 0


def categorize_role(title):
    title_lower = title.lower()

    if any(word in title_lower for word in [
        'ml engineer', 'machine learning engineer', 'ml-инженер', 'nlp', 'computer vision', 'cv',
        'ml инженер', 'ml разработчик', 'ml/llm', 'genai', 'ai engineer']):
        return 'ML Engineer'

    elif any(word in title_lower for word in
             ['data scientist', 'data science', 'дата сайентист', 'дата саентист', 'scientist']):
        return 'Data Scientist'

    elif any(word in title_lower for word in ['data engineer', 'дата инженер', 'big data']):
        return 'Data Engineer'

    elif any(word in title_lower for word in
             ['data analyst', 'data analysis', 'аналитик данных', 'аналитик дата', 'analytics', 'product analyst']):
        return 'Data Analyst'

    elif any(word in title_lower for word in ['backend', 'бэкенд', 'back-end', 'back end']):
        return 'Backend'

    elif any(word in title_lower for word in [
        'frontend', 'фронтенд', 'front-end', 'front end',
        'react', 'angular', 'vue', 'javascript', 'typescript',
        'html', 'css', 'web-разработчик']):
        return 'Frontend'

    elif any(word in title_lower for word in ['fullstack', 'фуллстак', 'full-stack', 'full stack']):
        return 'Fullstack'

    elif any(word in title_lower for word in
             ['system administrator', 'sysadmin', 'системный администратор', 'администратор', 'linux']):
        return 'Системный администратор'

    elif any(word in title_lower for word in
             ['qa', 'тестировщик', 'test engineer', 'tester', 'автотестировщик', 'automation', 'quality assurance']):
        return 'QA'

    elif any(word in title_lower for word in
             ['project manager', 'product manager', 'pm', 'проджект', 'продакт', 'team lead', 'tech lead',
              'руководитель', 'менеджер']):
        return 'Management'

    elif any(word in title_lower for word in ['1с', '1c', 'битрикс', 'bitrix']):
        return '1C/Bitrix'

    else:
        return 'Other'


def regroup_role(role):
    if role in ['ML Engineer', 'Data Scientist', 'Data Engineer']:
        return 'ML/Data'
    elif role in ['Backend', 'Frontend', 'Fullstack', 'Management']:
        return 'Developer/Manager'
    elif role == 'Системный администратор':
        return 'Системный администратор'
    else:
        return 'Other'


def str_to_list(skill_str):
    try:
        return ast.literal_eval(skill_str)
    except:
        return []


def has_any_lang(skills):
    """Проверяет, есть ли в навыках хотя бы один язык программирования"""
    skills_lower = [s.lower() for s in skills]
    return int(any(lang in ' '.join(skills_lower) for lang in popular_programming_languages))


def count_skills(skills):
    if skills == ['Не указано']:
        return 0
    return len(skills)


def skills_vector(skills):
    """Превращает список навыков в вектор с помощью Word2Vec"""
    vectors = [w2v.wv[skill] for skill in skills if skill in w2v.wv and skill != "Не указано"]
    if not vectors:
        return np.zeros(100)
    return np.mean(vectors, axis=0)


def clean_detailed_info(text):
    text = text.lower()

    text = re.sub(r'[^а-яa-z0-9\s\.]', '', text)

    text = re.sub(r'\s+', ' ', text).strip()

    return text


def lemmatize_text(text):
    """Приводит все слова к начальной форме (лемматизация)"""
    words = str(text).split()
    lemmas = []

    for word in words:
        parsed = morph.parse(word)[0]
        lemmas.append(parsed.normal_form)

    return ' '.join(lemmas)


def remove_stopwords(text):
    words = text.split()
    filter_text = [word for word in words if word not in all_lang_stopwords]
    return ' '.join(filter_text)
