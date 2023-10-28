import os

from huggingface_hub import hf_hub_download
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, Pipeline, pipeline

HUGGING_FACE_API_KEY = os.environ.get("HUGGING_FACE_API_KEY")
MODEL_ID = "google/flan-t5-large"


def get_llm_model():
    filenames = [
        "config.json",
        "flax_model.msgpack",
        "generation_config.json",
        "model.safetensors",
        "pytorch_model.bin",
        "special_tokens_map.json",
        "spiece.model",
        "tf_model.h5",
        "tokenizer.json",
        "tokenizer_config.json",
    ]

    for filename in filenames:
        hf_hub_download(repo_id=MODEL_ID, filename=filename, token=HUGGING_FACE_API_KEY)


def get_llm_pipeline() -> Pipeline:
    get_llm_model()

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, legacy=False)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID)

    return pipeline(
        "text2text-generation",
        model=model,
        device=-1,
        tokenizer=tokenizer,
        max_length=1000,
    )
