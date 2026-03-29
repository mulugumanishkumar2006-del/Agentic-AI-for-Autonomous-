import os

def ask_gemini(prompt):
    try:
        # 🔴 TEMP: Safe fallback (no API crash)
        return [
            "Analyze request",
            "Break into steps",
            "Execute workflow",
            "Verify completion"
        ]
    except Exception as e:
        print("Gemini failed:", e)
        return [
            "Fallback step 1",
            "Fallback step 2"
        ]