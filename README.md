##Google Container Engine 
gcloud config set compute/zone us-central1-b

##Google Container Registry
###Install Docker
>> sudo apt-get install apt-transport-https ca-certificates
>> sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

For Ubuntu 16.04

>>sudo vi /etc/apt/sources.list.d/docker.list
>>deb https://apt.dockerproject.org/repo ubuntu-xenial main
>>sudo apt-get update
>>sudo apt-get purge lxc-docker
>>sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual
>>sudo apt-get install docker-engine
>>sudo service docker start
>>sudo usermod -a -G docker nithink
>>sudo systemctl enable docker

###Creating the Docker File
>>sudo docker build -t sample .
>>sudo docker run -d -p 45001:11211 sample -name nithin
>>sudo docker exec -it ec6daaaeb442da683a8c741549e9e378caefa00e1039d357f0e5582e1001a077  bash
>>sudo docker stop ec6daaaeb442da683a8c741549e9e378caefa00e1039d357f0e5582e1001a077
>>sudo docker ps -a
>>sudo docker run -it --name nithin sample
 
### Build and Start Docker 
>>docker build -t webserver .
>>docker run -e GUNICORN_WORKERS=4 -e GUNICORN_ACCESSLOG=- -p 8000:8000 webserver

### Pushing Docker image to the registry
>> docker tag webserver gcr.io/q-project-x/webserver
>> cloud docker push gcr.io/q-project-x/webserver


###Run a container Image 
>> gcloud container clusters create ws-cluster --machine-type g1-small --num-nodes 1
>> gcloud components install kubectl
>> kubectl run ws --image=gcr.io/q-project-x/webserver:latest --port=8000
>> kubectl expose deployment ws --type="LoadBalancer"
>> kubectl get service wskubectl cluster-info
>> kubectl cluster-info
>> kubectl delete services ws
>> gcloud container clusters delete ws-cluster


##Web Service
Falcon framework is used for web service  
