import sys,os
from cellSegmentation.pipeline.training_pipeline import TrainPipeline
from cellSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin
from cellSegmentation.constant.application import APP_HOST, APP_PORT



app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

