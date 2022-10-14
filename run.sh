# Execute the following command on non-gpu machine(s)
docker run -p 5005:5005 \
--name=vertex_ai_demo_container \
$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE

# Execute the following command on gpu machine(s)
# docker run --gpus=all -p 5005:5005 \
# --name=vertex_ai_container \
# $REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE

# The following command will send a request to server
# curl -X POST -d "@sample_input.json" -H "Content-Type: application/json" http://localhost:5005/predict
