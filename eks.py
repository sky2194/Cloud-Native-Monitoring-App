from kubernetes import client, config

# Load the kubeconfig file to configure the client
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.ApiClient()

# Define the deployment manifest
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="cloudnative-deployment"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "cloudnative-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "cloudnative-app"}),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="cloudnative-container",
                        image="031822725486.dkr.ecr.ca-central-1.amazonaws.com/cloudnative-app:latest",
                        ports=[client.V1ContainerPort(container_port=5000)],
                    )
                ]
            ),
        ),
    ),
)

# Create the deployment in the default namespace
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    body=deployment, namespace="default"
)

# Define the service manifest
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="cloudnative-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "cloudnative-app"},
        ports=[client.V1ServicePort(protocol="TCP", port=80, target_port=5000)],
    )
)

# create the service in the default namespace
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    body=service, namespace="default"
)   


print("Deployment created successfully.")
