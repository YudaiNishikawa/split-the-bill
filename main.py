
import flet as ft#エラーが起きたら仮想環境を作成
from logic import calculattion_of_split_the_bill,get_payment_status_from_ui

def main(page:ft.Page):
    page.title="Split The Bill"
    page.scroll="auto"#画面が長くなった際にスクロール可能に

    input_rows=[]#入力行を管理するリスト
    inputs_container=ft.Column()#入力行だけをまとめる
    result_text=ft.Text()#結果を表示するエリア
    



    def add_clicked(e):#+ボタンが押された際の処理
        name_field=ft.TextField(label="名前",width=150)
        amount_field=ft.TextField(label="支払った額",width=150,suffix=ft.Text("円"))#末尾に円がつく
        
        row=ft.Row([name_field,amount_field])
        input_rows.append({"name":name_field,"amount":amount_field})
        inputs_container.controls.append(row)
        page.update()
        
    def calcu_clicked(e):   
        ui_data=[]
        for i in input_rows:
            ui_data.append({"name":i["name"].value,"amount":i["amount"].value})
        
        cleaned=get_payment_status_from_ui(ui_data)
        results=calculattion_of_split_the_bill(cleaned)

        if not results:
            result_text.value="精算の必要はありません"
        else:
            res_str="\n".join(results)
            result_text.value=f"【計算結果】\n{res_str}"
        page.update()
    
    for _ in range(2):
        add_clicked(None)#ボタンを押されていないが(None)関数を実行する
    
    page.add(
        inputs_container,
        ft.Divider(),
        ft.Button("+ メンバーの追加",on_click=add_clicked),
        ft.Button("計算する",on_click=calcu_clicked, bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE),
        result_text
    )

if __name__ == "__main__":
    ft.app(target=main)# port=0 は空いているポートを自動で使う、host="0.0.0.0" はネットワーク公開を許可する設定です
