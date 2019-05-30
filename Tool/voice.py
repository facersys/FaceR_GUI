# -*- coding: utf-8 -*-

import tempfile
import os
import pygame
import time
from aip import AipSpeech
from Config import getConfig


def checked_voice(name):
    """
    语音合成，传入签到者姓名
    """
    client = AipSpeech(
        getConfig('baidu-aip', 'app_id'),
        getConfig('baidu-aip', 'api_key'),
        getConfig('baidu-aip', 'secret_key'),
    )

    result = client.synthesis(f'{name}同学，签到成功', 'zh', 1, {
        'vol': 15,
    })

    if not isinstance(result, dict):
        tempFile = tempfile.NamedTemporaryFile('wb', delete=False)
        tempFile.write(result)
        tempFile.close()

        pygame.mixer.init()
        clock = pygame.time.Clock()
        # 加载音乐
        track = pygame.mixer.music.load(tempFile.name)
        # 播放音乐
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        else:
            pygame.mixer.quit()
            try:
                os.remove(tempFile.name)
            except PermissionError:
                pass


if __name__ == '__main__':
    checked_voice('应赵康')
