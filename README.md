# electron_selenium

#### Notes for capabilities if run Selenium node

```
{
  "capabilities": [
    {
      "browserName": "chrome",
      "maxInstances": 1,
      "seleniumProtocol": "WebDriver",
      "chromeOptions": {
        "binary": "app_path.exe",
        "args": [
          "--ignore-certificate-errors",
          "remote-debugging-port=9515",
          "--start-maximized"
        ]
      }
    }
  ],
  "proxy": "org.openqa.grid.selenium.proxy.DefaultRemoteProxy",
  "maxSession": 1,
  "port": 5555,
  "register": true,
  "registerCycle": 5000,
  "hub": "http://localhost:4444"
}
```

Make sure pip install all required libraries

### RUN
`python app.test`
