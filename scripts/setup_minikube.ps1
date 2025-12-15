# Start Minikube
minikube start --driver=docker

# Enable the internal registry addon
minikube addons enable registry

# Set Docker environment to use Minikube’s Docker daemon
minikube -p minikube docker-env | Invoke-Expression

Write-Host "Minikube started, registry enabled, and Docker env configured!"
