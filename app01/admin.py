from django.contrib import admin
from app01.models import *
from django.utils.safestring import mark_safe

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # 获取文章封面
    def get_cover(self):
        if self.cover:
            return mark_safe(f'<img src="{self.cover.url.url}" style="height: 60px;">')
        return
    get_cover.short_description = '文章封面'
    
    # 获取文章标签
    def get_tags(self):
        return ', '.join([i.title for i in self.tag.all()])
    get_tags.short_description = '文章封面'
    
    # 获取文章标题
    def get_title(self):
        return mark_safe(f'<a href="/article/{self.nid}/" target="_blank">{self.title}</a>')
    get_title.short_description = '文章封面'

    # 获取编辑按钮
    def get_edit_btn(self):
        return mark_safe(f"""
        <a href="/backend/edit_article/{self.nid}/" target="_blank">编辑</a>
        <a href="/admin/app01/articles/{self.nid}/delete/">删除</a>
         """)
    get_edit_btn.short_description = '操作'
    
    # 自定义字段
    list_display = [get_title,
                    get_cover,
                    get_tags,
                    'look_count',
                    'digg_count',
                    'comment_count',
                    'collects_count',
                    'word',
                    'change_date',
                    get_edit_btn]
    
    # 更新文章字数
    def update_word(self, request, queryset):
        for obj in queryset:
            word = len(obj.content)
            obj.word = word
            obj.save()
    update_word.type = 'success'
    update_word.short_description = '更新文章字数'
    
    # 自定义动作
    actions = [update_word]

# 注册
admin.site.register(Articles, ArticleAdmin)
admin.site.register(Tags)
admin.site.register(Cover)
admin.site.register(MenuImg)
admin.site.register(Comment)
admin.site.register(Avatars)
admin.site.register(UserInfo)
