#!/usr/bin/env python3
"""
Скрипт для добавления тегов к промптам в prompts.yaml
Анализирует текст промпта и находит соответствующие теги на основе ключевых слов
"""

import yaml
import json
import re
from pathlib import Path

# Пути к файлам
SCRIPT_DIR = Path(__file__).parent
TAGS_FILE = SCRIPT_DIR / "data" / "tags.json"
YAML_FILE = SCRIPT_DIR / "data" / "prompts.yaml"
OUTPUT_FILE = SCRIPT_DIR / "data" / "prompts.yaml"

def load_tags():
    """Загружает теги из JSON файла"""
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        tags_data = json.load(f)
    return {tag['id']: tag['name'] for tag in tags_data}

def load_prompts():
    """Загружает промпты из YAML файла"""
    with open(YAML_FILE, 'r', encoding='utf-8') as f:
        prompts = yaml.safe_load(f)
    return prompts

def find_matching_tags(prompt_data, tags_dict):
    """
    Находит теги для промпта на основе анализа текста
    Анализирует: title, description, category, prompt
    """
    # Объединяем все текстовые поля для анализа
    text_to_analyze = ' '.join([
        prompt_data.get('title', ''),
        prompt_data.get('description', ''),
        prompt_data.get('category', ''),
        prompt_data.get('prompt', '')
    ]).lower()
    
    matched_tags = set()
    
    for tag_id, tag_name in tags_dict.items():
        # Проверяем tag_id (например: javascript, python, chatgpt)
        tag_id_lower = tag_id.lower()
        tag_name_lower = tag_name.lower()
        
        # Разбиваем tag_id на части (например: code_review -> code, review)
        tag_parts = re.split(r'[_\-]', tag_id_lower)
        
        # Проверяем точное совпадение tag_id или tag_name
        if tag_id_lower in text_to_analyze or tag_name_lower in text_to_analyze:
            matched_tags.add(tag_id)
            continue
        
        # Проверяем части тега (особенно для составных тегов)
        # Но только если слово достаточно длинное (> 3 символов), чтобы избежать ложных срабатываний
        matched_parts = 0
        for part in tag_parts:
            if len(part) > 3:  # Игнорируем короткие слова типа "ai", "llm"
                # Используем регулярное выражение для поиска слова
                if re.search(r'\b' + re.escape(part) + r'\b', text_to_analyze):
                    matched_parts += 1
        
        # Если найдено более одной значимой части тега, считаем это совпадением
        if matched_parts >= 2 or (len(tag_parts) == 1 and matched_parts == 1):
            matched_tags.add(tag_id)
    
    # Добавляем общие теги на основе category
    category = prompt_data.get('category', '').lower()
    category_mapping = {
        'programming': ['coding', 'development'],
        'writing': ['writing', 'creative_writing'],
        'marketing': ['marketing', 'seo'],
        'business': ['business', 'strategy'],
        'productivity': ['productivity', 'workflow'],
        'education': ['learning', 'teaching'],
        'career': ['career_advice', 'interview_prep'],
        'customer support': ['customer_support'],
    }
    
    for cat_key, cat_tags in category_mapping.items():
        if cat_key in category:
            for cat_tag in cat_tags:
                if cat_tag in tags_dict:
                    matched_tags.add(cat_tag)
    
    return sorted(list(matched_tags))

def add_tags_to_prompts():
    """Добавляет теги ко всем промптам"""
    print("Загрузка тегов...")
    tags_dict = load_tags()
    print(f"Загружено {len(tags_dict)} тегов")
    
    print("Загрузка промптов...")
    prompts = load_prompts()
    print(f"Загружено {len(prompts)} промптов")
    
    print("Добавление тегов к промптам...")
    for i, prompt in enumerate(prompts):
        tags = find_matching_tags(prompt, tags_dict)
        prompt['tags'] = tags
        
        if (i + 1) % 100 == 0:
            print(f"  Обработано {i + 1} промптов...")
    
    print(f"Теги добавлены ко всем {len(prompts)} промптам")
    
    # Сохраняем обновленный YAML
    print(f"Сохранение в {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(prompts, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=1000)
    
    print("Готово!")
    
    # Выводим статистику
    total_tags = sum(len(p.get('tags', [])) for p in prompts)
    print(f"\nСтатистика:")
    print(f"  Всего промптов: {len(prompts)}")
    print(f"  Всего тегов присвоено: {total_tags}")
    print(f"  Среднее тегов на промпт: {total_tags / len(prompts):.2f}")
    
    # Показываем примеры
    print("\nПримеры промптов с тегами:")
    for i, p in enumerate(prompts[:3]):
        print(f"  {p.get('id', 'unknown')}: {p.get('tags', [])}")

if __name__ == "__main__":
    add_tags_to_prompts()
