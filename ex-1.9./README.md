# Assignment

Develop a second application that simply responds with "pong 0" to a GET request and increases a counter (the 0) so that you can see how many requests have been sent. The counter should be in memory so it may reset at some point. Create a new deployment for it and have it share ingress with "Log output" application. Route requests directed '/pingpong' to it.

In future exercises, this second application will be referred to as "ping-pong application". It will be used with "Log output" application.

The ping-pong application will need to listen to requests on '/pingpong', so you may have to make changes to its code. This can be avoided by configuring the Ingress to rewrite the path, but we will leave that as an optional exercise. You can check out [ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/#the-ingress-resource).

# Solution

- Python source code [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.9./pingpong/src/app.py).
- Deployment manifest [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.9./pingpong/manifests/deployment.yaml).
- Service manifest [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.9./pingpong/manifests/service.yaml).
- Ingress manifest [here](https://github.com/mark-feher/DevOps-with-Kubernetes/blob/main/ex-1.9./pingpong/manifests/ingress.yaml).
- Following commands were used to create and test deployment:
