Write-Host "Building Docker image..."

docker build -t flask-app:latest ..\app

if ($LASTEXITCODE -ne 0) {
    Write-Error "Docker build failed"
    exit 1
}

Write-Host "Loading image into Minikube..."

minikube image load flask-app:latest

if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to load image into Minikube"
    exit 1
}

Write-Host "Image successfully loaded into Minikube!"
