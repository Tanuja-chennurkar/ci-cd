# Apply namespace
kubectl apply -f ..\k8s\namespace.yaml

# Apply deployment
kubectl apply -f ..\k8s\deployment.yaml

# Apply service
kubectl apply -f ..\k8s\service.yaml

Write-Host "Kubernetes deployment completed!"
