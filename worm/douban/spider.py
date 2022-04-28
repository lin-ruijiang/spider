import urllib.error
import urllib.request
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    # savepath = ".\\豆瓣top250电影.xls"
    # saveData(datalist, savepath)
    # dbpath="movie.db"
    saveData2DB(datalist, dbpath)

    # askURL("https://movie.douban.com/top250?start=")


# 影片链接
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码

        soup = BeautifulSoup(html, "html.parser")

        # soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            # print(item)
            data = []
            item = str(item)

            link = re.findall(findLink, item)[0]
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。 ", "")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
            bd = re.sub('/', " ", bd)
            data.append(bd.strip())
            datalist.append(data)
    print(datalist)
    return datalist


def askURL(url):
    head = {}
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
    }
    # 用户代理表示告诉网站服务器我们是什么类型的机器——浏览器，本质上是告诉浏览器我们可以接收什么水平的文件内容。
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        respone = urllib.request.urlopen(request)
        html = respone.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e, "code")
        if hasattr(e, "reason"):
            print(e, "reason")
    return html


def saveData(datalist, savepath):
    print("save......")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    col = ('电影详情链接', "图片链接", "影片中文名", "影片外文名", "评分", "评分人数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save('movie.xls')


def saveData2DB(datalist, dppath):
    print("----")


def init_db(dbpath):
    sql = '''
    create table movie250
    (
    id integer primary key autoincrement,
    info_link text,
    pic_link text,
    cname varchar,
    ename varchar,
    score numeric,
    rated numeric,
    instroduction text,
    info text
    )
        '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.exexute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # main()
    init_db("movietest.db")

    print("爬取成功！")
