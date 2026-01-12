# Assignment

Switch to using Ingress instead of NodePort to access the project. You can delete the Ingress of the "Log output" application so they don't interfere with this exercise. We'll look more into paths and routing in the next exercise, and at that point, you can configure the project to run with the "Log output" application side by side.

# Solution

- Deployment manifests can be found [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.8./manifests/deployment.yaml)
- Service manifests can be found [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.8./manifests/service.yaml)
- Ingress manifests can be found [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.8./manifests/ingress.yaml)
- Following commands were used to create and test deployment:
![todo-app-ingress.png](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.8./todo-app-ingress.png)
![todo-app-ingress-output.png](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.8./todo-app-ingress-output.png)
![todo-app-ingress-output-browser.png](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.8./todo-app-ingress-output-browser.png)
