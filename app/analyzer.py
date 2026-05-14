def analyze_security_event(log):

    log = log.lower()

    if "failed login" in log or "unauthorized" in log:
        return {
            "threat": "Possible Unauthorized Access",
            "severity": "High",
            "recommendation": "Investigate login attempts and review account activity."
        }

    elif "malware" in log or "virus" in log:
        return {
            "threat": "Malware Detection",
            "severity": "Critical",
            "recommendation": "Isolate affected systems immediately."
        }

    elif "port scan" in log or "nmap" in log:
        return {
            "threat": "Reconnaissance Activity",
            "severity": "Medium",
            "recommendation": "Monitor source IP and block suspicious traffic."
        }

    return {
        "threat": "Unknown",
        "severity": "Low",
        "recommendation": "Continue monitoring."
    }