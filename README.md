# Vertex-Ai-Regressor
This project serves as a base template to deploy a model on Vertex AI via custom Docker container and Flask.

To execute this project, follow the below steps:
  1. Add the proper credentials and project specifications in gcs.env.
  2. Install docker desktop or authenticate yourself via CLI
  3. . build.sh (Restart Docker if you encounter error: "failed to copy files: copy file range failed: no space left on device
")
  4. Verify that the docker images was created using: docker images
  5. . run.sh
  6. Verify that the docker container was created using: docker ps -a
  7. Send request to Flask server using: curl -X POST -d "@data/sample_input_vector.json" -H "Content-Type:application/json" http://localhost:5005/predict
  8. Create GCP Artifact Repo using: 
gcloud beta artifacts repositories create $REPOSITORY \
 --repository-format=docker \
 --location=$REGION
  9. Push docker image to GCP Artifact Registry repo: docker push $REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE
  10. Upload custom model: gcloud beta ai models upload \
  --region=$REGION \
  --display-name=$MODEL_NAME \
  --container-image-uri=$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE \
  --container-ports=5005 \
  --container-health-route=/healthz \
  --container-predict-route=/predict
  11. Go to GCS Dashboard > Vertex AI and verify your model
  12. Execute test.py to send HTTP request to deployed model and get prediction
