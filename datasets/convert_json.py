import csv, json

def convert(csv_file, output_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as f:
        for row in csv.DictReader(f):
            result.append({'model': model, 'fields': row})

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False))

convert('ads.csv', 'ad.json', 'ads.ad')
# convert('location.csv', 'location.json', 'location')
# convert('user.csv', 'user.json', 'user')