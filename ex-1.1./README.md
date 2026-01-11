# Assignment

Exercises can be done with any language and framework you want.

Create an application that generates a random string on startup, stores this string into memory, and outputs it every 5 seconds with a timestamp. e.g.

Deploy it into your Kubernetes cluster and confirm that it's running with kubectl logs ...

You will keep building this application in future exercises. This application will be called Log output.

# Solution

- Python source code can be found [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.1./log_output/src/app.py).
- Image was pushed to Docker Hub repo [markfeher/log_output](https://hub.docker.com/r/markfeher/log_output).
- Following commands were used to create and test deployment:
![log_output-dockerized.png](https://raw.githubusercontent.com/mark-feher/DevOps-with-Kubernetes/refs/heads/main/ex-1.1./log_output-dockerized.png)
![log_output-deployed.png](https://raw.githubusercontent.com/mark-feher/DevOps-with-Kubernetes/refs/heads/main/ex-1.1./log_output-deployed.png)
