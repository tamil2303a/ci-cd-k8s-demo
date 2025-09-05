#!/usr/bin/env bash
set -euo pipefail

# Apply namespace + manifests
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

echo "Waiting for pods..."
kubectl -n demo rollout status deployment/demo-api

echo "Service:"
kubectl -n demo get svc demo-svc

echo "Open service in browser (minikube):"
minikube service demo-svc -n demo
