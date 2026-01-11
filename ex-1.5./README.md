# Assignment

Make the project respond something to a GET request sent to the / url of the project. A simple HTML page is good, or you can deploy something more complex, like a single-page application.

See [here](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/) how you can define environment variables for containers.

Use kubectl port-forward to confirm that the project is accessible and works in the cluster by using a browser to access the project.

# Solution

- Python source code can be found [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.5./todo-app/src/app.py)
- Deployment manifests can be found [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.5./manifests/deployment.yaml)
- Following commands were used to create and test deployment:
![todo-app-deployed.png](https://raw.githubusercontent.com/mark-feher/DevOps-with-Kubernetes/refs/heads/main/ex-1.5./todo-app-deployed.png)
![todo-app-deployed-port-forwarding-enabled.png](https://raw.githubusercontent.com/mark-feher/DevOps-with-Kubernetes/refs/heads/main/ex-1.5./todo-app-deployed-port-forwarding-enabled.png)
![todo-app-output.png](https://raw.githubusercontent.com/mark-feher/DevOps-with-Kubernetes/refs/heads/main/ex-1.5./todo-app-output.png)
![todo-app-output-browser.png](https://raw.githubusercontent.com/mark-feher/DevOps-with-Kubernetes/refs/heads/main/ex-1.5./todo-app-output-browser.png)
