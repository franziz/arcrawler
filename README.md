# arcrawler
AmouRe Crawler.is an app. It is not a library that can be used universally. In order to run this perfectly, you need to follow step by step about how to use this app.

# Requirement
You will need:
- Docker
- Git

# Preparation
You will need a docker image called arcrawler. In order to download the docker image you need to do this
```bash
docker pull franziz/arcrawler
docker pull mongo

docker run -d --name mongo mongo
docker run -it --name arcrawler -v location_of_arcrawler:/root/app --link mongo:mongo franziz/arcrawler bash
ctrl+p+q
```

# How to use
1. Make source to be crawled (you can look at inside src folder)
2. Build (use build.py)
3. Run (use run.py)

# Remote Deployment
Future improvement