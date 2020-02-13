# coding=utf-8
import requests
import parsel

page_num=0
for page in range(0,200+1,50): #
    page_num +=1
    print('第{}页数据'.format(page_num))
    base_url = 'https://tieba.baidu.com/f?kw=美女&ie=utf-8&pn={}'.format(page)  # 目标列表网页
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0;rv:11.0'}

    response = requests.get(base_url, headers=headers)  # 发送请求
    html_str = response.text

    html = parsel.Selector(html_str)
    title_url = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href').extract()  # 网址后段

    second_url = 'https://tieba.baidu.com'  # 网址前段
    for url in title_url:
        all_url = second_url + url  # 拼接网址
        print('当前网页是：', all_url)
        response_2 = requests.get(all_url, headers=headers).text  # 进入网址
        response_2_base = parsel.Selector(response_2)
        result_list = response_2_base.xpath('//cc/div/img[@class="BDE_Image"]/@src').extract()  # 找到图片

        for li in result_list:
            img_data = requests.get(li, headers).content  # 访问图片
            img_name = li.split('/')[-1]  # 获取图片名称
            print('正在下载图片', img_name)
            with open(r'C:\Users\KY\Desktop\新建文件夹\美女\\' + img_name, 'wb') as f:
                f.write(img_data)