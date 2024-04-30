# Cell Segmentation Using YOLO v8

This project focuses on cell segmentation using YOLO v8, a state-of-the-art deep learning model for object detection and segmentation. The model aims to segment cells in images accurately and efficiently.

## Workflows

1. **Constants**: Contains constant values used across the project.
2. **Entity**: Defines the entity classes and data structures.
3. **Components**: Contains various components required for the project.
4. **Pipelines**: Describes the data pipelines and workflows.
5. **App.py**: Main application file that ties everything together.

## How to Run?

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yash-raj202134/cell-segmentation-using-yolov-8.git
    ```

2. **Create a conda environment**:

    ```bash
    conda create -n cell python=3.8 -y
    conda activate cell
    ```

3. **Install the requirements**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:

    ```bash
    python app.py
    ```

5. **Access the application**:

    Open up your local host and port in a web browser to access the application.

## Azure CI/CD Deployment with GitHub Actions

### Run from Terminal

1. **Build the Docker image**:

    ```bash
    docker build -t cellseg.azurecr.io/cell:latest .
    ```

2. **Log in to Azure Container Registry**:

    ```bash
    docker login cellseg.azurecr.io
    ```

3. **Push the Docker image**:

    ```bash
    docker push cellseg.azurecr.io/cell:latest
    ```

### Deployment Steps

1. Build the Docker image of the source code.
2. Push the Docker image to Azure Container Registry.
3. Launch the web app server in Azure.
4. Pull the Docker image from the container registry to the web app server and run the application.

## Save Pass

Save pass: `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
