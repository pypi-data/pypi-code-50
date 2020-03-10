"""使用re模块解析曲谱(简谱)的程序。
A program that using re module to analyze music score (simplified score)."""
import winsound,math,time,re,sys
try:
    import timer
except ImportError:timer=None
try:
    import console_tool
except ImportError:COLORS=console_tool=None
else: COLORS=["white"]+console_tool.RAINBOW*2

music1="123 3 3 345 5 5  54321"
music2="53100 5310"
freqs=[None,264,297,330,352,396,440,495,528,556]
music_icon="\x0e"

__all__=["music","sinewave"]
__email__="3416445406@qq.com"
__author__="七分诚意 qq:3076711200 邮箱:%s"%__email__
__version__="1.0"

def print_icon(freq=None,icon=music_icon,console=None,
               color=None,normalcolor="magenta"):
    '在命令行打印音乐图标""'
    if console:
        if COLORS and (not color):
            if not freq in freqs:color=normalcolor
            else:color=COLORS[freqs.index(freq)]
        console.ctext(icon,color,end=" ",flush=True)
    else:print(icon,end=" ",flush=True)

def music(notation,duration):
    ##for pitch in notation:
    ##    if not pitch==" " or pitch=="-":
    ##        if pitch=="-":
    ##            yield freqs[prevpitch],duration
    ##        elif pitch=="0":time.sleep(duration/1000)
    ##        else:
    ##            yield freqs[pitch],duration
    ##            prevpitch=pitch
    "使用re模块解析曲谱的生成器"
    patt=re.compile(r"([0-9](\-| ){0,8})")
    for pitch in re.findall(patt,notation):
        pitch=pitch[0]
        if pitch[0]=="0":time.sleep(duration/1000)
        else:
            yield freqs[int(pitch[0])],duration*len(pitch)

def sinewave(times,duration=100):
    pitch=None
    for i in range(times):
        pitch=int(math.sin(i/6.28)*600+700)
        yield pitch,duration

def __demo(console=None):
    if timer:t=timer.Timer()
    else:t=None
    
    costed_time=0
    for freq,duration in music(music1,250):
        print_icon(freq,console=console)
        winsound.Beep(freq,duration)
        costed_time+=duration
    time.sleep(0.5)
    costed_time+=500
    print()
    for freq,duration in sinewave(times=100):
        print_icon(color="magenta",console=console)
        winsound.Beep(freq,duration)
        costed_time+=duration
    if t:
        print("\n预计用时:" ,costed_time/1000,"秒")
        print("实际用时:" , t.gettime() ,"秒")

def main():
    if console_tool:
        c=console_tool.Console()
        c.colorize()
    else:c=None
    if len(sys.argv)>1:
        for arg in sys.argv[1:]:
            try:
                f=open(arg,"r",encoding="utf-8")
                for freq,duration in music(f.read(),250):
                    print_icon(freq,console=c)
                    winsound.Beep(freq,duration)
                time.sleep(0.5)
            except OSError:
                print("文件 %s 未找到"%arg,file=sys.stderr)
    else:__demo(c)

if __name__=="__main__":main()
