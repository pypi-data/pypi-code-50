def parabolic_sar(df, high="high",low="low",close="close", col="par_sar", initial_af=0.02,step_af=0.02, end_af=0.2):
        
  
    df['trend']=0
    df['sar']=0.0
    df['ep']=0.0
    df['af']=0.0
    df[col]=0.0

    #initial values for recursive calculation
    df['trend'][1]=1 if df[close][1]>df[close][0] else -1
    df['sar'][1]=df[high][0] if df['trend'][1]>0 else df[low][0]
    df.at[1,'real sar']=df['sar'][1]
    df['ep'][1]=df[high][1] if df['trend'][1]>0 else df[low][1]
    df['af'][1]=initial_af

    #calculation
    for i in range(2,len(df)):
        
        temp=df['sar'][i-1]+df['af'][i-1]*(df['ep'][i-1]-df['sar'][i-1])
        if df['trend'][i-1]<0:
            df.at[i,'sar']=max(temp,df[high][i-1],df[high][i-2])
            temp=1 if df['sar'][i]<df[high][i] else df['trend'][i-1]-1
        else:
            df.at[i,'sar']=min(temp,df[low][i-1],df[low][i-2])
            temp=-1 if df['sar'][i]>df[low][i] else df['trend'][i-1]+1
        df.at[i,'trend']=temp
    
        
        if df['trend'][i]<0:
            temp=min(df[low][i],df['ep'][i-1]) if df['trend'][i]!=-1 else df[low][i]
        else:
            temp=max(df[high][i],df['ep'][i-1]) if df['trend'][i]!=1 else df[high][i]
        df.at[i,'ep']=temp
    
    
        if np.abs(df['trend'][i])==1:
            temp=df['ep'][i-1]
            df.at[i,'af']=initial_af
        else:
            temp=df['sar'][i]
            if df['ep'][i]==df['ep'][i-1]:
                df.at[i,'af']=df['af'][i-1]
            else:
                df.at[i,'af']=min(end_af,df['af'][i-1]+step_af)
        df.at[i,'real sar']=temp
       
        
    return df