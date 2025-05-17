import json

TEMPLATE = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Sprawdzanie kodów pelerynek</title>
    <style>
        body {{ font-family: sans-serif; padding: 2em; }}
        input, button {{ padding: 0.5em; font-size: 1em; }}
        .result {{ margin-top: 1em; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>Sprawdź kod pelerynki</h1>
    <input type="text" id="codeInput" placeholder="Wpisz kod peleryny">
    <button onclick="checkCode()">Sprawdź</button>
    <div class="result" id="result"></div>

    <script>
        const data = {json_data};

        function checkCode() {{
            const input = document.getElementById('codeInput').value.trim();
            const resultDiv = document.getElementById('result');
            if (!input) {{
                resultDiv.textContent = "Wpisz kod.";
                return;
            }}

            for (const category of data) {{
                for (const code of category.codes) {{
                    if (code.id === input) {{
                        if (code.used) {{
                            resultDiv.textContent = `Kod "${input}" został już użyty (kategoria: ${category.name}).`;
                        }} else {{
                            resultDiv.textContent = `Kod "${input}" jest dostępny (kategoria: ${category.name}).`;
                        }}
                        return;
                    }}
                }}
            }}

            resultDiv.textContent = `Kod "${input}" nie został znaleziony.`;
        }}
    </script>
</body>
</html>
"""

def convert_capes_json():
    with open("capes.json", "r") as f:
        original = json.load(f)

    # Konwersja do formatu z 'codes': [{id, used}]
    converted = []
    for entry in original:
        converted.append({
            "name": entry["name"],
            "codes": [
                {"id": code if isinstance(code, str) else code["id"], "used": False}
                for code in entry.get("ids", [])
            ]
        })

    return converted

if __name__ == "__main__":
    converted_data = convert_capes_json()

    with open("capes.html", "w", encoding="utf-8") as f:
        html = TEMPLATE.replace("{json_data}", json.dumps(converted_data, indent=4))
        f.write(html)

    print("Wygenerowano capes.html")