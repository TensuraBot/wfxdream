from fastapi import FastAPI, Query
from gradio_client import Client

app = FastAPI()

@app.get("/api/wfx")
async def generate_image(prompt: str = Query("1girl, blue eyes, slime style")):
    try:
        client = Client("Asahina2K/animagine-xl-3.1")
        result = client.predict(
            prompt, "", 0, 512, 512, 1, 1, "Euler a", "896 x 1152",
            "Anime", "(None)", True, 0, 1, True,
            api_name="/run"
        )
        return {"status": True, "data": result}
    except Exception as e:
        return {"status": False, "error": str(e)}
