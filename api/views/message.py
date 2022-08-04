import random
from multiprocessing.spawn import import_main_path
from winreg import REG_NOTIFY_CHANGE_SECURITY
from django.views import View
from django.http import JsonResponse
from sympy import content
from app01.models import Avatars, UserInfo, Message
from django.db.models import F
from app01.utils.comment import find_root, find_root_sub

# 发布留言
class AddMessageView(View):
    def post(self, request):
        res = {
            'msg': '发布留言成功！',
            'code': 412
        }
        
        # 获取并校验数据
        data = request.data
        content = data['content']
        if not content:
            res['msg'] = '留言内容为空！'
            return JsonResponse(res)
        
        # 校验登录
        name = request.user
        user_obj = UserInfo.objects.filter(username=name).first()
        avatar_list = [i.nid for i in Avatars.objects.all()]
        if not name:
            res['msg'] = '你还没有登录，将以游客身份留言'
            name = '游客'
            avatar_id = random.choice(avatar_list)
        else:
            # avatar_id = request.user['avatar_id']
            avatar_id = user_obj.avatar_id

        message_obj = Message.objects.create(
            content=content,
            name=name,
            avatar_id=avatar_id
        )
        res['code'] = 0
        return JsonResponse(res)
