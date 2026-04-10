from logic import get_payment_status_from_ui,calculattion_of_split_the_bill

def run_test():
    test_data=[
        {"name":"剣","amount":"２００"},#全角入力
        {"name":"","amount":"30"},#名前空白
        {"name":"john","amount":""}#金額空白
    ]

    print("=== テスト開始 ===")

    cleaned=get_payment_status_from_ui(test_data)
    print(f"データ整形完了:{cleaned}")

    results=calculattion_of_split_the_bill(cleaned)
    print("精算計算完了\n=== 送金指示 ===",*results,"=== テスト終了 ===",sep="\n")
    
if __name__=="__main__":#このファイルが「直接実行された時だけ」動くようにするおまじない
    run_test()


