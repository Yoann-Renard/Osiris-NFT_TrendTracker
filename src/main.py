from fastapi import FastAPI, Response, status
import json

from classes.settings import *

app = FastAPI()


@app.get("/get_new_best_publications_ids")
async def get_best_lunched_publications_list(response: Response):
    if os.path.exists(os.path.join(VOLUME_PATH, "best_launch_result.json")):
        with open(os.path.join(VOLUME_PATH, "best_launch_result.json"), 'r') as f:
            result = json.load(f)
        response.status_code = status.HTTP_200_OK
        return result
    else:
        response.status_code = status.HTTP_204_NO_CONTENT
        return {
            "message": "No content"
        }
