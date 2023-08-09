import flet as ft
import json

def load_chats():
    posts = []
    with open('data.json', 'r') as file:
        for line in file:
            post = json.loads(line)
            posts.append(post)
    return posts    

def main(page: ft.Page):
    page.scroll = True
    chats = load_chats()
    
    Column = ft.Column(expand=True)
    page.add(Column)

    data_rows = []
    for data in chats:
        data_row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(data["name"])),
                ft.DataCell(ft.Text(data["id"])),
                ft.DataCell(ft.Text(data["short_desc"])),
                ft.DataCell(ft.Text(data["long_desc"])),
                ft.DataCell(ft.Image(data["image"])),
                ft.DataCell(ft.Text(data["origin"])),
                ft.DataCell(ft.Text(data["dialouge"])),
                ft.DataCell(ft.Text(data["chat"])),
            ]
        )
        data_rows.append(data_row)

    Column.controls.append(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Name")),
                ft.DataColumn(ft.Text("id")),
                ft.DataColumn(ft.Text("short_desc")),
                ft.DataColumn(ft.Text("long_desc")),
                ft.DataColumn(ft.Text("image")),
                ft.DataColumn(ft.Text("origin")),
                ft.DataColumn(ft.Text("dialouge")),
                ft.DataColumn(ft.Text("chat")),
            ],
            rows=data_rows,
            column_spacing=40,  # Adjust the spacing value as needed
            data_row_height=80  ,
        )
    )
    
    page.update()

ft.app(target=main)
