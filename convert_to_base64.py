import base64

with open("1.pdf", "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

print(encoded)