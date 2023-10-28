from extractor.youtube_dl import download_subtitles
from models.google_flan_t5 import get_llm_pipeline

VIDEO_ID = "2AZOhqTHZoo"


def main():
    pipe = get_llm_pipeline()
    # download_subtitles(VIDEO_ID)

    with open(f"videos/{VIDEO_ID}/subtitles_en.txt", "r") as f:
        transcript = f.read()

    print(
        pipe(
            f"""extract all the ratings and price of the product in this text: {transcript}"""
        )
    )


if __name__ == "__main__":
    main()
