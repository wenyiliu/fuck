# -*- coding: utf-8 -*-

"""
  @date  2019-10-08 
  @author  liuwenyi
  
"""
from aip import AipSpeech
import os

""" 你的 APPID AK SK """
APP_ID = '16007034'
API_KEY = '9cVZDkCrl0sZP3wpQlMeqZq2'
SECRET_KEY = 'lGTYdBrcomGUAgfPCt2jrYO9Rg68IMAB'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def change_to_mp3(content='', turn=1, mp3_name='17k'):
    result = client.synthesis(content, 'zh', 1, {
        'vol': 5, 'per': 0, 'spd': 3
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
        if turn:
            os.system(
                "gnome-terminal -e 'ffmpeg -y  -i auido.mp3  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s.pcm '" % (
                    mp3_name))


change_to_mp3(
    content='患者自诉一年前出现打鼾，初期罕有短暂鼾声且鼾声靠近口鼻可闻，家长未带其治疗。'
            '今年十月份因反复感冒引起每天前半夜持续性打鼾，且鼾声身边可闻，同时伴有憋气症状，'
            '症状持续至今。2018.10.18：患者于浙江省儿保耳鼻喉科就诊，主诉因感冒引起每天整晚持续性打鼾，'
            '鼾声身边可闻，同时伴有憋气症状一月余。X线片显示腺样体肥大。诊断为腺样体肥大，医生建议预约睡眠监测(已预约)，'
            '予糠酸莫米松鼻喷雾剂*1瓶QD；孟鲁司特钠咀嚼片4mg(顺尔宁)*2盒QD治疗，十天后复查。',
    turn=1, mp3_name='17k')
