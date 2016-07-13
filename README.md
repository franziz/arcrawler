# arcrawler
AmouRe Crawler.is an app. It is not a library that can be used universally. In order to run this perfectly, you need to follow step by step about how to use this app.

# Requirement
You will need:
1. Docker
2. Git

# Preparation
You will need a docker image called arcrawler. In order to download the docker image you need to do this
```bash
docker pull franziz/arcrawler
docker pull mongo
docker pull rabbitmq:management

docker run -d --name mongo mongo
docker run -d --name rabbitmq --hostname rabbitmq -p port_to_web_gui:15672 rabbitmq:management
docker run -it --name arcrawler -v location_of_arcrawler:/root/app --link mongo:mongo --link rabbitmq:rabbitmq franziz/arcrawler bash
ctrl+p+q
```

# How to use
1. Make source to be crawled (you can look at inside src folder)
2. Build (use build.py)
3. Test (use test.py)
4. Deploy (use deploy.py)
