import vk_api,re,datetime,json,os
#Использование:
#              Авторизация:
#1. audio_obj = audio(login='login',password='password')
#
#2. vk = vk_api.VkApi(login='login',password='password')
#   vk.auth()
#   audio_obj = audio(vk)
#
#           Дальнейшие действия:
#1. map_audio_object = audio_obj.get()                                              <- map объект
#   for i in map_audio_object:
#       print(i.title,i.artist,i.image,i.duration,i.owner_id,i.full_id,i.image)
#2. list_audio_object = audio_obj.get(need_list=True,owner_id=1234567,offset=10)    <- list
#   print(list_audio_object[0].title,list_audio_object[10].artist)
#3. list_audio_object = audio_obj.get(need_list=True)                               <- list
#   list_audio_object[3].edit(title="Новое название",artist="Новый артист!")
#   list_audio_object[3].delete()
#   list_audio_object[3].restore()
class audio(object):
    hashes=''
    def __init__(this,vk=None,login=None,password=None):
        "Модуль аудио вк. vk - vk_api.VkApi или login и пароль"
        if vk is None:vk=vk_api.VkApi(login,password);vk.auth()
        this.vk=vk;
        this.uid = this.vk.method("users.get")[0]["id"]
        this.vk.http.headers['Upgrade-Insecure-Requests']= "1"
        this.vk.http.cookies.set('remixaudio_background_play_time_','0');
        this.vk.http.cookies.set('remixaudio_background_play_time_limit','1800');
        this.vk.http.cookies.set('remixaudio_show_alert_today','0');
        this.vk.http.cookies.set('remixff','10');
        this.vk.http.cookies.set('remixmaudioq','');
        this.vk.http.cookies.set('remixaudio_date',datetime.datetime.now().date().strftime("%Y-%m-%d"))
        this.vk.http.cookies.set('remixmdevice','1280/800/1/!!-!!!!')
        this.vk.http.headers['X-Requested-With']='XMLHttpRequest'
    def delete_audio(this,owner_id,audio_id):
        return this.vk.method("audio.delete",{"owner_id":owner_id,"audio_id":audio_id})
    def add_audio(this,owner_id,audio_id):
        return this.vk.method("audio.add",{"owner_id":owner_id,"audio_id":audio_id})
    def get_hashes(this,owner_id,audio_id):
        this.vk.http.cookies.set('remixmaudio',owner_id+"_"+audio_id+'_search')
        this.text = vk.http.get(f"https://m.vk.com/audio{owner_id+'_'+audio_id}").text
        h = re.findall('\{"add_hash"\:"(.+?)"\,"del_hash"\:"(.+?)","res_hash":"(.+?)","use_new_stats":true}',this.text)
        this.add_hash,this.del_hash,this.res_hash =h[0]
    def get(this,owner_id=None,offset=0,need_list=False):
        if offset==0:
            del this.vk.http.headers['X-Requested-With'];
            text = this.vk.http.get(f"https://m.vk.com/audio{('s'+str(owner_id)) if owner_id is not None else ''}").text;
            this.vk.http.headers['X-Requested-With']='XMLHttpRequest'
            all_audio = re.findall('"_cache":(.+?),"soft_filter":true|false,"need_invalid_keys":true|false,"top_len":\d+,',text)
            this.ans_stupid = json.loads(all_audio[0] if len(all_audio)>0 and len(all_audio[0])!=0 else "{}")
        else:
            u_t_p="https://m.vk.com/audios"+(str(owner_id)if owner_id is not None else str(this.uid))
            t = this.vk.http.post(u_t_p,data={"_ajax":1,'offset':offset}).json()['data']
            this.ans_stupid=t[0]if t[0]else[]+t[1]if t[1]else[]+t[2]if t[2]else[]
        return list(map(this._as_object,this.ans_stupid)) if need_list else map(this._as_object,this.ans_stupid)
    def _as_object(this,i):
        q = this.ans_stupid[i]
        id = i.split("_")[1]
        owner_id=i.split("_")[0]
        sig=q[1][13].split("/")
        sig = sig[2]+"_"+sig[5]
        return Audio_obj(id,owner_id,sig,
                     q[1][3],q[1][4],q[1][5],
                     q[1][14].split(",")[0],
                     this.encode_url,this.vk
                     )
                     
        
    def encode_url(this,url):
        if(__name__=='__main__'):
            from decoder import decode_audio_url
        else:
            from .decoder import decode_audio_url
        return decode_audio_url(url,this.uid)
class Audio_obj(object):
    __is_url=None
    def __init__(this,id,owner_id,sig,artist,title,duration,image,encode,vk):
        this.title=title;
        this.id=id;
        this.owner_id=owner_id;
        this.__url=sig;
        this.artist=artist;
        this.title=title;
        this.duration=duration;
        this.image=image;
        this.full_id=f"{owner_id}_{id}";
        this.__encode=encode;
        this.__vk=vk;
    @property
    def url(self):
        if self.__is_url is None:self.__is_url = self.__encode(self.__get_url(self.__url))
        return self.__is_url
    def edit(self,title=None,artist=None):
        ans= self.__vk.method("audio.edit",{"owner_id":self.owner_id,
                                                            "audio_id":self.id,
                                                            "title":title if title is not None else self.title,
                                                            "artist":artist if artist is not None else self.artist
                                  }
            )
        if(title is not None):self.title=title
        if(artist is not None):self.artist=artist
        
    def delete(self):
        return self.__vk.method("audio.delete",{"owner_id":self.owner_id,"audio_id":self.id})
    def restore(self):
        return self.__vk.method("audio.restore",{"owner_id":self.owner_id,"audio_id":self.id})

    def __get_url(self,url):
        self.__vk.http.headers['Upgrade-Insecure-Requests']= "1"
        self.__vk.http.headers['X-Requested-With']='XMLHttpRequest'
        resp = self.__vk.http.post('https://m.vk.com/audio',data={
            'act': 'reload_audio',
            'ids': f"{self.full_id}_{self.__url}"}).json()
        return resp['data'][0][0][2]
if __name__=="__main__":
    if(input("хотите протестировать работу? ( если нет - просто нажмите enter )")):
        vk = vk_api.VkApi(input("введите логин"),input("введите пароль"))
        vk.auth()
        a= audio(vk)
        c = False
        for i,item in enumerate(a.get(offset=0)):
            if(not c):os.startfile(item.url)
            print(f"{i+1}.{item.artist} {item.title}")
            c=True
