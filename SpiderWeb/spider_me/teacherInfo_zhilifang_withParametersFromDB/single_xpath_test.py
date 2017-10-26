from lxml import etree
text = """
    <div class="bd doulist-subject">
        <div class="source">
            来自：豆瓣读书
        </div>

        <div class="post">
            <a href="https://book.douban.com/subject/10519369/" target="_blank">
                <img width="100" src="https://img1.doubanio.com/lpic/s8869768.jpg">
            </a>
        </div>

        <div class="title">
            <a href="https://book.douban.com/subject/10519369/" target="_blank">
                万物生光辉
            </a>
        </div>

        <div class="rating">
            <span class="allstar50"></span>
            <span class="rating_nums">9.4</span>
            <span>(738人评价)</span>
        </div>

        <div class="abstract">
        "
                作者: [英] 吉米·哈利
        <br>
        "
                出版社: 中国城市出版社
        <br>
        "
                出版年: 2012-3
            "
        </div>
    </div>

    """

selector = etree.HTML(text)

title = selector.xpath('//div[@class="title"]/a/text()')
title = title[0]
title = title.replace(" ","").replace("\\n", "").replace("\\r", "")
title = title.strip()
print(title)

rate = selector.xpath('//span[@class="rating_nums"]/text()')
rate = rate[0]
rate = rate.replace(" ", "").replace("\\n", "").replace("\\r", "")
print(rate)

author = selector.xpath('//div[@class="abstract"]/text()')
author = author[0]
author = author.replace(" ", "").replace("\\n", "").replace("\\r", "").replace('"', "")
author = author.strip()
print(author)
