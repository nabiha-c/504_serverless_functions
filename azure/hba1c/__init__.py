import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """HTTP Azure Function for HbA1c classification.
    Returns JSON classification (normal / abnormal) 
    """
    try:
        data = req.get_json()
    except ValueError:
        data = {}

    hba1c = data.get("hba1c") or req.params.get("hba1c")

    if hba1c is None:
        return func.HttpResponse(
            json.dumps({"error": "Field 'hba1c' is required."}),
            status_code=400,
            mimetype="application/json"
        )

    try:
        hba1c_val = float(hba1c)
    except (TypeError, ValueError):
        return func.HttpResponse(
            json.dumps({"error": "'hba1c' must be a number."}),
            status_code=400,
            mimetype="application/json"
        )

    if hba1c_val < 5.7:
        status = "normal"
        category = "Normal (<5.7%)"
    else:
        status = "abnormal"
        category = "Abnormal (≥5.7%)"

    load = {
        "hba1c": hba1c_val,
        "status": status,
        "category": category,
    }

    return func.HttpResponse(
        json.dumps(load),
        status_code=200,
        mimetype="application/json"
    )
