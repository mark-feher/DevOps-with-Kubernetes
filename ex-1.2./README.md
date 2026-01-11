# Assignment

Create a web server that outputs "Server started in port NNNN" when it is started and deploy it into your Kubernetes cluster. Please make it so that an environment variable PORT can be used to choose the used port. You may call the server todo app since it will, amongst other things, provide the functionality of a todo application pretty soon.

You will not have access to the port when it is running in Kubernetes yet. We will configure the access when we get to networking.

# Solution

- Python source code can be found [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.2./todo-app/src/app.py).
- Image was pushed to Docker Hub repo [markfeher/todo-app](https://hub.docker.com/r/markfeher/todo-app).
- Following commands were used to create and test deployment:
![todo-app-dockerized.png](https://raw.githubusercontent.com/mark-feher/DevOps-with-Kubernetes/refs/heads/main/ex-1.2./todo-app-dockerized.png)
![todo-app-deployed.png](https://raw.githubusercontent.com/mark-feher/DevOps-with-Kubernetes/refs/heads/main/ex-1.2./todo-app-deployed.png)
