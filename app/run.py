from h2o_wave import Q, main, app, ui

def base_cards(q):
    q.page['meta'] = ui.meta_card(box='')
    q.page['example'] = ui.form_card(box='1 1 -1 1', items=[
            ui.tabs(
                name="menu",
                value=q.args.menu or "Tab1",
                items=[
                        ui.tab(name='Tab1', label='Tab 1'),
                        ui.tab(name='Tab2', label='Tab 2'),
                ],),
            
        ])

@app('/')
async def serve(q: Q):
    if not q.client.initialized:
        base_cards(q)
        q.args.menu = 'Tab1'
        q.client.initialized = True

    if q.args.show_side_panel:
        base_cards(q)
        q.page['meta'].side_panel = ui.side_panel(title='Side Panel', items=[
            ui.text('This is the Side Panel'),
            ui.buttons([ui.button(name='next_step', label='Next', primary=True)])
        ])
    elif q.args.next_step:
        base_cards(q)
        q.page['meta'].dialog = ui.dialog(
            title='my_dialog',
            items=[
                ui.text('This is a sample text'),
                ui.buttons([
                    ui.button("Ok", "OK")
                ])
            ]
        )
    elif q.args.menu == "Tab2":
        base_cards(q)
        q.page['example2'] = ui.form_card(box='1 2 -1 -1', items=[
        ui.text('This is the Tab 2 Page'),
        ])
    elif q.args.menu == "Tab1":
        base_cards(q)
        q.page['example2'] = ui.form_card(box='1 2 -1 -1', items=[
        ui.text('This is the Tab 1 Page'),
        ui.button(name='show_side_panel', label='Show Panel', primary=True)
        ])
    else:
        base_cards(q)

    await q.page.save()