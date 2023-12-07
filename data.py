import re

def textHandler(text):
    text = text.lower()
    text = re.sub(r'\s+',' ', text)
    return text


def apiHandler(gpt_response):
    
    parts = gpt_response.split()

    # Inicializar variables para almacenar la clasificación, probabilidad y detalles
    classification = None
    likelihood = None
    details = None

    for i in range(len(parts)):
        if parts[i] == "Classification:":
            classification = parts[i + 1] if i + 1 < len(parts) else None
        elif parts[i] == "Likelihood:":
            likelihood = parts[i + 1] if i + 1 < len(parts) else None
        elif parts[i] == "Details:":
            details = ' '.join(parts[i + 1:]) if i + 1 < len(parts) else None

    return details, likelihood, classification      

    