from TikTokApi import TikTokApi
import asyncio
import os
from dotenv import load_dotenv
import cv2

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


ms_token = os.environ.get("MS_TOKEN", None)


async def trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False)
        async for video in api.trending.videos(count=30):
            print(video)
            print(video.as_dict)


async def main():
    pass


if __name__ == "__main__":
    asyncio.run(main())