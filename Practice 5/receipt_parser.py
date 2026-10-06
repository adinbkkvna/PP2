import json
import re

with open("raw.txt", "r", encoding="utf-8") as f:
  text = f.read()

#1|3
price_pattern = r"\d{1,3}(?: \d{3})*,\d{2}"
all_prices = re.findall(price_pattern, text)

if all_prices:
  total_amount = all_prices[-1]
else:
  total_amount = "0,00"

#2
item_pattern = r"\d+\.\s*\n(.*?)\n\d+,\d{3}\s*x\s*[\d\s]+,\d{2}\nСтоимость\n([\d\s]+,\d{2})"
matches = re.findall(item_pattern, text, re.DOTALL)

items = []
for product_name, price in matches:
  clean_name = re.sub(r"\s+", " ", product_name).strip()
  items.append({"product": clean_name, "cost": price.strip()})

#4
date_time_pattern = r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})"
dt_match = re.search(date_time_pattern, text)

if dt_match:
  date_time = dt_match.group(1)
else:
  date_time = "Не найдено"

#5
payment_pattern = r"(Банковская карта|Наличные):"
pay_match = re.search(payment_pattern, text)

if pay_match:
  payment_method = pay_match.group(1)
else:
  payment_method = "Банковская карта"


#6
receipt_data = {
    "store": "ТОО EUROPHARMA АСТАНА",
    "date_time": date_time,
    "payment_method": payment_method,
    "items_count": len(items),
    "items": items,
    "total_amount": total_amount,
}

print(json.dumps(receipt_data, ensure_ascii=False, indent=4))

with open("parsed_receipt.json", "w", encoding="utf-8") as out:
  json.dump(receipt_data, out, ensure_ascii=False, indent=4)