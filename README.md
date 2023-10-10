# electron_selenium

#### Notes for capabilities if run Selenium node


Start Selenium hub

`java -jar selenium-server-standalone-3.141.59.jar -role hub`

Start Selenium node
`java -jar selenium-server-standalone-3.141.59.jar -role node -nodeConfig app.json`

app.json
```
{
  "capabilities":
  [
    {
      "browserName": "chrome",
	    "platformName": "WINDOWS",
      "maxInstances": 5,
      "seleniumProtocol": "WebDriver"
    }
  ],
  "proxy": "org.openqa.grid.selenium.proxy.DefaultRemoteProxy",
  "maxSession": 5,
  "port": 5555,
  "register": true,
  "registerCycle": 5000,
  "hub": "http://localhost:4444",
  "nodeStatusCheckTimeout": 5000,
  "nodePolling": 5000,
  "role": "node",
  "unregisterIfStillDownAfter": 60000,
  "downPollingLimit": 2,
  "debug": false,
  "servlets" : [],
  "withoutServlets": [],
  "custom": {}
}
```

Make sure pip install all required libraries

### RUN
`python app.test`
