# CST8919 Lab 2: Building a Web App with Threat Detection using Azure Monitor and KQL

## What I Learned

During this lab, I learned how to:
- Deploy a Python Flask app to Azure App Service
- Configure diagnostic logging using Azure Monitor
- Use Kusto Query Language (KQL) to analyse app behaviour
- Create an alert rule that detects multiple failed login attempts

---

## Challenges Faced

- Initial deployment failures due to misplacement of app.py
- 503 and 404 errors from incorrect startup configuration
- Diagnosing logs when columns like `csUriStem` didn't match – fixed by inspecting available fields with `take 1`
- Setting up KQL alerts with the correct time frame and thresholds

### Why I used gunicorn and app.zip:
- I chose gunicorn because it's a production-ready Python web server that's required by Azure App Service to run Flask apps reliably on Linux. The default Flask server is for development only and doesn’t work well in Azure's environment.
- I used app.zip with ZIP Deploy because it provided me with more control compared to Git. It allowed me to quickly upload just the necessary files (app.py and requirements.txt) and avoid issues with broken Git pushes or extra folders.

---

## Real-World Improvement

In a real-world scenario:
- Track IP addresses:
Instead of just logging usernames and status codes, I would also log the client’s IP address to identify suspicious sources and block repeated failed attempts from the same location.

- Rate limiting / throttling:
I would add logic to limit login attempts per IP or user (e.g., max 5 tries in 10 minutes). This helps reduce brute-force attacks.

- Geo-location checks:
I could flag login attempts from unusual countries or IP ranges that differ from the user’s normal login behaviour.

- Database logging:
Instead of just printing logs to the console, I’d store login attempts in a secure database for long-term analysis and auditing.

- Automated blocking or flagging:
Use Azure Firewall, Application Gateway, or custom middleware to block IPs automatically or alert security teams in real time.

---

## KQL Query Explanation

```kql
AppServiceHTTPLogs // This is the log table that stores all incoming HTTP requests to your Azure Web App.
| where TimeGenerated > ago(5m) // This filters the logs to show only requests made in the last 5 minutes.
| where CsUriStem == "/login" // This narrows the results to just the /login route, which is where users try to log in.
| where ScStatus == 401 // This filters the results only to include failed login attempts — HTTP status code 401 means Unauthorised.
```

## YouTube Demo Link

https://youtu.be/Qh6V3zJCS2w

- The video shows:
- App deployed on Azure
- /login requests made using the .http file
- Logs appearing in Azure Monitor
- KQL query tested
- Alert setup and triggering demo



