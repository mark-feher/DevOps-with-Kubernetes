# Assignment

Split the "Log output" application into two different containers within a single pod:

    One generates a random string on startup and writes a line with the random string and timestamp every 5 seconds into a file.
    The other reads that file and provides the content in the HTTP GET endpoint for the user to see

You may find [this](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/) helpful now since there are more than one container running inside a pod.

# Solution
