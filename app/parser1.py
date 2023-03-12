import os
import random
import psycopg2
from psycopg2.extras import execute_values
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from slugify import slugify
base_url='https://rozetka.com.ua/headphones/c80027/'
#urls=[]
types_ = 'extra'
response = HTMLSession()
'''for i in range(1,2):
    url = f'https://rozetka.com.ua/headphones/c80027/page={i};21078=tws-2-razdelno,vakuumnie,2726;21079=2731;21806=dlya-telefona/'
    html = response.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    contain = soup.find('rz-grid',class_="ng-star-inserted").find_all('li')
    for j in contain:
        try:
            a = j.find('a')['href']
        except:
            a = None
        urls.append(a)'''
urls=['https://rozetka.com.ua/ua/defunc_d4271m/p296932928/', None, 'https://rozetka.com.ua/ua/defunc_d4271m/p296932928/', 'https://rozetka.com.ua/ua/defunc_d4274m/p297022453/', 'https://rozetka.com.ua/ua/defunc_d4276m/p320436982/', 'https://rozetka.com.ua/ua/defunc_d4275m/p320436985/', 'https://rozetka.com.ua/ua/defunc_d4273m/p320432248/', 'https://rozetka.com.ua/ua/defunc_d4272m/p296988478/', 'https://rozetka.com.ua/ua/logitech_985_001182/p366117102/', 'https://rozetka.com.ua/ua/logitech_985_001182/p366117102/', 'https://rozetka.com.ua/ua/logitech_985_001183/p366117165/', 'https://rozetka.com.ua/ua/sony_wfc500d_ce7/p335691736/', None, 'https://rozetka.com.ua/ua/defunc_d4214/p267878356/', None, 'https://rozetka.com.ua/ua/defunc_d4211/p267873376/', 'https://rozetka.com.ua/ua/defunc_d4214/p267878356/', 'https://rozetka.com.ua/ua/defunc_d4216/p267878401/', 'https://rozetka.com.ua/ua/defunc_d4215/p267878386/', 'https://rozetka.com.ua/ua/defunc_d4213/p267878346/', 'https://rozetka.com.ua/ua/defunc_d4212/p267878191/', 'https://rozetka.com.ua/ua/samsung_sm_r510nlvasek/p349736922/', None, 'https://rozetka.com.ua/ua/samsung_sm_r510nlvasek/p349736922/', 'https://rozetka.com.ua/ua/samsung_sm_r510nzwasek/p349743921/', 'https://rozetka.com.ua/ua/samsung_sm_r180nznasek/p238811347/', 'https://rozetka.com.ua/ua/samsung_sm_r180nzkasek/p238792495/', 'https://rozetka.com.ua/ua/samsung_sm_r180nznasek/p238811347/', 'https://rozetka.com.ua/ua/samsung_sm_r180nzwasek/p238811953/', 'https://rozetka.com.ua/ua/apple-pro-with-magsafe-charging-case-2022-2-e-pokolenie/p352490850/', 'https://rozetka.com.ua/ua/huawei_55034952/p350661462/', 'https://rozetka.com.ua/ua/defunc-d4311/p356138040/', None, 'https://rozetka.com.ua/ua/defunc-d4311/p356138040/', 'https://rozetka.com.ua/ua/defunc-d4314/p362376219/', 'https://rozetka.com.ua/ua/defunc-d4316/p362376222/', 'https://rozetka.com.ua/ua/defunc-d4315/p362376231/', 'https://rozetka.com.ua/ua/defunc-d4313/p362376228/', 'https://rozetka.com.ua/ua/defunc-d4312/p356142477/', 'https://rozetka.com.ua/ua/apple-mpny3ty-a/p353550168/', 'https://rozetka.com.ua/ua/huawei_55036650/p363258609/', 'https://rozetka.com.ua/ua/huawei_55036650/p363258609/', 'https://rozetka.com.ua/ua/huawei_55036649/p363258612/', 'https://rozetka.com.ua/ua/huawei_55036651/p363258606/', 'https://rozetka.com.ua/ua/xiaomi_6957141405505/p142831103/', 'https://rozetka.com.ua/ua/jbl_jblwbudsblk/p367813299/', 'https://rozetka.com.ua/ua/jbl_jblwbudsblk/p367813299/', 'https://rozetka.com.ua/ua/jbl_jblwbudswht/p367813302/', 'https://rozetka.com.ua/ua/xiaomi-bhr5489gl/p363180225/', 'https://rozetka.com.ua/ua/beatbox_bbppro1wcb/p301052013/', 'https://rozetka.com.ua/ua/beatbox_bbppro1wcb/p301052013/', 'https://rozetka.com.ua/ua/beatbox_bbppro1wcbr/p349601304/', 'https://rozetka.com.ua/ua/beatbox_bbppro1wcw/p301055198/', 'https://rozetka.com.ua/ua/beatbox_bbppro1wcwr/p349606683/', 'https://rozetka.com.ua/ua/samsung_sm_r177nzwasek/p313512175/', 'https://rozetka.com.ua/ua/samsung_sm_r177nzkasek/p313489399/', 'https://rozetka.com.ua/ua/samsung_sm_r177nlvasek/p313512172/', 'https://rozetka.com.ua/ua/samsung_sm_r177nzgasek/p313512166/', 'https://rozetka.com.ua/ua/samsung_sm_r177nzwasek/p313512175/', 'https://rozetka.com.ua/ua/jbl-jblwflexblk/p367908939/', 'https://rozetka.com.ua/ua/jbl-jblwflexblk/p367908939/', 'https://rozetka.com.ua/ua/jbl-jblwflexwht/p367909464/', 'https://rozetka.com.ua/ua/jbl_jblwbeamblk/p367813344/', 'https://rozetka.com.ua/ua/jbl_jblwbeamblk/p367813344/', 'https://rozetka.com.ua/ua/jbl_jblwbeamwht/p367813347/', 'https://rozetka.com.ua/ua/beatbox_bbpair2wcb/p301066823/', 'https://rozetka.com.ua/ua/beatbox_bbpair2wcb/p301066823/', 'https://rozetka.com.ua/ua/beatbox_bbpair2wcbr/p349606686/', 'https://rozetka.com.ua/ua/beatbox_bbpair2wcw/p301097733/', 'https://rozetka.com.ua/ua/beatbox_bbpair2wcwr/p349606689/', 'https://rozetka.com.ua/ua/anker_a3952gq1_a3952hq1/p337209058/', None, 'https://rozetka.com.ua/ua/anker_a3952ga1/p337209061/', 'https://rozetka.com.ua/ua/anker_a3952gq1_a3952hq1/p337209058/', 'https://rozetka.com.ua/ua/358042887/p358042887/', 'https://rozetka.com.ua/ua/oppo_enco_air_2_w13_ete11_blue/p344376319/', 'https://rozetka.com.ua/ua/sony-wic100b-ce7/p359748258/', 'https://rozetka.com.ua/ua/sony-wic100b-ce7/p359748258/', 'https://rozetka.com.ua/ua/sony-wic100l-ce7/p359748273/', 'https://rozetka.com.ua/ua/sony-wic100w-ce7/p359748267/', 'https://rozetka.com.ua/ua/pixus_alien/p335900782/', 'https://rozetka.com.ua/ua/sennheiser_509180/p345724510/', 'https://rozetka.com.ua/ua/sennheiser_509180/p345724510/', 'https://rozetka.com.ua/ua/sennheiser_700074/p345724537/', 'https://rozetka.com.ua/ua/sennheiser_509181/p345728749/', 'https://rozetka.com.ua/ua/marshall_1005964/p348792777/', 'https://rozetka.com.ua/ua/gelius_2099900822988/p268358846/', 'https://rozetka.com.ua/ua/gelius_2099900822971/p268323221/', 'https://rozetka.com.ua/ua/gelius_2099900822988/p268358846/', 'https://rozetka.com.ua/ua/sony_wf_1000xm4s/p303539973/', 'https://rozetka.com.ua/ua/sony_wf_1000xm4b/p303537893/', 'https://rozetka.com.ua/ua/sony_wf_1000xm4s/p303539973/', 'https://rozetka.com.ua/ua/promate_freepods_3_black/p348277131/', 'https://rozetka.com.ua/ua/promate_freepods_3_black/p348277131/', 'https://rozetka.com.ua/ua/promate_freepods_3_blue/p348278271/', 'https://rozetka.com.ua/ua/promate_freepods_3_white/p348278268/', 'https://rozetka.com.ua/ua/oppo-enco-air2-pro-ete21-white/p354318834/', 'https://rozetka.com.ua/ua/panasonic_rz_b100wge_w/p305911783/', None, 'https://rozetka.com.ua/ua/panasonic_rz_b100wge_k/p305888628/', 'https://rozetka.com.ua/ua/panasonic_rz_b100wge_w/p305911783/', 'https://rozetka.com.ua/ua/anker_a3983h11/p352305267/', 'https://rozetka.com.ua/ua/promate_epic_black/p365481465/', None, 'https://rozetka.com.ua/ua/anker-a3936g11/p361730169/', None, 'https://rozetka.com.ua/ua/proda_prd_bt112wt/p346128400/', 'https://rozetka.com.ua/ua/philips_tat1207bk_00/p350246325/', 'https://rozetka.com.ua/ua/philips_tat1207bk_00/p350246325/', 'https://rozetka.com.ua/ua/philips_tat1207wt_00/p350246361/', 'https://rozetka.com.ua/ua/1more-960737/p362655270/', 'https://rozetka.com.ua/ua/1more-960737/p362655270/', 'https://rozetka.com.ua/ua/1more-960738/p362655663/', 'https://rozetka.com.ua/ua/oppo-enco-x2-ete01-black-oppo/p350853450/', 'https://rozetka.com.ua/ua/oppo-enco-x2-ete01-black-oppo/p350853450/', 'https://rozetka.com.ua/ua/oppo-enco-enco-x2-ete01-white-oppo/p350856918/', 'https://rozetka.com.ua/ua/canyon_cne_cbths3w/p268986696/', None, 'https://rozetka.com.ua/ua/canyon_cne_cbths3b/p268986656/', 'https://rozetka.com.ua/ua/canyon_cne_cbths3w/p268986696/', 'https://rozetka.com.ua/ua/beatbox_bbppro6b/p349384572/', 'https://rozetka.com.ua/ua/beatbox_bbppro6b/p349384572/', 'https://rozetka.com.ua/ua/beatbox_bbppro6bl/p349387062/', 'https://rozetka.com.ua/ua/beatbox_bbppro6o/p349387065/', 'https://rozetka.com.ua/ua/beatbox_bbppro6p/p349387068/', 'https://rozetka.com.ua/ua/beatbox_bbppro6w/p349387071/', 'https://rozetka.com.ua/ua/anker-a3961g91/p361727706/', None, 'https://rozetka.com.ua/ua/xiaomi-t10probk/p326159293/', 'https://rozetka.com.ua/ua/beatbox_bbppromw/p349387122/', 'https://rozetka.com.ua/ua/358042884/p358042884/', 'https://rozetka.com.ua/ua/358042881/p358042881/', 'https://rozetka.com.ua/ua/358042884/p358042884/', 'https://rozetka.com.ua/ua/defunc_d4241/p286060278/', None, 'https://rozetka.com.ua/ua/358042893/p358042893/', 'https://rozetka.com.ua/ua/358042890/p358042890/', 'https://rozetka.com.ua/ua/358042893/p358042893/', 'https://rozetka.com.ua/ua/358042896/p358042896/', 'https://rozetka.com.ua/ua/358042899/p358042899/', 'https://rozetka.com.ua/ua/xiaomi_897741/p362800596/', 'https://rozetka.com.ua/ua/anker-a3961g21/p361727565/', None, 'https://rozetka.com.ua/ua/ergo_bs_740w/p363258618/', 'https://rozetka.com.ua/ua/ergo_bs_740k/p363258615/', 'https://rozetka.com.ua/ua/ergo_bs_740w/p363258618/', 'https://rozetka.com.ua/ua/anker-a3936g21/p361731012/', None, 'https://rozetka.com.ua/ua/pixus_storm/p335900980/', 'https://rozetka.com.ua/ua/sennheiser_509247/p345733168/', 'https://rozetka.com.ua/ua/baseus_ngtw030102/p367382691/', 'https://rozetka.com.ua/ua/x_digital_hbs_110k/p363481464/', None, 'https://rozetka.com.ua/ua/x_digital_hbs_110k/p363481464/', 'https://rozetka.com.ua/ua/x_digital_hbs_110w/p363481467/', 'https://rozetka.com.ua/ua/promate-rippleblack/p346649994/', 'https://rozetka.com.ua/ua/promate-rippleblack/p346649994/', 'https://rozetka.com.ua/ua/promate-rippleblue/p346660971/', 'https://rozetka.com.ua/ua/ergo-bs-900k/p367908777/', 'https://rozetka.com.ua/ua/a4tech_4711421978651/p362398896/', 'https://rozetka.com.ua/ua/jbl_jblt125btwht/p291422343/', 'https://rozetka.com.ua/ua/ergo-bs-730w/p363176613/', 'https://rozetka.com.ua/ua/ergo-bs-730k/p363175821/', 'https://rozetka.com.ua/ua/ergo-bs-730w/p363176613/', 'https://rozetka.com.ua/ua/a4tech_4711421978378/p362398893/', 'https://rozetka.com.ua/ua/a4tech_4711421978446/p362398890/', 'https://rozetka.com.ua/ua/a4tech_4711421978378/p362398893/']
print(1)
id=0
count=0
args=[]
slug_check=[]
brands=['oppo','huawei','tecno','vivo','xiaomi','samsung','realme']
corpuses=['алюминий','пластик']
vids=['вкладыши','накладные']
descriptions = ['Все лучшее для пользователя собрано в этой маленькой компактной оболочке вакуумного типа. Наушники стали идеальным средством прослушивания музыки, осуществления голосовых вызовов, гейминга посредством применения мобильных устройств.',
                'Компактный зарядный кейс весом всего 45 граммов сочетает в себе миниатюрный, минималистический дизайн и батарею емкостью 400 mAh. Время работы таких компактных и одновременно мощных наушников составит до 5 часов без подзарядки и до 22 часов вместе с зарядным кейсом.',
                'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
                'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
                'новые беспроводные наушники Huawei, доступные каждому. Модель ориентирована на покупателей, выбирающих устройство с оптимальным соотношением цена-качество, покупают первые TWS-наушники.',
                'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
                'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
                'Беспроводные наушники нового поколения подключаются при помощи Bluetooth 5.0 и используют технологию TWS для первоклассного 3D стереозвука. Двойной микрофон еще лучше справляется с шумоподавлением. Наушники выполнены в компактном и ультра лёгком корпусе, что позволяет им крепко держаться в ушах даже при занятии спортом. Наушники так же могут использоваться по отдельности как беспроводная гарнитура, когда вы за рулем.',
                'Технология JBL Deep Bass Sound До 6 часов оспроизведения плюс 20 в чехле с возможностью быстрой зарядки Стереозвонки в режиме «hands-free»',
                'Неисчерпаемый источник энергии для любителей музыки. обеспечивают до 24 часов воспроизведения любимых музыки и видео.']
