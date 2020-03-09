import pandas as pd

data = {"name":["张三","张思","王五","李严"],
        "age":["12","12","12","12"],
        "city":["北京","北京","北京","北京"],
        "height":["187","187","187","187"]

}

data_frame=pd.DataFrame(data)
print(data_frame)