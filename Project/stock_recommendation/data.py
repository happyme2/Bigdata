import pandas as pd

def data_load():
    path = 'C:\\Users\\USER\\Desktop\\stock_recommendation\\file\\'
    
    #user_item_df
    train_df= pd.read_excel(path+'train.xlsx',index_col=0) 
    user_item_df = train_df.pivot_table(index = '고객구분코드', columns = ['평균거래대금구간', '변동률구간'], values = '주문일자', aggfunc = 'count').fillna(0)

    #predict_df
    predict_df = pd.read_csv(path+'predict_df_4.csv', encoding = 'cp949')
    predict_df.drop([0,1], axis = 0, inplace = True)
    predict_df.drop('평균거래대금구간', axis = 1, inplace = True)
    predict_df.columns = user_item_df.columns
    predict_df.index = user_item_df.index

    #item_df
    item_df = pd.read_excel(path+'item.xlsx',index_col=0)

    #check_matrix
    check_matrix = train_df.pivot_table(index = '고객구분코드', columns = '종목코드', values = '주문일자', aggfunc = 'count').fillna(0)

    #profit_df
    profit_df = pd.read_excel(path+'profit.xlsx',index_col=0)
    
    return user_item_df,predict_df,item_df,check_matrix,profit_df