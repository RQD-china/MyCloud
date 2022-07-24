from app01.models import Comment

# 寻找根评论
def find_root(comment: Comment):
    if comment.parent_comment:
        return find_root(comment.parent_comment)
    return comment

# 寻找根评论的子评论列表
def find_root_sub(root, sub_list):
    for sub_comment in root.comment_set.all():
        sub_list.append(sub_comment)
        find_root_sub(sub_comment,sub_list)

# 获取评论列表
def get_comment(nid):
    # 找到某个文章的所有评论
    comment_query = Comment.objects.filter(article_id = nid).order_by ('-create_time')
    comment_list = []
    
    for comment in comment_query:
        if not comment.parent_comment:
            sub_list = []
            find_root_sub(comment, sub_list)
            def time(comment: Comment):
                return comment.create_time
            sub_list.sort(key=time)
            comment.sub_comment = sub_list
            comment_list.append(comment)
            continue
        
    return comment_list
    
