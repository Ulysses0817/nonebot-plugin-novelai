import aiohttp
import base64
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent,MessageSegment
from nonebot.log import logger
from .translation import translate
start = "data:image/jpeg;base64,"
deepdanbooru = on_command(".gettag", aliases={"鉴赏", "查书"})


@deepdanbooru.handle()
async def deepdanbooru_handle(event: GroupMessageEvent):
    url=""
    for seg in event.message['image']:
        url=seg.data["url"]
    if url:
        async with aiohttp.ClientSession() as session:
            logger.info(f"正在获取图片")
            async with session.get(url) as resp:
                bytes = await resp.read()
        str_img = str(base64.b64encode(bytes), "utf-8")
        str0 = start+str_img
        message=MessageSegment.at(event.user_id)
        async with aiohttp.ClientSession() as session:
            async with session.post('https://hf.space/embed/mayhug/rf5-anime-image-label/api/predict/', json={"data": [str0, 0.2]}) as resp:
                if resp.status != 200:
                    await deepdanbooru.finish(f"识别失败，错误代码为{resp.status}")
                jsonresult = await resp.json()
                data=jsonresult['data'][0]
                logger.info(f"TAG查询完毕，{data}")
                tags=""
                for label in data['confidences']:
                    tags=tags+label["label"]+","
        tags_ch=await translate(tags.replace("_"," "),"zh-Hans")
        if tags_ch==tags.replace("_"," "):
            message=message+tags
        message=message+tags+f"\n机翻结果:"+tags_ch
        await deepdanbooru.finish(message)
    else:
        await deepdanbooru.finish(f"未找到图片")