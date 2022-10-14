from typing import Optional, Dict, Sequence, Tuple
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
from typing import Optional, Dict, Sequence, Tuple, Union, List
from google.cloud.aiplatform_v1beta1.types import ExplanationParameters, ExplanationMetadata


def deploy_model_with_dedicated_resources_sample(
    project,
    location,
    model_name: str,
    machine_type: str,
    endpoint: Optional[aiplatform.Endpoint] = None,
    deployed_model_display_name: Optional[str] = None,
    traffic_percentage: Optional[int] = 0,
    traffic_split: Optional[Dict[str, int]] = None,
    min_replica_count: int = 1,
    max_replica_count: int = 1,
    accelerator_type: Optional[str] = None,
    accelerator_count: Optional[int] = None,
    explanation_metadata: Optional[ExplanationMetadata] = None,
    explanation_parameters: Optional[ExplanationParameters] = None,
    metadata: Optional[Sequence[Tuple[str, str]]] = (),
    sync: bool = True,
):
    """
    Creates a model end-point and deploys the model onto Google Vertex AI.
    model_name: A fully-qualified model resource name or model ID.
          Example: "projects/123/locations/us-central1/models/456" or
          "456" when project and location are initialized or passed.
    """
    aiplatform.init(project=project, location=location)

    model = aiplatform.Model(model_name=model_name)

    # The explanation_metadata and explanation_parameters should only be
    # provided for a custom trained model and not an AutoML model.
    model.deploy(
        endpoint=endpoint,
        deployed_model_display_name=deployed_model_display_name,
        traffic_percentage=traffic_percentage,
        traffic_split=traffic_split,
        machine_type=machine_type,
        min_replica_count=min_replica_count,
        max_replica_count=max_replica_count,
        accelerator_type=accelerator_type,
        accelerator_count=accelerator_count,
        explanation_metadata=explanation_metadata,
        explanation_parameters=explanation_parameters,
        metadata=metadata,
        sync=sync,
    )

    model.wait()
    print("[OUTPUT]: Model display name: {}".format(model.display_name))
    print("[OUTPUT]: Model resource name: {}".format(model.resource_name))
    return model


if __name__ == "__main__":
    # Deploy VAE
    deploy_model_with_dedicated_resources_sample(
        project='forgerock-autoid',
        location='us-west2',
        model_name="6459780346765377536",
        machine_type='n1-standard-4',
    )
    # Deploy AE
    deploy_model_with_dedicated_resources_sample(
        project='forgerock-autoid',
        location='us-west2',
        model_name="8283175245897007104",
        machine_type='n1-standard-4',
    )