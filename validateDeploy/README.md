# action-trigger-test-wait

## Inputs
### app
**Required** - app name
### gitSha
**Required** - Github sha with 7 lenght long
### maxAttempt
**Required** - Max Attempt counter how many times to try
### sleepTime
**Required** - pause between attempts


## Usages
```yaml
- uses: psingh-cariq/customActions/k8sAppDeploy@main
  name: Trigger deploy and wait
  with:
    app: user
    gitSha: 12345676
    maxAttempt: 10
    sleepTime: 5
```
