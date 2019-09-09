docker build . -t forensics-api
docker run -p5000:5000 -v$(pwd)/src:/app/ forensics-api


https://data.lip6.fr/cadene/pretrainedmodels/
