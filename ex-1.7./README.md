# Assignment

"Log output" application currently outputs a timestamp and a random string (that it creates on startup) to the logs.

Add an endpoint to request the current status (timestamp and the random string) and an Ingress so that you can access it with a browser.

You can just store the random string to the memory.

# Solution

- Deployment manifests can be found [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.7./manifests/deployment.yaml)
- Service manifests can be found [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.7./manifests/service.yaml)
- Ingress manifests can be found [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.7./manifests/ingress.yaml)
- Following commands were used to create and test deployment:
![log-output-ingress.png](https://raw.githubusercontent.com/mark-feher/DevOps-with-Kubernetes/refs/heads/main/ex-1.7./log-output-ingress.png)
![log-output-ingress-output.png](https://raw.githubusercontent.com/mark-feher/DevOps-with-Kubernetes/refs/heads/main/ex-1.7./log-output-ingress-output.png)
![log-output-ingress-output-browser.png](https://raw.githubusercontent.com/mark-feher/DevOps-with-Kubernetes/refs/heads/main/ex-1.7./log-output-ingress-output-browser.png)
