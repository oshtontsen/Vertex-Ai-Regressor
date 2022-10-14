# NOTE: Open the docker desktop app if you forget your login
source gcs.env
docker login
docker build --tag=$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE .
