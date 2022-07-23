# scowin-microservices

Required Tools:
1) Docker
2) Kuburnetes
3) Minikube

Steps to run Microservices in Docker:

1) Clone the Git Repository
https://github.com/nvallore/scowin-microservices

2) Run Docker Desktop

3) Navigate to Repo folder

4) Run -$ docker-compose build 
This builds all the docker images

5) Run -$ docker-compose up
This starts all the docker images

Through NGINX we can access the endpoints
eg: http://localhost/students/students, http://localhost/vaccination/student-vaccination

Steps to run Microservices in Kuburnetes:

1) Clone the Git Repository
https://github.com/nvallore/scowin-microservices

2) Run Docker Desktop

3) In terminal run - $ minikube start
This command starts the minikube

4) Navigate to Repo folder

4) Apply the kuburnetes migrations from kube directory
kubectl apply -f kube

5) When the services, pods and PVC are up, we can access the application and see logs
To see info about pods - $ kubectl get pod
To see info about services - $ kubectl get service
To see logs of particular pod - $ kubectl describe pod {pod_name}
To get the url to access service - $ minikube service {service_name} --url
** Note: for minikube cluster in local the url CLI should be open till we want to access the app



