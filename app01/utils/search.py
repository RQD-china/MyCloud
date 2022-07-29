from urllib.parse import urlencode

class Order:
    def __init__(self, key, order, order_list, query_params):
        self.order = order
        self.key = key
        self.order_list = order_list
        self.query_params = {}
        for i in query_params:
            self.query_params[i] = query_params.getlist(i)
    
    def order_html(self):
        order_list = []
        for li in self.order_list:
            self.query_params[self.key] = li[0]
            if self.order == li[0]:
                li = f'<li class="active"><a href="?{self.query_encode}">{li[1]}</a></li>'
            else:
                li = f'<li><a href="?{self.query_encode}">{li[1]}</a></li>'
            order_list.append(li)
        return ''.join(order_list)
    
    @property
    def query_encode(self):
        return urlencode(self.query_params, doseq=True)
        # return self.query_params.urlencode()
        
if __name__ == '__main__':
    order = Order(
        order='look_count',
        order_list=[('', '综合排序'),
                    ('-create_time', '最新发布'),
                    ('look_count', '最多浏览'),
                    ('digg_count', '最多点赞'),
                    ('comment_count', '最多评论'),
                    ('collects_count', '最多收藏')],
        query_params={"key": 'Java'}
    )
    print(order.order_html())
