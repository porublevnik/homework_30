import json

def convert(input_file, output_file, model):
    result = []
    with open(input_file, encoding='utf-8') as f:
        text = json.load(f)
        for i in text:
            result.append({'model': model, 'fields': i})

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False))

convert('ads.json', 'ads.json', 'ad')
convert('categories.json', 'categories.json', 'ad')