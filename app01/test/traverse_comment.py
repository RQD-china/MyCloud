import os
import sys

if __name__ == '__main__':
    # 加载Django项目的配置信息
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(BASE_DIR)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myCloud.settings')
    
    # 导入Django并启动
    import django
    
    django.setup()
    
    from app01.models import Articles, Comment
    
    # 找到某个文章的所有评论
    comment_query = Comment.objects.filter(article_id = 1)
    
    comment_dict = {}
    
    def find_root(comment: Comment):
        if comment.parent_comment:
            return find_root(comment.parent_comment)
        return comment
    
    for comment in comment_query:
        if not comment.parent_comment:
            # 把根评论放入字典
            comment_dict[comment.nid] = comment
            comment.sub_comment = []
            continue
    
    for comment in comment_query:
        for sub_comment in comment.comment_set.all():
            root_comment = find_root(sub_comment)
            comment_dict[root_comment.nid].sub_comment.append(sub_comment)
            
    for k, v in comment_dict.items():
        print('根评论：', v)
        for comment in v.sub_comment:
            print(' 子评论：', comment)
    