
import requests, json, sys

url = "https://hba1c-trial-1001096826473.us-central1.run.app"

def test(payload):
    try:
        r = requests.post(url, json=payload, timeout=10)
        print("Response:", r.text)
        try:
            print("JSON:", json.dumps(r.json(), indent=2, ensure_ascii=False))
        except Exception:
            pass
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    test({"hba1c": 5.2})  
    test({"hba1c": 6.2})  