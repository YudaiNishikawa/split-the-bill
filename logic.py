
import unicodedata

def calculattion_of_split_the_bill(payment_status):
    """精算リストの生成"""
    #logic of calculaion
    amount_list=[i["amount"] for i in payment_status]
    total=sum(amount_list)
    N=len(amount_list)
    average=(total+N+1)//N
    surplus=-(total-N*average)

    #update　lsit
    pay_list=[n-average for n in amount_list]
    max_index=pay_list.index(max(pay_list))
    pay_list[max_index]+=surplus

    for i in range(N):
        payment_status[i]["pay"]=pay_list[i]
    # import json
    # print(json.dumps(payment_status))   #This code is for conformimg container of dictionary

    payers=[i for i in payment_status if i["pay"]<0]
    payers.sort(key=lambda x:abs(x["pay"]),reverse=True)
    receivers=[i for i in payment_status if i["pay"]>0]
    receivers.sort(key=lambda x:x["pay"],reverse=True)

    results=[]
    while payers:
        send=min(abs(payers[0]["pay"]),receivers[0]["pay"])

        results.append(f"{payers[0]['name']}さんが{receivers[0]['name']}さんに{send}円支払う")
        
        payers[0]["pay"]+=send
        receivers[0]["pay"]-=send
        if payers[0]["pay"]==0:
            payers.pop(0)
        if receivers[0]["pay"]==0:
            receivers.pop(0)
    #print(f'{payers[0]["name"]}さんが{receivers[0]["name"]}さんに{send}円払う')
    return(results)

def get_payment_status_from_ui(ui_inputs):
    """UI入力内容を整える"""
    cleaned_status=[]
    
    for i,item in enumerate(ui_inputs):#enumerateにより要素にindexがつく
        raw_name=item.get("name","").strip()#get()によりnameがなくても""を返す、strip()によって前後の空白をなくす
        name=raw_name if raw_name else f"メンバー{i+1}"

        raw_amount=item.get("amount","")
        normalized=unicodedata.normalize("NFKC",str(raw_amount)).replace(",","")#ここでraw_amountはstr型に変化している
    
        try:
            amount=int(normalized)#str型からint型へ
        except ValueError:
            amount=0#空文字や変換不能は0
        cleaned_status.append({"name":name,"amount":amount})
    return cleaned_status