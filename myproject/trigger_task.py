from myapp.api_utilis import get_comparable_items

# Trigger the task asynchronously
result = get_comparable_items.delay()

# Optionally, wait for the result
response = result.get(timeout=10)
print(response)
