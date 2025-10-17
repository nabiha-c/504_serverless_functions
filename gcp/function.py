import json
import functions_framework

@functions_framework.http
def hba1c_go(request):
    """HTTP Cloud Function for HbA1c classification """

   
    data = request.get_json(silent=True) or {}
    args = request.args or {}

    hba1c = data.get("hba1c", args.get("hba1c"))

    # Check for presence
    if hba1c is None:
        return (
            json.dumps({"error": "Field 'hba1c' is required."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Validate 
    try:
        hba1c_val = float(hba1c)
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "'hba1c' must be a number."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Apply rule
    if hba1c_val < 5.7:
        status = "normal"
        category = "Normal (<5.7%)"
    else:
        status = "abnormal"
        category = "Abnormal (≥5.7%)"

    payload = {
        "hba1c": hba1c_val,
        "status": status,
        "category": category,
    }

    return json.dumps(payload), 200, {"Content-Type": "application/json"}