dop_infa=['наушники типа -C EO-IC100','есть 2 режима записи наушника','идёт в комплект чистка для наушников']
for i in urls:
    try:
        id+=1
        if id==81:
            5+'k'
        html = response.get(i).text
        soup = BeautifulSoup(html, 'html.parser')
        name_ = soup.find('h1',class_='product__title').text[11:]
        slug_ = slugify(name_)
        brand_ = brands[random.randint(0,6)]
        if slug_ not in slug_check:
            slug_check.append(slug_)
        else:
            slug_ += f'{id}'
        pricef=soup.find('p',class_="product-price__big").text
        pricef=pricef.replace("₴",'')
        if not len(pricef)<=5:
            1+'5'
        if len(pricef)==5:
            pricef = pricef.replace(pricef[1], '')
        price_ = int(pricef)*308
        photes = soup.find('ul', class_="simple-slider__list ng-star-inserted")
        photo_1_ = photes.find('li').find('img')['src']
        photo_2_ = photes.find('li').find_next('li').find('img')['src']
        weight_ = str(random.randint(30,60))+' г'
        corpus_= corpuses[random.randint(0,1)]
        description_= descriptions[random.randint(0,9)]
        dop_infa_ = dop_infa[random.randint(0,2)]
        vid_=vids[random.randint(0,1)]
        i+='characteristics/'
        html = response.get(i).text
        soup = BeautifulSoup(html, 'html.parser')
        list_towar=soup.find('dl',class_="characteristics-full__list").find_all('div')
        for j in list_towar:
            if j.find('dt',class_="characteristics-full__label").text == 'Тип навушників':
                type_ = j.find('dd').text
            elif j.find('dt',class_="characteristics-full__label").text == 'Тип підключення':
                type_connection_ = j.find('dd').text.replace('Бездротові','Бездротовые')
            elif j.find('dt',class_="characteristics-full__label").text == "Інтерфейс під'єднання":
                enterface_ = j.find('dd').text + ' с микрофоном'
            elif j.find('dt',class_="characteristics-full__label").text == 'Колір':
                color_ = j.find('dd').text
            elif j.find('dt',class_="characteristics-full__label").text == 'Наявність активного шумозаглушення':
                anti_shum_ = 'с активным шумоподавлением'
            elif j.find('dt',class_="characteristics-full__label").text == 'Матеріал амбушур':
                ambushur_ = 'Силекон'
            elif j.find('dt',class_="characteristics-full__label").text == 'Тип випромінювача':
                type_vipe_ = 'Динамический'
            elif j.find('dt',class_="characteristics-full__label").text == "Рік випуску моделі":
                date_create_ = j.find('dd').text
            elif j.find('dt',class_="characteristics-full__label").text == 'Країна-виробник товару':
                country_ = j.find('dd').text
            elif j.find('dt',class_="characteristics-full__label").text == 'Гарантія':
                garantee_ = j.find('dd').text.replace('місяці','мес:')
                garantee_ = garantee_.replace('в','')
            elif j.find('dt',class_="characteristics-full__label").text == "Час роботи, год":
                time_work_ = j.find('dd').text+f' ч с аккамулятором'
        count_ = random.randint(25,50)
        rating_ = 5
    except:
        id -= 1
        count += 1
    else:
        try:
            args.append((id,name_, slug_, brand_,price_,photo_1_,photo_2_,type_,type_connection_,enterface_,color_,anti_shum_,ambushur_,type_vipe_,date_create_,country_,garantee_,time_work_,corpus_,description_,weight_,vid_,dop_infa_,types_,count_,rating_))
        except:
            id-=1
            count+=1
        else:
            print(id)
print(count)
con = psycopg2.connect(
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS'),
            host=os.environ.get('DB_HOST')
        )
cur = con.cursor()
execute_values(cur,"INSERT INTO phones_airpods (id,name, slug, brand,price,photo1,photo2,type,type_connection,enterface,color,anti_shum,ambushur,type_vipe,date_create,country,garantee,time_work,corpus,description,weight,vid,dop_infa,types,count,rating) VALUES %s",args)
con.commit()
con.close()