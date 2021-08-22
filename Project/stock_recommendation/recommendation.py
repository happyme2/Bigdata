from data import data_load
import pandas as pd

### 1. 25개중에 거래안했던 칸의 종목을 추천
def recommendation(user_id,num_of_recom):

    user_item_df,predict_df,item_df,check_matrix,profit_df= data_load()
    
    penalty = 0.2

    temp = pd.concat([user_item_df.loc[[user_id]], predict_df.loc[[user_id]]], axis = 0)
    temp.index = ['user_item', 'predict']
    for index in temp.columns:
        if temp[index][0] != 0:
            temp[index][1] = temp[index][1] - penalty       ### penalty 추가
    temp_columns = temp.T.sort_values(by = 'predict', ascending = False).T.columns[0] ## penalty 추가한 predict중 젤 높은 구간
    item_recom = item_df[item_df.평균거래대금구간 == temp_columns[0]]
    item_recom = item_recom[item_recom.변동률구간 == temp_columns[1]]  ## 해당구간 종목들
    ### 거래했던 상품 제외
    item_recom = item_recom[item_recom.종목코드.isin(check_matrix.loc[user_id][check_matrix.loc[user_id] == 0].index)]
    
    ### 혹시나 해당구간 상품을 모두 거래했다면
    if len(item_recom) == 0:
        temp_columns = temp.T.sort_values(by = 'predict', ascending = False).T.columns[1]  ## 두번째 구간
        item_recom = item_df[item_df.평균거래대금구간 == temp_columns[0]]
        item_recom = item_recom[item_recom.변동률구간 == temp_columns[1]]
        item_recom = item_recom[item_recom.종목코드.isin(check_matrix.loc[user_id][check_matrix.loc[user_id] == 0].index)]
        final_df = profit_df[profit_df.종목코드.isin(item_recom.종목코드)].sort_values(by = '등락률', ascending = False)[:num_of_recom]
    
    else:
        final_df = profit_df[profit_df.종목코드.isin(item_recom.종목코드)].sort_values(by = '등락률', ascending = False)[:num_of_recom]
    
    return final_df
